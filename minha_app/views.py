# coding: utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material, Loan
from .forms import MaterialForm, LoanForm

from django.views.generic.base import TemplateView

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'login.html', {})

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'home.html', {})

def indexMaterials(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    materials = Material.objects.all()
    return render(request, 'materials/index.html', { 'materials': materials })

def createMaterials(request):
    form = MaterialForm(request.POST or None)
    if form.is_valid():
        form.instance.qnt_available = form.cleaned_data['qnt']
        form.save()
        return redirect('materials.index')
    return render(request,'materials/create.html', {'form':form})

def editMaterials(request, pk):
    material = Material.objects.get(pk=pk)
    form = MaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        form.save()
        return redirect('materials.index')
    return render(request,'materials/edit.html', {'form':form, 'material': material})

def deleteMaterials(request, pk):
    material = Material.objects.get(pk=pk)
    material.delete()
    return redirect('materials.index')

def indexLoans(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    loans = Loan.objects.all()
    return render(request, 'loans/index.html', { 'loans': loans })

def createLoans(request):
    form = LoanForm(request.POST or None)
    if form.is_valid():
        form.instance.responsible = request.user.get_full_name() + ' (' + request.user.username + ')'
        material = Material.objects.get(pk=form.cleaned_data['material'].pk)
        if material.qnt_available > 0:
            form.save()
        return redirect('loans.index')
    return render(request,'loans/create.html', {'form':form})

def editLoans(request, pk):
    loan = Loan.objects.get(pk=pk)
    form = LoanForm(request.POST or None, instance=loan)
    if form.is_valid():
        form.instance.responsible = request.user.get_full_name() + ' (' + request.user.username + ')'
        material = Material.objects.get(pk=form.cleaned_data['material'].pk)
        if (material.qnt_available == 0 and form.cleaned_data['returned']) or material.qnt_available > 0:
            form.save()
        return redirect('loans.index')
    return render(request,'loans/edit.html', {'form':form, 'loan': loan})

def deleteLoans(request, pk):
    loan = Loan.objects.get(pk=pk)    
    loan.delete()
    return redirect('loans.index')

class ErrorPage(TemplateView):
    template_name = 'error.html'