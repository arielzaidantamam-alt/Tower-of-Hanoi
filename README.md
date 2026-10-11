Tower of Hanoi

Deskripsi

Tower of Hanoi adalah permainan logika yang bertujuan memindahkan semua cakram dari tiang asal ke tiang tujuan menggunakan satu tiang tambahan.

Tujuan Program

Program ini dibuat untuk menerapkan algoritma rekursif dalam menyelesaikan teka-teki Tower of Hanoi dengan tiga cakram.

Aturan Permainan

1. Hanya satu cakram yang boleh dipindahkan dalam satu langkah.
2. Cakram yang lebih besar tidak boleh diletakkan di atas cakram yang lebih kecil.
3. Tiang bantuan boleh digunakan selama proses pemindahan.

Algoritma

Program menggunakan rekursi untuk menyelesaikan permainan:

1. Pindahkan cakram sebanyak n-1 dari tiang asal ke tiang bantuan.
2. Pindahkan cakram terbesar yang tersisa ke tiang tujuan.
3. Pindahkan cakram dari tiang bantuan ke tiang tujuan.

Hasil

Untuk tiga cakram, program menghasilkan tujuh langkah pemindahan. Jumlah langkah minimum dihitung menggunakan rumus:

T(n) = 2^n - 1

Kesimpulan

Algoritma Tower of Hanoi menunjukkan penerapan rekursi, urutan instruksi, dan pemecahan masalah. Konsep ini dapat digunakan dalam Game Development untuk membangun logika teka-teki dan mekanisme permainan.
