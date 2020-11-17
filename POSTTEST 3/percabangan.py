# harga varian
ty1_price = 2000
ty2_price = 2500

# welcome screen
print("Selamat datang di Toko-yaki!")
print("Daftar Harga:")
print("1. Varian 1 = Rp", str(ty1_price) + "/pcs")
print("2. Varian 2 = Rp", str(ty2_price) + "/pcs")
print("""Promo!:
Beli Varian 1 sebanyak 10 pcs atau lebih kamu dapat diskon 10%
Beli Varian 2 sebanyak 8 pcs atau lebih kamu dapat diskon 8%
""")

# beli
# pastikan cuma pilih 1 atau 2
while True:
    pick = input("Pilih yang mana : ")
    if int(pick) > 2 or int(pick) < 1:
        print("Maaf, varian lain belum tersedia")
        continue
    else:
        break

how_much = int(input("Mau beli berapa : "))
print("=" * 30)

# harga total
if pick == "1":
    print("Kamu membeli Varian 1 sebanyak", how_much, "pcs")
    total = ty1_price * how_much
    if how_much >= 10:
        # diskon 10% = 90% harga asli
        total *= 0.9
elif pick == "2":
    print("Kamu membeli Varian 2 sebanyak", how_much, "pcs")
    total = ty2_price * how_much
    if how_much >= 8:
        # diskon 8% = 92% harga asli
        total *= 0.92

print("Harga totalnya adalah", "Rp", round(total))