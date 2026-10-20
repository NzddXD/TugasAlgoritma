hari: str = "Selasa"

match hari:
    case "Senin":
        print("Sekarang hari: ", hari)
    case "Selasa":
        print("Selasa")
    case "Sabtu" | "Minggu":
        print("Sekarang libur")
    case _:
        print("Hari biasa")