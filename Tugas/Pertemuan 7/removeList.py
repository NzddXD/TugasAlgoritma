# Elemen utama
items = [
    "Shackle",
    "Tally Counter",
    "Fast Clock",
    "Blindfold",
    "Band of Regeneration",
    "Ancient Chisel",
    "Feral Claws",
    "Ancient Chisel"
]

selectedItem = "Ancient Chisel"
items.remove(selectedItem)

while selectedItem in items:
    items.remove(selectedItem)
print(items)