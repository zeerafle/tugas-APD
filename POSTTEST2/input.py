print("Survey !")
while True:
    sattu = input("Pilih satuan berikut untuk berapa lama waktu ideal belajar\njam/menit/detik\n--> ")
    if sattu == "jam" or sattu == "menit" or sattu == "detik":
        break
    else:
        continue

waktu = input("Berapa waktu ideal untuk belajar? (angka saja)\n--> ")

while True:
    hari = input("Menurutmu gaji yang tepat diberi setiap...\nhari/bulan/tahun\n--> ")
    if hari == "hari" or hari == "bulan" or hari == "tahun":
        break
    else:
        continue

while True:
    makan = input("Berapa kali rata-rata kamu makan dalam sehari?\n--> ")
    try:
        int(makan)
        break
    except:
        continue

gigi = input("Setelah mandi apa yang kamu lakukan?\n--> ")

while True:
    sukan = input("Pada meeting online terakhir, apakah kamu sudah makan?\nsudah/belum\n--> ")
    if sukan == "sudah" or sukan == "belum":
        break
    else:
        continue

while True:
    bau = input("Bagaimana selokan dirumahmu?\nbau/sangat bau/lumayan bau\n--> ")
    if bau == "bau" or bau == "sangat bau" or bau == "lumayan bau":
        break
    else:
        continue

gans = input("Menurutmu, siapa makhluk paling ganteng?\n--> ")

lst = [sattu, waktu, hari, makan, gigi, sukan, bau, gans]
print("terima kasih, berikut adalah hasil yang kamu input")
print(lst)
print()
lst.reverse()
lst.insert(2, "karena")
print("="*30)
print()
print("Sekarang baca kalimat dibawah!")
print(" ".join(lst))