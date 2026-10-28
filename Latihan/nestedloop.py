# Nested Loop: Perulangan di dalam perulangan. Digunakan untuk
#              Mencetak Pola.

# For di dalam For
def forinfor(outer, inner):
    for i in range(outer):
        for j in range(inner):
            print("hi")

# While di dalam While
def whileinwhile(outer, inner):
    i = 0
    while i < outer:
        j = 0
        while j < inner:
            print(i, j)
            j += 1
        i += 1

# Nested Loop
for i in range(5):
    for j in range(2):
        print(f'i = {i}, j = {j}')

