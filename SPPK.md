## 📌 Daftar Isi
- [Fitur](#-fitur)
- [Cara Kerja](#-cara-kerja)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Contoh](#-contoh)
- [Keterbatasan](#-keterbatasan)
- [Pengembangan Selanjutnya](#-pengembangan-selanjutnya)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)

## ✨ Fitur
- ✅ Antarmuka interaktif untuk menentukan kriteria dan bobot
- ✅ Dukungan multi-alternatif dengan penilaian kustom
- ✅ Perbandingan berpasangan otomatis menggunakan metode Copeland
- ✅ Visualisasi hasil perankingan yang jelas
- ✅ Validasi input untuk bobot dan alternatif

## 🛠 Cara Kerja
Aplikasi ini mengimplementasikan metode Copeland Score melalui 3 tahap:

1. **Fase Input**:
   - Tentukan kriteria keputusan (contoh: Biaya, Kualitas)
   - Atur bobot untuk setiap kriteria (total harus 100%)
   - Masukkan alternatif yang akan dibandingkan
   - Berikan nilai untuk setiap pasang alternatif-kriteria

2. **Fase Perhitungan**:
   ```python
   def calculate_copeland_score(alternatives, weighted_scores):
       # 1. Hitung total skor tertimbang
       scores = {alt: sum(weighted_scores[alt]) for alt in alternatives}
       
       # 2. Bandingkan semua pasangan alternatif
       comparisons = {}
       for alt1, alt2 in itertools.combinations(alternatives, 2):
           if scores[alt1] > scores[alt2]:
               comparisons[(alt1, alt2)] = alt1
           elif ... # lanjutan logika perbandingan
       
       # 3. Terapkan skoring Copeland (+1 untuk menang, -1 untuk kalah)
       for (alt1, alt2), result in comparisons.items():
           if result == alt1:
               scores[alt1] += 1
               scores[alt2] -= 1
           # ... lanjutan pembaruan skor
       
       return scores
   ```

3. **Fase Output**:
   - Menampilkan alternatif yang sudah diurutkan dalam tabel
   - Menyoroti opsi dengan skor tertinggi

## 💻 Instalasi
1. Clone repositori:
   ```bash
   git clone https://github.com/namauser/kalkulator-copeland-score.git
   ```
2. Instal dependensi:
   ```bash
   pip install streamlit pandas itertools
   ```
3. Jalankan aplikasi:
   ```bash
   streamlit run aplikasi_copeland.py
   ```

## 🚀 Penggunaan
1. Masukkan kriteria keputusan (satu per baris)
2. Tetapkan bobot untuk setiap kriteria (total 100%)
3. Masukkan alternatif yang akan dibandingkan
4. Input nilai untuk setiap kombinasi alternatif-kriteria
5. Klik "Hitung Copeland Score" untuk melihat hasil

## 📊 Contoh
**Contoh Input**:
```
Kriteria: Biaya, Kualitas
Bobot: 60%, 40%
Alternatif: A, B, C
Nilai:
- A: Biaya=80, Kualitas=70
- B: Biaya=60, Kualitas=90
- C: Biaya=50, Kualitas=50
```

**Output**:
| Alternatif | Skor |
|------------|------|
| B          | 1    |
| A          | 0    |
| C          | -1   |

## ⚠️ Keterbatasan
- Memerlukan input nilai manual untuk setiap pasang alternatif-kriteria
- Tidak ada penanganan khusus untuk skor Copeland yang sama
- Performa mungkin menurun jika alternatif >10 karena kompleksitas perbandingan

## 🔮 Pengembangan Selanjutnya
- [ ] Penambahan mekanisme tie-breaker
- [ ] Fitur impor/ekspor data dalam CSV
- [ ] Visualisasi grafik distribusi skor
- [ ] Dukungan skala penilaian berbeda (misal Likert 1-5)

## 🤝 Kontribusi
Kontribusi terbuka! Silakan buat issue atau PR untuk:
- Perbaikan bug
- Fitur baru
- Penyempurnaan dokumentasi

## 📜 Lisensi
Lisensi MIT - Lihat [LICENSE](LICENSE) untuk detail
```
