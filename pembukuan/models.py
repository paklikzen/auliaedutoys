from __future__ import unicode_literals

from django.db import models
from datetime import date

class Suplier(models.Model):
    namaSuplier = models.CharField(max_length=255, null=True)
    alamat = models.CharField(max_length=255, null=True)
    CP = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "Suplier"
 
    def __unicode__(self):
        return self.namaSuplier

class NoTelepon(models.Model):
    Telp = models.CharField(max_length=255, null=True)
    Suplier=models.ForeignKey(Suplier,related_name='NoTelpSuplier')
    class Meta:
        verbose_name_plural = "NoTelepon"
 
    def __unicode__(self):
        return self.Telp

class NoRekening(models.Model):
    Bank = models.CharField(max_length=255, null=True)
    NoRekBank = models.CharField(max_length=25, null=True)
    AtasNama = models.CharField(max_length=255, null=True)
    Suplier=models.ForeignKey(Suplier,related_name='NoRekSuplier')
    class Meta:
        verbose_name_plural = "NoRekening"
 
    def __unicode__(self):
        return self.Bank

class IDBarang(models.Model):
    NamaBarang = models.CharField(max_length=255, null=True)
    Suplier = models.ForeignKey(Suplier)
    Harga = models.IntegerField()
    Diskon = models.IntegerField()
    Ongkir = models.IntegerField()
    HargaJual = models.IntegerField()
    class Meta:
        verbose_name_plural = "IDBarang"
 
    def __unicode__(self):
        return self.NamaBarang

    @property
    def rp_diskon(self):
        RPSD= self.Harga
        ProsenDiskon= self.Diskon
        Rabat=RPSD*ProsenDiskon/100
        return Rabat

    @property
    def Rp_Stl_Disc(self):
        RPSD= self.Harga
        RpDiskon= self.rp_diskon
        RpStlRabat=RPSD-RpDiskon
        return RpStlRabat

    @property
    def Modalku(self):
        RpOngkir= self.Ongkir
        ModalItem= self.Rp_Stl_Disc
        RpModalku=RpOngkir+ModalItem
        return RpModalku

class PembelianBarang(models.Model):
    NamaBarang = models.ForeignKey(IDBarang)
    TanggalFaktur=models.DateField(default=date.today())
    Jumlah=models.IntegerField()
    Harga = models.IntegerField()
    Diskon = models.IntegerField()
    Ongkir = models.IntegerField()
    class Meta:
        verbose_name_plural = "NamaBarang"
 
    def __unicode__(self):
        return self.NamaBarang.NamaBarang

# Create your models here.
