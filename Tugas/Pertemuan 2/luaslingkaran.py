# Variable
pi: float = 3.14159

# function untuk menghitung luas lingkaran
def hitungLuas(radius):
    if radius <= 0:
        radius = 0
    return pi * (radius * radius)

# hanya menerima bilangan desimal saat mode input.
jari = float(input("Jari - jari: "))
print("\nLuas: ", hitungLuas(jari))