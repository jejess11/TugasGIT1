print("=== Program Penilaian Siswa ===")

nama = input("Masukkan nama siswa")
jumlah_mapel = int(input("Masukkan jumlah mata pelajaran"))
totat_nilai = 0

for i in range(jumlah_mapel):
    nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
    total_nilai += nilai

rata_rata = total_nilai / jumlah_mapel

if rata_rata >= 75:
    status = "LULUS!!"
else:
    status = "TIDAK LULUS:("

print("\n== Hasil Penilaian ===")
print(f"Nama Siswa      : {nama}")
print(f"Rata-rata Nilai : {rata_rata: .2f}")
print(f"Status          : {status}")