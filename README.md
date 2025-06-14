# Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahaan Jaya Jaya Maju

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dengan lebih dari 1.000 karyawan di seluruh Indonesia. Dalam dua dekade terakhir, perusahaan menunjukkan pertumbuhan signifikan dan mengukuhkan posisinya di industri.
Namun, pesatnya perkembangan bisnis diiringi tantangan dalam pengelolaan SDM, khususnya dalam mempertahankan karyawan. Tingginya attrition rate yang melebihi 10% menjadi perhatian utama, karena berdampak pada stabilitas operasional, efisiensi, serta meningkatnya biaya rekrutmen dan pelatihan.
Oleh karena itu, manajemen—khususnya Departemen HR—menilai perlu dilakukan analisis berbasis data untuk mengidentifikasi faktor penyebab dan merumuskan strategi penurunan tingkat attrition secara efektif.

---

### Permasalahan Bisnis

Permasalahan utama yang ingin diselesaikan dalam proyek ini antara lain:

1. **Tingginya tingkat attrition karyawan** (>10%) yang belum diketahui secara pasti penyebab utamanya.
2. Kurangnya **informasi terstruktur dan mendalam** terkait faktor-faktor yang memengaruhi keputusan karyawan untuk keluar.
3. Tidak adanya **alat bantu visual (dashboard)** yang dapat memantau indikator-indikator kunci SDM secara real-time.

---

### Cakupan Proyek

Proyek ini akan mencakup beberapa tahap utama sebagai berikut:

1. Eksplorasi dan Pemahaman Data: Analisis dataset `employee_data.csv` untuk memahami karakteristik karyawan dan distribusi attrition.
2. Data Preparation: Membersihkan dan memproses data agar siap digunakan untuk analisis lebih lanjut.
3. Analisis Faktor Penyebab Attrition:
   Analisis antara variabel seperti pendapatan, lembur, tingkat kepuasan, dan jarak rumah.
   Visualisasi tren dan pola attrition di berbagai departemen, level pekerjaan, dan usia karyawan.
4. Pembuatan Business Dashboard: Visualisasi data dalam bentuk dashboard yang mudah dipahami untuk memantau faktor penyebab attrition.
5. Kesimpulan dan Rekomendasi: Menarik kesimpulan dari hasil analisis dan memberikan rekomendasi praktis untuk mengurangi attrition.

---

### Persiapan

Berikut adalah tahapan untuk menyiapkannya:
Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee
Link Dashboard: https://lookerstudio.google.com/s/rRTDkRgbE40
Setup environment: Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Berikut merupakan tahapan dalam membuat virtual environment menggunakan conda untuk melakukan prediksi.

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.

```
conda create --name prediksi_attrition python=3.12.9
```

3. Aktifkan virtual environment dengan menjalankan perintah berikut

```
conda activate prediksi_attrition
```

4. Instal semua library yang dibutuhkan menggunakan perintah berikut.

```
pip install -r requirements.txt
```

5. Buka jupyter-notebook dengan menjalankan perintah berikut.

```
jupyter-notebook
```

6. Buka file python prediction.py
7. Masukkan data yang ingin diprediksi pada variabel data_baru
8. Tekan tombol run code
9. Hasil prediksi akan keluar beserta deskripsinya

## Business Dashboard

Dashboard bisnis ini dirancang untuk memvisualisasikan data terkait karyawan, termasuk tingkat attrition serta berbagai faktor yang berkontribusi terhadap tingginya attrition rate. Visualisasi mencakup aspek demografis dan kompensasi, kondisi pekerjaan dan tingkat kepuasan, keseimbangan antara pekerjaan dan kehidupan pribadi, serta faktor-faktor relevan lainnya yang berpengaruh terhadap keputusan karyawan untuk keluar dari perusahaan.

## Conclusion

Proyek analisis Human Resources pada perusahaan Jaya Jaya Maju telah berhasil mengidentifikasi pola dan faktor-faktor yang berkontribusi terhadap terjadinya attrition (perpindahan karyawan). Dengan memanfaatkan visualisasi data dalam bentuk dashboard serta evaluasi model prediksi klasifikasi, diperoleh pemahaman mendalam bahwa meskipun tingkat retensi karyawan secara umum masih tergolong tinggi, terdapat kelompok-kelompok spesifik yang memiliki risiko tinggi untuk keluar dari perusahaan.

Secara demografis, karyawan laki-laki dan kelompok usia 25–34 tahun menunjukkan angka attrition yang lebih tinggi dibanding kelompok lain. Di sisi lain, variabel seperti work-life balance, kepuasan kerja, dan terutama kualitas hubungan antarpegawai memiliki pengaruh yang signifikan terhadap keputusan karyawan untuk bertahan atau meninggalkan perusahaan. Temuan ini menunjukkan bahwa faktor non-finansial dan psikososial di lingkungan kerja memiliki peran krusial dalam retensi karyawan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
Fokus pada peningkatan kualitas hubungan kerja dan budaya organisasi, karena faktor ini terbukti berkontribusi signifikan terhadap keputusan karyawan untuk bertahan.
Tingkatkan perhatian terhadap kelompok karyawan muda, khususnya usia 25–34 tahun, melalui jalur pengembangan karier, mentoring, dan fleksibilitas kerja.
Evaluasi dan perbaiki model prediktif yang digunakan, terutama dalam menangani ketidakseimbangan data, agar bisa digunakan secara efektif sebagai sistem peringatan dini (early warning system).
Lakukan exit interview secara sistematis dan terdigitalisasi untuk melengkapi data dashboard dengan wawasan kualitatif yang lebih mendalam.
