from django.contrib import admin
from .models import Material

# Daftarkan model Material saja agar bisa dikelola admin
admin.site.register(Material)

# Catatan: 
# admin.site.register(Employee) <-- Baris ini sengaja dihapus/tidak ditulis
# tujuannya agar menu "Employees" HILANG dari halaman admin.