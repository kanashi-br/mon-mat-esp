# coding: utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Material
from .forms import MaterialForm

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
