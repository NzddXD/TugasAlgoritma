# meng-inisialisasi dan menyimpan nilai username dan
# password yang asli agar bisa disesuaikan secara mudah.
realUsername = "admin"
realPassword = "python"

# kita buat nilai maksimum untuk batas kali meng-input nilai
maxRetries = 3

# untuk menyimpan berapa kali user telah menginput.
retries = 0

# loop selama nilai 'retires' masih kurang dengan nilai 'maxRetries' 
while retries <= maxRetries:
    try:

        # penginputan nilai dari user.
        username = str(input("Username: "))
        password = str(input("Password: "))

        # buat logika jika username dan/atau passowd tidak sama dengan
        # aslinya.
        if username != realUsername or password != realPassword:

            # tambah 1 ke variabel 'retries' dan buat pesan salah.
            retries += 1
            print(f'Username atau Password salah!, {retries} kali percobaan.')

            # jika sudah melebihi limit percobaan, keluar dari loop dan exit dari
            # kode.
            if retries >= maxRetries:
                print("Jumlah percobaan telah mencapai maksimum! Tidak dapat login lagi.")
                break

        # jika username dan password benar, tampilkan pesan berhasil, keluar dari loop,
        # dan exit dari kode.
        else:
            print(f'Selamat datang, {username}!')
            break

    # jika pengguna menginput nilai selain string, tampilkan pesan error.
    # NOTE: mau apapun nilai yang dimasukkan jika ke dalam string, akan tetap sama
    # menjadi string, sehingga nilai apapun akan valid.
    except TypeError:
        print("Masukkan info yang valid!")
    