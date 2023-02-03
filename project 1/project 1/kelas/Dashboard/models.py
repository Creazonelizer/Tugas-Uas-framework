from unittest.util import _MAX_LENGTH
from django.db import models

class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def  __str__(self):
        return self.nama


# Create your models here.
class Barang(models.Model):
    kodebrng=models.CharField(max_length=8)
    nama_barang=models.CharField(max_length=50)
    stok=models.IntegerField()
    harga=models.BigIntegerField()
    link_gbr=models.CharField(max_length=150, blank=True)
    jenis_id=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return "{}. {}. {}. {}".format(self.kodebrng,self.nama_barang,self.harga,self.stok)

class customer(models.Model):
    nomor = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    nama_barang = models.CharField(max_length=120)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.nama


class Detailtrans(models.Model):
    kodetrans=models.CharField(max_length=10)
    kodebrng=models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()
    
    def __str__(self):
        return "{}. {}".format(self.kodetrans,self.kodebrng)

class produk(models.Model):
    kode_produk = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    tempat = models.CharField(max_length=120)
    berat = models.CharField(max_length=10)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.nama