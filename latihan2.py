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
