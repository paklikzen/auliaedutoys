from django.contrib import admin
from django.contrib import admin
from pembukuan.models import Suplier
from pembukuan.models import IDBarang
from pembukuan.models import NoTelepon
from pembukuan.models import NoRekening

class SuplierAdmin(admin.ModelAdmin):
    list_display=('namaSuplier', 'alamat', 'CP')
    
#class IDBarangAdmin(admin.ModelAdmin):
   # list_display=('NamaBarang','Suplier','Harga','Diskon','DiskonRp','HargaDiskon','Ongkir','Modal','HargaJual')
class IDBarangAdmin(admin.ModelAdmin):
    list_display=('NamaBarang','Suplier','Harga','Diskon', 'DiskonRupiah', 'RpSetelahDisc', 'Ongkir','Modal','HargaJual')

    def DiskonRupiah(self, obj):
        return "Rp "+str(obj.rp_diskon)
    DiskonRupiah.short_description='Diskon Rp'

    def RpSetelahDisc(self, obj):
        return str(obj.Rp_Stl_Disc)
    RpSetelahDisc.short_description='Harga Setelah Diskon'


#
#
#    def DiskonRp2(self, obj):
#        RPSD= obj.Harga
#        ProsenDiskon= obj.Diskon
#        Rabat=RPSD*ProsenDiskon/100
#        return(Rabat)
#    DiskonRp2.short_description='Diskon Rp'
   
#    def RpSetelahDisc(self, obj):
#        RPSD= obj.Harga
#        RpDiskon= self.DiskonRp2(obj)
#        RpStlRabat=RPSD-RpDiskon
#        return(RpStlRabat)
#    RpSetelahDisc.short_description='Harga Setelah Diskon'
   

# Register your models here.
admin.site.register(Suplier, SuplierAdmin)
admin.site.register(IDBarang, IDBarangAdmin)
admin.site.register(NoTelepon)
admin.site.register(NoRekening)
