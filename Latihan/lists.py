# Sequence: tipe data yang berisi elemen berururtan
# Mutable: Dapat diubah
# Immutable: Tidak dapat diubah

# List (Mutable):
mutableList: list = [24, 47, 128, 56, 93]
immutableList: list = ["Kai", "Makena", "Farah", "Dempsey", "Jard"]

# Cara akses elemen
pertama = mutableList[0] # Indeks pertama (dimulai dari 0)
terakhir = mutableList[-1] # Indeks terakhri

# Slicing: mengakses elemen dengan range tertentu
sliced = mutableList[0 : 2]

# Len: Mengambil seberapa panjang list tersebut
length = len(mutableList)

# METHODS
# .append(value): menambahkan elemen baru di paling akhir
mutableList.append([91, 48, 37])

# .insert(index, value): menyisipkan data baru ke indeks yang ditentukan
mutableList.insert(0, 412)

# .remove(value): menghapus elemen yang match pertama dengan nilai yang ditentukan
mutableList.remove(93)

# .pop(index): menghapus elemen dengan indeks yang diberikan
mutableList.pop(3)

# .sort(): mengurutkan sebuah list
mutableList.sort()

# .reverse(): membalikkan sebuah list
mutableList.reverse()

