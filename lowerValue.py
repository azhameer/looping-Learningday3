for i in range(1, 11):
    angka = float(input(f"Masukkan angka ke-{i}: "))

    if terkecil is None or angka < terkecil:
        terkecil = angka

print(f"\nBilangan terkecil yang Anda masukkan adalah: {terkecil}")
