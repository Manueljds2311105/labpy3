# Tugas Praktikum 3

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
![foto](https://github.com/Manueljds2311105/foto/blob/b670933c24f480c41fe0843b63962d6b463e67f9/latihan2.png)
Penjelasan:

## ATM Sederhana
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
        laba = 0.02

    laba_bulan_ini = modal * laba
    total_keuntungan += laba_bulan_ini
    print(f"Bulan {bulan}: Laba = Rp {laba_bulan_ini:.0f} ")
print(f"\nTotal keuntungan selama 8 bulan adalah: Rp {total_keuntungan:.0f} ")
```
## Hasil Program
![foto](https://github.com/Manueljds2311105/foto/blob/b670933c24f480c41fe0843b63962d6b463e67f9/latihan3atm.png)
Penjelasan:
