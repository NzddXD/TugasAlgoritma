# Variabel untuk banyaknya barisan
baris = 5

# Loop sebanyak banyaknya baris, hanya sekali untuk tiap
# barisan.
for i in range(1, baris + 1):

    # Inner loop memberikan spasi sebanyak 'i - 1'
    for j in range(1, i):

        # parameter 'end=' digunakan untuk menentukan apa yang akan di
        # outputkan pada akhiran 'print()'. Secara default, 'end=' akan
        # menggunakan '\n' sehingga akan otomatis mencetak dengan baris
        # baru tiap perintah 'print()'
        print(" ", end="")

    # Inner loop kedua, memerikan output sebanyak '2 * (baris - i) + 2' bintang
    for j in range(1, 2 * (baris - i) + 2):
        print("*", end="")

    # Buat baris baru
    print()