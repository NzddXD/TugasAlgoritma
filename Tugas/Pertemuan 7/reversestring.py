# Main input
userInput: str

while True:
    try:
        userInput = str(input("Masukkan teks acak: "))
        break
    except ValueError:
        print("Masukkan teks yang valid!")

reversedString = userInput[::-1]
print(f'Output: {reversedString}')
