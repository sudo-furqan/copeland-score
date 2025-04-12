# 🎯 Copeland Score Calculator

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://copeland-score.streamlit.app/)

**Author:** Furqan — 24/546979/PPA/06867

Selamat datang di **Copeland Score Calculator** – sebuah aplikasi berbasis Streamlit yang dirancang untuk membantu pengambilan keputusan multi-kriteria menggunakan metode **pairwise Copeland**.

Pengguna dapat menentukan kriteria beserta bobotnya, menambahkan alternatif, lalu memberikan skor berdasarkan kriteria tersebut. Hasil akhir ditampilkan dalam bentuk peringkat alternatif.

---

## ✨ Fitur Unggulan

✅ Input **kriteria** beserta bobot dalam persen  
✅ Tambahkan berbagai **alternatif** untuk dibandingkan  
✅ Berikan **nilai/skor** untuk setiap alternatif pada masing-masing kriteria  
✅ Hitung dan tampilkan **Skor Copeland** secara otomatis  
✅ Lihat hasil akhir dalam bentuk **tabel peringkat yang jelas**

---

## 🚀 Coba Langsung

Klik tombol di bawah untuk mencoba aplikasi secara langsung:

👉 [**Buka Aplikasi di Streamlit**](https://copeland-score.streamlit.app/)

---

## ⚙️ Instalasi Lokal

### 1. Clone repositori
```bash
git clone https://github.com/username/copeland-score-app.git
```

### 2. Masuk ke direktori aplikasi
```bash
cd copeland-score-app
```

### 3. Instal dependensi
Pastikan Python telah terpasang di sistem Anda:
```bash
pip install -r requirements.txt
```

### 4. Jalankan aplikasi
```bash
streamlit run streamlit_app.py
```

> Ganti `streamlit_app.py` dengan nama file utama jika berbeda.

---

## 🧑‍💻 Cara Menggunakan

1. **Masukkan Kriteria dan Bobot**  
   ➤ Tulis satu kriteria per baris  
   ➤ Tentukan bobot dalam persen (total harus 100%)

2. **Masukkan Alternatif**  
   ➤ Tulis nama tiap alternatif, satu per baris  
   ➤ Minimal dua alternatif dibutuhkan

3. **Beri Skor**  
   ➤ Skor tiap alternatif untuk setiap kriteria (range: 0–100)

4. **Hitung Skor Copeland**  
   ➤ Klik **"Calculate Copeland Score"** untuk melihat hasil peringkat

---

## 🔍 Contoh Kasus

Misal:

- **Kriteria:** Biaya, Kualitas, Daya Tahan  
- **Bobot:** 40%, 30%, 30%  
- **Alternatif:** A, B, C

| Alternatif | Biaya | Kualitas | Daya Tahan |
|------------|-------|----------|------------|
| A          | 80    | 70       | 90         |
| B          | 60    | 85       | 80         |
| C          | 75    | 80       | 85         |

Aplikasi akan membandingkan semua pasangan alternatif dan menghitung skor Copeland untuk menentukan **peringkat akhir yang objektif dan adil**.

---

## 📄 Lisensi

Lisensi: [MIT License](LICENSE)  
Silakan gunakan, modifikasi, atau kontribusi secara bebas!

---

## 🤝 Kontribusi

Pull request dan issue sangat disambut untuk meningkatkan aplikasi ini.  
Yuk berkontribusi dalam membangun alat bantu keputusan yang bermanfaat!

---

Dibuat dengan ❤️ menggunakan [Streamlit](https://streamlit.io)
