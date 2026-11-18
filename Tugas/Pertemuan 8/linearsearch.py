# Algoritma Linear Search

# Mulai dari elemen pertama >
# Banding elemen yang dicari>
#   (?) Jika cocok, selesai
#   (X) Jika tidak, lanjut
#   (X) Jika telah mencapai akhir list, tidak ditemukan

# Contoh

# List Data
debuffs = [
    "Blinded",
    "Bleeding",
    "Withered",
    "Slow",
    "Poison",
    "Venom Acid",
    "Creative Shock",
    "Impaled"
]

# User input prompt
finder_prompt = str(input("Cari: "))
found: bool = False

# print(finder_prompt)

# Loop keseluruh list
for debuff in range(len(debuffs)):

    # Jika ditemukan, berhenti loop dan exit
    if debuffs[debuff] == finder_prompt:
        print(f'Found {finder_prompt} at index: {debuff}')
        found = True
        break

    # Jika belum ditemukan, lanjut sampai akhir list
    if not found:
        print('Debuff not found.')