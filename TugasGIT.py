import random

angka_rahasia = random.randint(1, 10)
kesempatan = 3

print("=== Game Tebak Angka ===")
print("Saya sudah memilih angka antara 1 sampai 10.")
print("Kamu punya 3 kesempatan untuk menebak!\n")

for i in range(kesempatan):
    tebakan = int(input(f"Tebakan ke-{i+1}: "))

    if tebakan == angka_rahasia:
        print("CONGRATS!! Tebakanmu benar!:)")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil. Coba angka yang lebih gede :|\n")
    else:
        print("Terlalu gede. Coba angka yang lebih kecil :|\n")
else:
    print(f"Kesempatan kamu telah habis! Amgka yang benar adalah {angka_rahasia}")