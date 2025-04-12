```markdown
# 🏆 Copeland Score Decision Maker

**Aplikasi berbasis Streamlit untuk pengambilan keputusan kelompok menggunakan metode Copeland Score**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## 📚 Daftar Isi
- [Contoh Kasus](#-contoh-kasus)
- [Fitur](#-fitur)
- [Cara Menggunakan](#-cara-menggunakan)
- [Instalasi](#-instalasi)
- [Struktur Kode](#-struktur-kode)
- [Contoh Input/Output](#-contoh-inputoutput)
- [Keterbatasan](#-keterbatasan)
- [Roadmap](#-roadmap)
- [Kontribusi](#-kontribusi)

## 🏢 Contoh Kasus: Seleksi Vendor IT

### 🎯 Kriteria & Bobot
| Kriteria               | Bobot |
|------------------------|-------|
| Harga                  | 40%   |
| Kualitas Produk        | 30%   |
| Pengalaman Vendor      | 20%   |
| Dukungan Pasca-Jual    | 10%   |

### 📊 Data Vendor
| Vendor | Harga | Kualitas | Pengalaman | Dukungan |
|--------|-------|----------|------------|----------|
| A      | 85    | 70       | 80         | 90       |
| B      | 70    | 90       | 60         | 80       |
| C      | 90    | 60       | 70         | 50       |

### 📈 Hasil Perhitungan
```python
Perhitungan Skor Tertimbang:
- Vendor A: (85×0.4) + (70×0.3) + (80×0.2) + (90×0.1) = 80
- Vendor B: (70×0.4) + (90×0.3) + (60×0.2) + (80×0.1) = 75
- Vendor C: (90×0.4) + (60×0.3) + (70×0.2) + (50×0.1) = 73

Hasil Copeland Score:
| Vendor | Skor |
|--------|------|
| A      | 2    |
| B      | 0    |
| C      | -2   |
```

## ✨ Fitur
- 🖥️ Antarmuka interaktif berbasis web
- ⚖️ Pembobotan kriteria fleksibel
- 🔢 Perhitungan otomatis skor Copeland
- 📊 Visualisasi hasil ranking
- ✅ Validasi input otomatis

## 🚀 Cara Menggunakan
1. Masukkan kriteria keputusan
2. Tetapkan bobot untuk setiap kriteria (total harus 100%)
3. Tambahkan alternatif yang akan dibandingkan
4. Input skor untuk setiap alternatif
5. Klik "Hitung Copeland Score"

Contoh perintah:
```bash
streamlit run copeland_app.py
```

## 💻 Instalasi
1. Clone repositori:
```bash
git clone https://github.com/username/copeland-decision-maker.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Jalankan aplikasi:
```bash
streamlit run src/app.py
```

## 🏗️ Struktur Kode
```
copeland-decision-maker/
├── src/
│   ├── app.py              # Main Streamlit app
│   └── copeland.py         # Core calculation logic
├── data/
│   └── examples/           # Sample input data
├── requirements.txt        # Dependencies
└── README.md               # Dokumentasi
```

## 📌 Contoh Input/Output
**Input:**
```yaml
criteria: [Harga, Kualitas, Pengalaman]
weights: [40, 30, 20]
alternatives: [Vendor A, Vendor B]
scores: [[85,70,80], [70,90,60]]
```

**Output:**
```markdown
## 🏆 Hasil Keputusan
1. Vendor A (Skor: 2)
2. Vendor B (Skor: 0)
```

## ⚠️ Keterbatasan
- Tidak mendukung impor data eksternal (CSV/Excel)
- Belum ada penanganan tie-breaker otomatis
- Antarmuka belum responsive untuk mobile

## 🗺️ Roadmap
- [x] Versi dasar dengan input manual
- [ ] Fitur impor/ekspor data
- [ ] Visualisasi grafik
- [ ] Autentikasi multi-user

## 🤝 Kontribusi
Silakan buka issue atau pull request untuk:
- Laporkan bug
- Usulkan fitur baru
- Perbaiki dokumentasi
