# 🎈 Copeland Score Calculator

**Nama:** Furqan  
**NIM:** 24/546979/PPA/06867

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://copeland-score.streamlit.app/)

Aplikasi ini digunakan untuk menghitung skor **Copeland** dalam pengambilan keputusan multi-kriteria. Pengguna dapat memasukkan sejumlah kriteria dan bobotnya, kemudian memberikan penilaian pada tiap alternatif berdasarkan kriteria tersebut. Hasil akhirnya berupa peringkat alternatif berdasarkan metode perbandingan pasangan (pairwise) Copeland.

---

## ✨ Fitur

- Menentukan daftar **kriteria** dan **bobot (%)**
- Menambahkan **alternatif** yang akan dibandingkan
- Memasukkan **nilai/skor** tiap alternatif pada setiap kriteria
- Menghitung dan menampilkan **Skor Copeland** secara otomatis
- Menampilkan hasil akhir dalam bentuk tabel peringkat

---

## 📦 Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/username/copeland-score-app.git
```

### 2. Masuk ke Direktori Aplikasi
```bash
cd copeland-score-app
```

### 3. Install Dependensi
Pastikan Python dan pip telah terpasang, lalu jalankan:
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run streamlit_app.py
```

> Ganti `streamlit_app.py` jika nama file berbeda.

---

## 🛠️ Cara Penggunaan

1. **Masukkan Kriteria dan Bobotnya**
   - Tulis kriteria (satu per baris).
   - Tentukan bobot tiap kriteria (dalam persen).
   - Total bobot harus = 100%.

2. **Masukkan Alternatif**
   - Tulis nama alternatif (satu per baris).
   - Minimal 2 alternatif diperlukan.

3. **Masukkan Skor Alternatif**
   - Masukkan nilai (0–100) untuk setiap alternatif pada masing-masing kriteria.

4. **Hitung Skor Copeland**
   - Klik tombol **"Calculate Copeland Score"**.
   - Hasil akhir ditampilkan dalam bentuk tabel peringkat.

---

## 🧪 Contoh Penggunaan

Misal:

- **Kriteria:** Biaya, Kualitas, Daya Tahan  
- **Bobot:** 40%, 30%, 30%
- **Alternatif:** A, B, C

| Alternatif | Biaya | Kualitas | Daya Tahan |
|------------|-------|----------|------------|
| A          | 80    | 70       | 90         |
| B          | 60    | 85       | 80         |
| C          | 75    | 80       | 85         |

Aplikasi akan melakukan perbandingan semua pasangan alternatif dan menghitung skor Copeland untuk menentukan peringkat akhir.

---

## 📄 Lisensi

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE). Bebas digunakan dan dimodifikasi.

---

## 🤝 Kontribusi

Pull request dan issue sangat terbuka bagi siapa saja yang ingin berkontribusi dalam proyek ini.

---

Dibuat dengan ❤️ menggunakan [Streamlit](https://streamlit.io/)
```
