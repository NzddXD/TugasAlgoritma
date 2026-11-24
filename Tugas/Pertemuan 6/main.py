# RANDOM ITEM GENERATOR
# Untuk Algoritma, bisa dilihat di dalam file 'algoritma.txt'
# Untuk Flowchart, bisa dilihat di 'Diagram.drawio.png'

# Import kelas kelas sebagai blueprint / module
from cls.Output import Output # Modul pewarnaan output berdasarkan jenis output (info, error, warning)
from cls.Colorizer import Colorizer # Modul pewarnaan teks menggunakan escape code ASCI

# Import modul sistem yang kruisial untuk mini-project ini
import random # Digunakan untuk mengakses library random dan untuk menggunakan fungsi random.uniform() 
import time # Digunakan untuk 
import sys

# Peng-inisialisasian kelas menggunakan variabel
color = Colorizer('RESET', '')
out = Output('Default')

# Gunakan Token untuk menambahkan fitur batas roll?
useToken = False

# Total kali roll
timesRolled = 0

# Item Pool List
itemPools = {
    "Common": ['Shackle', 'Tatered Cloth', 'Acorn', 'Gel'],
    "Rare": ['Deathweed', 'Diamond Hook', 'Guide Voodo Doll'],
    "Epic": ['Fast Clock', 'Nimble Platinum Axe', 'Blindfold'],
    "Legendary": ["Dual Hook", "Hallow Bars", "Roaring Insignia"],
    "Mythic": ['Zenith', 'Meowmere', 'Terraspark Boots', 'Wisp in a Bottle', 'MBG']
}

# List nilai Requirement rarity maksimum
rarityList = {
    'Mythic': 0.21,
    'Legendary': 1.21,
    'Epic': 11.16,
    'Rare': 42.44,
}

# List item apa saja yang telah di dapat
acquiredItems = {
    'Common': [],
    'Rare': [],
    'Epic': [],
    'Legendary': [],
    'Mythic': []
}

# Fungsi untuk membuat teks animasi 'Rolling...'
def rollingText(doneholder):

    # Initialisasi: jika teks setelah animasi selesai tidak ada, gunakan nilai default 'Done'
    if not doneholder:
        doneholder = 'Done'

    # Set teks '>> Rolling <<...'
    rollingText = 'Rolling'

    # Ambil durasi acak dari 0.31 - 1.67 detik
    duration = random.uniform(0.31, 1.67)

    # Interval animasi untuk titik titik di depan 'Rolling'
    interval = 0.38

    # Ambil snapshot waktu sekarang dan tambahkan 
    # dengan durasi untuk membuat waktu akhir.
    endTime = time.time() + duration
    dot_count = 0

    while time.time() < endTime:
        dots = "." * (dot_count % 4)

        # Pad with spaces to erase leftovers
        sys.stdout.write(f'\r{rollingText}{dots:<3}')
        sys.stdout.flush()

        dot_count += 1
        time.sleep(interval)

    sys.stdout.write(f'\r\033[K{doneholder}\n')
    sys.stdout.flush()

def showStats(data):
    if not data:
        out.err('Data not found/poorly passed.')

    out.success('Your items:')

    # Totals
    totalItems = len(data)

# While-loop digunakan untuk roll angka acak, mengambil tipe rarity, dan mengambil item
# acak secara berulang ulang

# Loop akan di selesaikan jika user menekan Ctrl + C di keyboard.
# Jika 'useToken' bernlai True, loop akan berjalan selama token belum mencapai atau kurang dari 0
try:

    # Ambil nilai token random untuk nanti kedepannya jika 'useToken' bernilai True
    token = random.randrange(4, 9)

    # Tampilkan teks awal sebelum memulai operasi rolling.
    # Lanjut ke step berikutnya jika user menekan Enter.
    input(color.colorize('green', 'Welcome to the Random Item Generator! Press Enter to Continue...'))

    while True:

        # Tambah 1 ke total roll, ini digunakan jika ingin mengetahui seberapa banyak rolling terjadi.
        timesRolled += 1

        # (CRITICAL) ambil nilai acak desimal (float) dari 0.0 - 100.0
        roll = random.uniform(0.0, 100.0)

        # Root Decision: yang menentukan apa item yang akan didapatkan berdasarkan
        # nilai roll user.
        match roll:
            case rollValue if rollValue <= rarityList['Mythic']:
                rarity = 'Mythic'
                rarityColor = 'red'

            case rollValue if rollValue <= rarityList['Legendary']:
                rarity = 'Legendary'
                rarityColor = 'yellow'

            case rollValue if rollValue <= rarityList['Epic']:
                rarity = 'Epic'
                rarityColor = 'magenta'

            case rollValue if rollValue <= rarityList['Rare']:
                rarity = 'Rare'
                rarityColor = 'blue'

            case _: # Default
                rarity = 'Common'
                rarityColor = 'reset'

        # Jika rarity telah di dapatkan, ambil item random di dalam kategori rarity tersebut.
        item_name = random.choice(itemPools[rarity])

        # Push data baru jika user sudah roll
        list.append(acquiredItems[rarity], item_name)

        rollingText(f'You got: {color.colorize(rarityColor, item_name)}\nRarity: {color.colorize(rarityColor, rarity)}\n')

        # Rolled: {roll:.2f

        # (Opsional) jika menggunakan token, kurangi token sebanyak 1 tiap roll.
        if useToken == True:
            token -= 1
            input(f'Enter to continue rolling... (Remaining token: {token})\n')

            # Jika token habis, beri warning token habis dan break loop
            if token <= 0:
                out.warn(f"Ran out of token! Total rolls: {timesRolled}")
                print(acquiredItems)
                break

        # Jika tidak menggunakan token:
        else:
            input('Enter to continue rolling...\n')

# Handle error Ctrl + C dengan pesan kustom yang telah dibuat
except KeyboardInterrupt:
    out.err(f'Rolling aborted! Total rolls: {timesRolled}')

    print(f'Your items:\n')
    
    print('Common: ')
    print(', '.join(acquiredItems['Common']))

    print(color.colorize('magenta', 'Epic:'))
    print(color.colorize('magenta', ', '.join(acquiredItems['Epic'])))

    print(color.colorize('yellow', 'Legendary:'))
    print(color.colorize('yellow', ', '.join(acquiredItems['Legendary'])))
    
    print(color.colorize('red', 'Mythic:'))
    print(color.colorize('red', ', '.join(acquiredItems['Mythic'])))