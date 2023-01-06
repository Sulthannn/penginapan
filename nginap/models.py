from django.db import models

# Create your models here.

class Jenis(models.Model):
    jenis = models.CharField(max_length=50)

    def __str__(self):
        return self.jenis


class Penginapan(models.Model):
    koordinat = models.CharField(max_length=100)
    nama = models.CharField(max_length=50)
    harga = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=250)
    tersisa = models.IntegerField(null=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)
    foto = models.ImageField(upload_to='foto/', null=True)

    def __str__(self):
        return self.nama
