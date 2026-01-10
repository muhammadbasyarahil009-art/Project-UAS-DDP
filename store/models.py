from django.db import models

# ---  MODEL BARANG (MATERIAL) ---
class Material(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nama Barang")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    price = models.IntegerField(verbose_name="Harga (Rp)")
    stock = models.IntegerField(verbose_name="Stok")
    unit = models.CharField(max_length=50, verbose_name="Satuan (Sak/Pcs/M3)")
    # Kolom Gambar
    image = models.ImageField(upload_to='materials/', null=True, blank=True, verbose_name="Foto Barang")

    def __str__(self):
        return self.name

# ---  MODEL KARYAWAN (EMPLOYEE/SALARY) ---
class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama Karyawan")
    division = models.CharField(max_length=100, verbose_name="Divisi")
    salary = models.IntegerField(verbose_name="Gaji (Salary)") 

    def __str__(self):
        return self.name