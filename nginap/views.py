from django.shortcuts import render, redirect
from nginap.models import *
from nginap.forms import * 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else: 
            messages.success(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:   
        form = UserCreationForm()
        konteks = {
            'form' : UserCreationForm()
        }
    return render(request,'signup.html', konteks)

def index(request):
    data_peta = Penginapan.objects.all()
    data_peta_json = serializers.serialize('json', data_peta)
    nginaps = Penginapan.objects.all()
    judul = "Data Penginapan di Wilayah Tangerang"
    konteks = {
        "title": judul,
        "subtitle": judul,
        "nginaps" : nginaps,
        "dataJson" : data_peta_json,
        "dataPetas" : data_peta
    }
    return render(request, 'index.html', konteks)

@login_required(login_url= settings.LOGIN_URL)
def nginap(request):
    nginaps = Penginapan.objects.all()
    judul = "Data Penginapan di Wilayah Tangerang"
    konteks = {
        "title": judul,
        "subtitle": judul,
        "nginaps" : nginaps,
    }
    return render(request, 'penginapan.html', konteks)

@login_required(login_url= settings.LOGIN_URL)
def tambah_penginapan(request):
    if request.POST:
        form = FormPenginapan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPenginapan()
            judul = "Tambah Data Penginapan"
            pesan = "Data Berhasil Ditambahkan!"
            konteks = {
                "title" : judul,
                "subtitle" : judul,
                "form" : form,
                "pesan" : pesan,
            }
            return render(request, 'tambah_penginapan.html', konteks)
    else:
        form = FormPenginapan()
        judul = "Tambah Data Penginapan"
        konteks = {
            "title" : judul,
            "subtitle" : judul,
            "form" : form,
        }
    return render(request, 'tambah_penginapan.html', konteks)

@login_required(login_url= settings.LOGIN_URL)
def update_penginapan(request, id_nginap):
    nginap = Penginapan.objects.get(id= id_nginap)
    judul = "Edit Data Penginapan"
    template = "update_penginapan.html"

    if request.POST:
        form = FormPenginapan(request.POST, request.FILES, instance=nginap)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"  
            konteks = {
                "title" : judul,
                "subtitle" : judul,
                "pesan" : pesan,
                "form" : form,
                "nginap" : nginap
            }
            return render(request, template, konteks)
    else:
        form = FormPenginapan(instance=nginap)
        konteks = {
            "title" : judul,
            "subtitle" : judul,
            "form" : form,
            "nginap" : nginap
        }
    return render(request, template, konteks)

def delete_penginapan(request, id_nginap):
    nginap = Penginapan.objects.get(id= id_nginap)
    nginap.delete()

    return redirect("/penginapan/")

def detail_penginapan(request, id_nginap):
    nginap = Penginapan.objects.get(id= id_nginap)
    template = "detail.html"
    judul = "Lihat Detail Penginapan"

    konteks = {
        "title" : judul,
        "subtitle" : judul,
        "penginapan" : nginap,
    }

    return render(request, template, konteks)
