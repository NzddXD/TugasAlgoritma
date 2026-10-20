# Variabel konstan untuk base biaya parkir
# BIAYA_PARKIR : float = 5000

# Array daftar biaya parkir sesuai jam
biayaParkir = [
    5000,
    10000,
    15000,
]

# fungsi untuk kalkulasi biaya parkir
# def hitungBiayaParkir(durasiParkir: float):
#     return durasiParkir * BIAYA_PARKIR

# menjalankan kode loop untuk mengecek apakah user hanya memasukkan tipe
# bilangan bulat saja.

# Mengapa dibungkus di dalam loop? Karena python memperlakukan 'input()'
# sebagai string. Hasilnya bagian perbandingan nilai di dalam kode blok
# logic gate akan error duluan sebelum user dapat meng-input nilai.
while True:
    try:
        durasi = int(input("Masukkan durasi parkir dalam jam: "))
        # print("Jumlah bayar: Rp.", f"{hitungBiayaParkir(durasi):,}")
        print("Anda parkir selama: ", durasi, "jam.")
        break

    except TypeError:
        print("Masukkan jumlah durasi yang valid.")

# fungsi 'f' digunakan untuk mem-format output. Contohnya
# menggunakan ',' untuk mem-format nilai menjadi bentuk ribuan (6000 -> 6,000)
# Cara penggunaan -> (input:format) 
if durasi <= 2:
    print("Biaya parkir: Rp.", f"{biayaParkir[0]:,}")
elif durasi > 2 and durasi < 5:
    print("Biaya parkir: Rp.", f"{biayaParkir[1]:,}")
elif durasi > 5:
    print("Biaya parkir: Rp.", f"{biayaParkir[2]:,}")