from django.contrib import admin

# Register your models here.
from .models import Barang,customer,Detailtrans,Jenis,produk

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrng','nama_barang','stok','harga','link_gbr','jenis_id']
    search_fields=['kodebrng','nama_barang','harga']
    list_filter=('jenis_id',)
    list_per_page=4

class kolomCustomer(admin.ModelAdmin):
    list_display = ['nomor', 'nama', 'nama_barang','jumlah']
    search_fields = ['nomor', 'nama']
    list_filter = ('jumlah',)
    list_per_page = 3

class kolomProduk(admin.ModelAdmin):
    list_display = ['kode_produk', 'nama', 'tempat', 'berat', 'jumlah']
    search_fields = ['kode_produk', 'nama']
    list_filter = ('jumlah',)
    list_per_page = 3

admin.site.register(Barang,kolomBarang)
admin.site.register(Detailtrans)
admin.site.register(Jenis)
admin.site.register(customer, kolomCustomer)
admin.site.register(produk, kolomProduk)