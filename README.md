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
Penjelasan:

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
        laba = 0.02

    laba_bulan_ini = modal * laba
    total_keuntungan += laba_bulan_ini
    print(f"Bulan {bulan}: Laba = Rp {laba_bulan_ini:.0f} ")
print(f"\nTotal keuntungan selama 8 bulan adalah: Rp {total_keuntungan:.0f} ")
```
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
Penjelasan:
