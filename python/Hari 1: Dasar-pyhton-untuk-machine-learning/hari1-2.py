def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang+lebar)
print(keliling_persegi_panjang(30,40))

angka = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
for i in range(len(angka)): # tidak pakai for i in angka karena menghasil error "list index out of range"
    if angka[i] % 3 == 0:
        print(angka[i])

produk = {"nama": "Sabun", "harga": 3000, "stok": 4}
print(f"Nama produk: {produk['nama']}\nHarga: {produk['harga']}\nStok tersedia: {produk['stok']}")