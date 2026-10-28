# Contoh pola angka berurutan.

def polaAngkaBerurutan(min, max):
    if min == None or min == 0:
        min = 1

    if max == None or max <= min:
        max = min + 1

    for i in range(min, max):
        for j in range(min, i + 1):
            print(j, end=' ')
        print()

polaAngkaBerurutan(1, 6)
