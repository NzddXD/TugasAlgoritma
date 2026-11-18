# Classes
from cls.Output import Output
from cls.Colorizer import Colorizer
import random
import time
import sys

# Vars
color = Colorizer('RESET', '')
out = Output('Default')

# Gunakan Token untuk batas roll?
useToken = True

# Total kali roll
timesRolled = 0

# print(color.colorize('green', 'verity'))

# Item Pool List
itemPools = {
    "Common": ['Shackle', 'Tatered Cloth', 'Acorn', 'Gel'],
    "Rare": ['Deathweed', 'Diamond Hook', 'Guide Voodo Doll'],
    "Epic": ['Fast Clock', 'Nimble Platinum Axe', 'Blindfold'],
    "Legendary": ["Dual Hook", "Hallow Bars", "Roaring Insignia"],
    "Mythic": ['Zenith', 'Meowmere', 'Terraspark Boots', 'Wisp in a Bottle', 'MBG']
}

# Maximum rarity requirement lists
rarityList = {
    'Mythic': 0.21,
    'Legendary': 1.21,
    'Epic': 11.16,
    'Rare': 42.44,
}

# 'Loading...' style
def rollingText(doneholder):

    # Init
    if not doneholder:
        doneholder = 'Done'

    rollingText = 'Rolling'
    duration = random.uniform(1.06, 2.27)
    interval = 0.38

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

# rollingText()


# Test phase
try:
    token = random.randrange(4, 9)

    input(color.colorize('green', 'Welcome to the Random Item Generator! Press Enter to Continue...'))
    while True:
        timesRolled += 1

        roll = random.uniform(0, 100.0)

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

            case _:
                rarity = 'Common'
                rarityColor = 'reset'

        item_name = random.choice(itemPools[rarity])
        rollingText(f'You got: {color.colorize(rarityColor, item_name)}\nRarity: {color.colorize(rarityColor, rarity)}\n')

        # Rolled: {roll:.2f



        if useToken == True:
            token -= 1
            input(f'Enter to continue rolling... (Remaining token: {token})\n')

            if token <= 0:
                out.warn('Ran out of token! Purchase additional 10 tokens for only $95.99!')
                # out.warn("Can't afford tokens? (y/n)")
                # decision = str(input()).strip().lower()

                # if decision == 'y':
                #     out.warn('Broke ahh mfs get a job lil chud.')
                # else:
                #     out.warn('Then why the hell do you want to spend your entire livesaving over a token.')
                # break
                break
        else:
            input('Enter to continue rolling...\n')

except KeyboardInterrupt:
    out.err(f'Rolling aborted! Total rolls: {timesRolled}')