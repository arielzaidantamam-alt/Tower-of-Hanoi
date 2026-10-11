
def tower_of_hanoi(n, asal, bantuan, tujuan):
    # Kondisi dasar: hanya ada satu cakram
    if n == 1:
        print(f"Pindahkan cakram dari {asal} ke {tujuan}")
        return

    # Pindahkan n-1 cakram ke tiang bantuan
    tower_of_hanoi(n - 1, asal, tujuan, bantuan)

    # Pindahkan cakram terbesar ke tiang tujuan
    print(f"Pindahkan cakram dari {asal} ke {tujuan}")

    # Pindahkan n-1 cakram dari tiang bantuan ke tujuan
    tower_of_hanoi(n - 1, bantuan, asal, tujuan)


# Program utama
jumlah_cakram = 3

print("Solusi Tower of Hanoi:")
tower_of_hanoi(jumlah_cakram, "A", "B", "C")
