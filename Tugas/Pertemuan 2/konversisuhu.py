# Variable
nama: str = "nez"
angka: int = 1
desimal: float = 9.31
truth: bool = False

# fungsi untuk konversi nilai ke Fahrenheit
def fahrenheit(n):
    return (n - 32) * 5 / 9

# fungsi untuk konversi nilai ke Celsius
def celsius(n):
    return (n * 9 / 5) + 32

print(fahrenheit(0))