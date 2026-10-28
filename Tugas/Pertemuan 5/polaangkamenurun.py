# Mengontrol jumlah baris yang akan dicetak.
for i in range(5, 0, -1):

    # Nested loop yang selalu mencetak dari angka 1 hingga
    # batas nilai i.
    for j in range(1, i + 1):

        # Cetak output.
        print(j, end='')
    print()