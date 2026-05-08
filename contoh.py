''' sitem pengkasiran '''

pelanggan = 1

while pelanggan < 2:
  print(f'Pelanggan ke-{pelanggan}')
  total = 0

while True:
  harga = int(input("masukkan harga barang : "))
  if harga == 0:
    break
  total += harga
print("total : ", total)
pelanggan += 1
