from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from Dashboard.views import  *

def coba1(request):
    return HttpResponse('Welcome')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel' : titelnya,
    }
    return render(request,'index.html',konteks)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',coba2), 
    path('addbrg/',Barang_add),
    path('Vbrg/',Barang_View,name='Vbrg'),
    path('customer/',Customer),
    path('produk1/',Produk),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),

]
