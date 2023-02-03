from django.shortcuts import render
from Dashboard.post_forms import FormBarangku
from Dashboard.models import Barang,customer,produk
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.



def Barang_View(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs,
    }
    return render(request,'tampil_brg.html',konteks)

# def Barang_Transaksi(request):
#     trans=Transaksi.objects.all()
#     konteks={
#         'trans':trans,
#     }
#     return render(request,'tampil_trans.html',konteks)

def tambah_barang(request):
    form=FormBarangku()
    konteks={
        'form':form,
    }
    return render(request,'tambah_barang.html',konteks)


def Customer(request):
    Customers=customer.objects.all()
    konteks={
        'Customers':Customers,
    }
    return render(request,'customer.html',konteks)


def Produk(request):
    Produks=produk.objects.all()
    konteks={
        'Produks':Produks,
    }
    return render(request,'produk1.html',konteks)

def Barang_add(request):
    if request.POST:
        form= FormBarangku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form = FormBarangku()
            konteks = {
                'form': form
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarangku()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)
    
def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarangku(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarangku(instance=barangs)
        konteks = {
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def hapus_brg(request,id_barang):
        barangs=Barang.objects.filter(id=id_barang)
        barangs.delete()
        messages.success(request,"Data Terhapus")
        return redirect('VBrg')
