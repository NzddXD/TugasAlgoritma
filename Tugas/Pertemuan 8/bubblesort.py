# Bubble Sort

# Compare dua element berurutan
# Tukar jika urutan salah
# Ulangi

# Tiap iterasi -> elemen terbesar 'bubbles' ke akhir

# Contoh

# Data
num = [10, 74, 92, 42, 37, 81]

# Nested loop
for index in range(len(num) - 1):
    for j in range(len(num) - index - 1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

print('Result: ', num)