# 🎈 Copeland Score Calculator

**Nama:** Furqan\
**NIM:** 24/546979/PPA/06867

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://copeland-score.streamlit.app/)

Aplikasi ini digunakan untuk menghitung skor Copeland dalam pengambilan keputusan multi-kriteria dengan mempertimbangkan kriteria, bobot, dan perbandingan pasangan alternatif.

## Fitur
- Menentukan kriteria dan bobot dalam persen (%).
- Menentukan alternatif yang akan dibandingkan.
- Memasukkan nilai alternatif berdasarkan kriteria.
- Menghitung skor Copeland secara otomatis.
- Menampilkan hasil peringkat berdasarkan skor Copeland.

## Instalasi

### 1. Clone Repository
```sh
git clone https://github.com/username/copeland-score-app.git
```

### 2. Masuk ke Direktori Aplikasi
```sh
cd copeland-score-app
```

### 3. Install Dependensi
Pastikan Anda memiliki Python dan pip terinstall, lalu jalankan perintah berikut:
```sh
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
Gunakan perintah berikut untuk menjalankan aplikasi dengan Streamlit:
```sh
streamlit run app.py
```

## Cara Penggunaan

1. **Masukkan Kriteria dan Bobotnya**
   - Tuliskan kriteria yang digunakan untuk menilai alternatif, satu per baris.
   - Tentukan bobot masing-masing kriteria dalam persen (%).
   - Pastikan total bobot kriteria berjumlah 100%.

2. **Masukkan Alternatif**
   - Tuliskan alternatif yang akan dibandingkan, satu per baris.
   - Minimal harus ada dua alternatif.

3. **Masukkan Nilai Alternatif**
   - Berikan skor untuk setiap alternatif berdasarkan setiap kriteria.
   - Skor berkisar dari 0 hingga 100.

4. **Hitung Skor Copeland**
   - Klik tombol "Hitung Skor Copeland" untuk memulai perhitungan.
   - Hasil akan ditampilkan dalam bentuk tabel dengan peringkat alternatif berdasarkan skor Copeland.

## Contoh Penggunaan
Jika memiliki 3 alternatif: **A, B, C** dan 3 kriteria: **Biaya, Kualitas, Daya Tahan** dengan bobot masing-masing **40%, 30%, 30%**, Anda dapat memasukkan nilai alternatif seperti berikut:

| Alternatif | Biaya | Kualitas | Daya Tahan |
|------------|-------|----------|------------|
| A          | 80    | 70       | 90         |
| B          | 60    | 85       | 80         |
| C          | 75    | 80       | 85         |

Aplikasi akan secara otomatis melakukan pairwise contest dan menampilkan hasil peringkat alternatif berdasarkan metode Copeland.

## Lisensi
Aplikasi ini menggunakan lisensi MIT. Silakan gunakan dan modifikasi sesuai kebutuhan Anda.

## Kontribusi
Jika Anda ingin berkontribusi dalam proyek ini, silakan buat pull request atau ajukan issue.

---
Dibuat dengan ❤️ menggunakan Streamlit.
