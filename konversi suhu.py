# inputan terus diminta
while True:
    cel = input("Masukkan suhu celcius ('00' untuk berhenti): ")
    if cel == "00":
        break
    
    # pastikan yang diinput user adalah angka
    try:
        intcel = int(cel)
    except:
        print("Mohon gunakan angka!")
        continue
    
    # tanya mau dikonversi ke apa
    while True:
        print(
            "Konversi ke?\nF : Farenheit       K : Kelvin      R : Reamur"
        )
        ask = input("--> ")
        if ask == "F" or ask == "f":
            print(intcel, "°C =", 9/5 * intcel, "°F")
            print("")
            break
        elif ask == "K" or ask == "k":
            print(intcel, "°C =", intcel + 273, "°K")
            print("")
            break
        elif ask == "R" or ask == "r":
            print(intcel, "°C =", 4/5 * intcel, "°R")
            print("")
            break
        else:
            print("Input tidak valid!\n")
            continue