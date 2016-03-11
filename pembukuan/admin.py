from django.contrib import admin
from django.contrib import admin
from pembukuan.models import Suplier
from pembukuan.models import IDBarang
from pembukuan.models import NoTelepon
from pembukuan.models import NoRekening

class SuplierAdmin(admin.ModelAdmin):
    list_display=('namaSuplier', 'alamat', 'CP')
    
class IDBarangAdmin(admin.ModelAdmin):
    list_display=('NamaBarang','Suplier','Harga','Diskon','DiskonRp','HargaDiskon','Ongkir','Modal','HargaJual')

   

# Register your models here.
admin.site.register(Suplier, SuplierAdmin)
admin.site.register(IDBarang, IDBarangAdmin)
admin.site.register(NoTelepon)
admin.site.register(NoRekening)
