n = input("Masukkan bilangan : ")

if int(n) <= 0:
    pangkat = int(n)
else:
    pangkat = len(n)

hasil = 1
for i in range(pangkat):
    hasil *= 10

print(hasil)