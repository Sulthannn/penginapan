from django.forms import ModelForm
from django import forms 
from nginap.models import * 
from .models import *

class FormPenginapan(ModelForm):
    class Meta:
        model = Penginapan
        fields = '__all__'

        widgets = {
                'koordinat' : forms.TextInput({'class':'form-control','placeholder':'koordinat','required':'required'}),
                'nama' : forms.TextInput({'class': 'form-control', 'placeholder':'Nama Penginapan', 'required':'required'}),
                'harga' : forms.TextInput({'class': 'form-control', 'placeholder':'Harga Penginapan', 'required':'required'}),
                'lokasi' : forms.TextInput({'class': 'form-control', 'placeholder':'Lokasi Penginapan', 'required':'required'}),
                'tersisa' : forms.NumberInput({'class': 'form-control', 'placeholder':'Tersisa Kamar Kosong', 'required':'required'}),
                'jenis_id' : forms.Select({'class': 'form-control', 'placeholder':'Jenis Penginapan', 'required':'required'})
            }