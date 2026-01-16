from django.shortcuts import render, get_object_or_404
from .models import Material

# View untuk Halaman Utama (Dashboard)
def home(request):
    materials = Material.objects.all()
    
    # --- LOGIKA DASHBOARD ---
    total_material = materials.count()
    low_stock = materials.filter(stock__lt=10).count()
    total_asset = sum(item.price * item.stock for item in materials)

    context = {
        'materials': materials,
        'total_material': total_material,
        'low_stock': low_stock,
        'total_asset': total_asset,
    }
    
    # Kirim 'context' ke HTML
    return render(request, 'store/home.html', context)

# View untuk Halaman Detail Barang
def detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    return render(request, 'store/detail.html', {'material': material})


def about(request):
    return render(request, 'store/about.html')

def gallery(request):
    return render(request, 'store/gallery.html')

def employee(request):
    return render(request, 'store/employee.html')

def employee(request):
    context = {}

    if request.method == 'POST':
        # Ambil data dari form HTML
        nama = request.POST.get('nama')
        jabatan = request.POST.get('jabatan')
        agama = request.POST.get('agama')
        status = request.POST.get('status')

        # Tentukan Gaji Pokok berdasarkan Jabatan (Simulasi)
        gaji_pokok = 0
        if jabatan == 'Manager':
            gaji_pokok = 20000000
        elif jabatan == 'Asisten Manager':
            gaji_pokok = 15000000
        elif jabatan == 'Supervisor':
            gaji_pokok = 12000000
        elif jabatan == 'Staff Gudang':
            gaji_pokok = 8000000
        elif jabatan == 'Administrasi':
            gaji_pokok = 10000000
        elif jabatan == 'Kasir':
            gaji_pokok = 7500000
        
        # Hitung Tunjangan (Jika Menikah tambah 1 Juta)
        tunjangan = 0
        if status == 'Menikah':
            tunjangan = 1000000
        
        # Hitung Gaji Kotor
        gaji_kotor = gaji_pokok + tunjangan

        # Hitung Zakat (Jika Islam, potong 2.5%)
        zakat = 0
        if agama == 'Islam' and gaji_kotor >= 0:
            zakat = gaji_kotor * 0.025 # 2.5 persen
        
        # Hitung Gaji Bersih (Take Home Pay)
        gaji_bersih = gaji_kotor - zakat

        # Bungkus data untuk dikirim balik ke HTML
        context = {
            'hasil': True,
            'nama': nama,
            'jabatan': jabatan,
            'agama': agama,
            'status': status,
            'gaji_pokok': int(gaji_pokok),
            'tunjangan': int(tunjangan),
            'gaji_kotor': int(gaji_kotor),
            'zakat': int(zakat),
            'gaji_bersih': int(gaji_bersih)
        }

    return render(request, 'store/employee.html', context)