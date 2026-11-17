import time

text = 'hi, this is a cringe text. Pls kill me.'
delayTime: float = 0.07

# Dictionary
delayType = {
    ",": 0.3,
    ".": 0.9
}

for char in text:
    delayTime = delayType.get(char, 0.07)

    print(char, end='', flush=True)
    time.sleep(delayTime)