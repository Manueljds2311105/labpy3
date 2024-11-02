# Tugas Praktikum 3
Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.,

Mata Kuliah: Bahasa Pemograman
## latihan1
```python
from random import random

n = int(input("Masukkan nilai N: "))

for i in range(n):
    a = random()
    # Ulangi pengacakan jika nilai a >= 0.5
    while a >= 0.5:
        a = random()
    print(f"data ke: {i+1} => {a}")

print("Selesai")
```
## Hasil Program
![foto](https://github.com/Manueljds2311105/foto/blob/b670933c24f480c41fe0843b63962d6b463e67f9/latihan1.png)
Penjelasan:
```python
from random import random
```
Baris ini mengimpor fungsi random() dari modul random. Fungsi ini digunakan untuk menghasilkan nilai acak berupa angka desimal antara 0 dan 1.
```python
n = int(input("Masukkan nilai N: "))
```
Di sini, program meminta untuk memasukkan nilai 'N', yang kemudian diubah menjadi tipe data integer. Nilai ini menentukan berapa banyak angka acak yang akan dihasilkan.
```python
for i in range(n):
```
Baris ini memulai loop for yang akan berulang sebanyak n kali. Variabel i di sini berfungsi sebagai penghitung iterasi (mulai dari 0 hingga n-1).
```python
a = random()
```
Di dalam loop, nilai acak antara 0 dan 1 dihasilkan oleh fungsi random() dan disimpan dalam variabel a
```python
while a >= 0.5:
    a = random()
```
Jika nilai a yang dihasilkan lebih besar atau sama dengan 0.5, program akan terus menghasilkan angka acak baru sampai mendapatkan angka yang kurang dari 0.5. Ini dilakukan dengan menggunakan loop while.
```python
print(f"data ke: {i+1} => {a}")
```
Setelah diperoleh nilai a yang kurang dari 0.5, program akan mencetak hasilnya. i+1 menunjukkan nomor data, dan {a} menampilkan nilai acak tersebut.
```python
print("Selesai")
```
Setelah semua iterasi selesai, program mencetak "Selesai" sebagai tanda bahwa proses telah berakhir.
## latihan2
```python
modal = 100000000
total_keuntungan = 0 

for bulan in range (1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <= 4:
        laba = 0.01
    elif bulan <= 7:
        laba = 0.05
    else:
        laba = 0.03

    laba_bulan_ini = modal * laba
    total_keuntungan += laba_bulan_ini
    print(f"Bulan {bulan}: Laba = Rp {laba_bulan_ini:.0f} ")
print(f"\nTotal keuntungan selama 8 bulan adalah: Rp {total_keuntungan:.0f} ")
```
## Hasil Program
![foto](https://github.com/Manueljds2311105/foto/blob/71b789ae0bd785dd01dcd67b0857dff8bfb3c279/latihan2py.png)
Penjelasan:
```python
modal = 100000000
total_keuntungan = 0
```
modal awal diset sebesar Rp 100,000,000. total_keuntungan diinisialisasi ke 0, yang akan digunakan untuk menampung jumlah keuntungan total selama 8 bulan.
```python
for bulan in range(1, 9):
```
Perulangan for digunakan untuk menghitung laba setiap bulan, dari bulan ke-1 hingga bulan ke-8.
```python
if bulan <= 2:
    laba = 0
elif bulan <= 4:
    laba = 0.01
elif bulan <= 7:
    laba = 0.05
else:
    laba = 0.03
```
Berdasarkan bulan, tingkat laba yang digunakan berbeda-beda:
- Bulan 1-2: tidak ada laba (laba = 0).
- Bulan 3-4: laba 1% (laba = 0.01).
- Bulan 5-7: laba 5% (laba = 0.05).
- Bulan 8: laba 3% (laba = 0.03).
```python
laba_bulan_ini = modal * laba
```
Pada setiap bulan, laba dihitung dengan mengalikan modal dengan laba yang telah ditentukan . Nilai ini disimpan dalam variabel laba_bulan_ini.
```python
total_keuntungan += laba_bulan_ini
print(f"Bulan {bulan}: Laba = Rp {laba_bulan_ini:.0f}")
```
Laba bulanan (laba_bulan_ini) ditambahkan ke total_keuntungan. Kemudian, hasil laba bulan tersebut dicetak.
```python
print(f"\nTotal keuntungan selama 8 bulan adalah: Rp {total_keuntungan:.0f}")
```
Setelah perulangan selesai, total keuntungan selama 8 bulan ditampilkan.
## ATM Sederhana
```python
# Saldo awal pengguna
saldo = 1000000

while True:
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")
    
    pilihan = input("Pilih menu (1/2): ")
    if pilihan == "1":
            jumlah = int(input("Masukkan jumlah penarikan: Rp "))
            if jumlah > saldo:
                print("Saldo tidak cukup!")
            else:
                saldo -= jumlah
                print("Penarikan berhasil!")
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
```
## Hasil Program
![foto](https://github.com/Manueljds2311105/foto/blob/b670933c24f480c41fe0843b63962d6b463e67f9/latihan3atm.png)
Penjelasan:
```python
saldo = 1000000
```
Variabel saldo diset dengan nilai awal 1000000, yang berarti pengguna memiliki saldo awal sebesar Rp 1.000.000.
```python
while True:
```
while True adalah loop yang berjalan terus menerus hingga ada perintah break untuk menghentikannya. Loop ini menjaga agar program tetap berjalan sampai pengguna memilih untuk keluar.
```python
print("\nSaldo saat ini: Rp", saldo)
print("1. Tarik Uang")
print("2. Keluar")
```
Bagian ini mencetak saldo pengguna saat ini dan dua pilihan menu:
- Tarik Uang: Memilih opsi ini memungkinkan pengguna untuk menarik uang dari saldo.
- Keluar: Memilih opsi ini akan keluar dari program
```python
pilihan = input("Pilih menu (1/2): ")
```
Program meminta untuk memasukkan pilihan (1 atau 2).Input ini disimpan dalam variabel pilihan
```python
if pilihan == "1":
    jumlah = int(input("Masukkan jumlah penarikan: Rp "))
    if jumlah > saldo:
        print("Saldo tidak cukup!")
    else:
        saldo -= jumlah
        print("Penarikan berhasil!")
```
Jika memilih 1 (tarik uang), maka:

kita diminta untuk memasukkan jumlah uang yang ingin ditarik.

- Jika jumlah yang dimasukkan lebih besar dari saldo, maka akan muncul pesan "Saldo tidak cukup!" karena saldo tidak cukup untuk transaksi tersebut.
- Jika jumlah yang dimasukkan kurang dari atau sama dengan saldo, maka saldo akan dikurangi sebesar jumlah penarikan dan pesan "Penarikan berhasil!" akan ditampilkan.
```python
elif pilihan == "2":
    print("Terima kasih telah menggunakan ATM!")
    break
```
Jika memilih 2, pesan "Terima kasih telah menggunakan ATM!" akan ditampilkan, dan perintah break digunakan untuk keluar dari while loop, mengakhiri program.
