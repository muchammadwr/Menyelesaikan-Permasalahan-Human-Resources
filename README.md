# Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahaan Jaya Jaya Maju

## Business Understanding

**Jaya Jaya Maju** adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai wilayah Indonesia. Perusahaan ini telah mengalami pertumbuhan yang signifikan dalam dua dekade terakhir, membuktikan posisinya sebagai pemain besar di industrinya.

Namun, seiring dengan perkembangan bisnis yang pesat, perusahaan menghadapi tantangan besar dalam hal manajemen sumber daya manusia (SDM), khususnya dalam mempertahankan karyawan. Salah satu indikator utama yang menjadi perhatian adalah tingginya **attrition rate**, yaitu tingkat keluarnya karyawan dari perusahaan, yang telah mencapai lebih dari **10%**.

Angka ini cukup mengkhawatirkan dan dapat memengaruhi stabilitas operasional, efisiensi bisnis, serta biaya rekrutmen dan pelatihan karyawan baru. Maka dari itu, pihak manajemen—khususnya Departemen Human Resource (HR)—memandang perlu adanya pendekatan berbasis data untuk mengidentifikasi penyebab dari tingginya tingkat attrition dan mengambil langkah strategis yang tepat.

---

### Permasalahan Bisnis

Permasalahan utama yang ingin diselesaikan dalam proyek ini antara lain:

1. **Tingginya tingkat attrition karyawan** (>10%) yang belum diketahui secara pasti penyebab utamanya.
2. Kurangnya **informasi terstruktur dan mendalam** terkait faktor-faktor yang memengaruhi keputusan karyawan untuk keluar.
3. Tidak adanya **alat bantu visual (dashboard)** yang dapat memantau indikator-indikator kunci SDM secara real-time.
4. Kebutuhan akan **sistem peringatan dini (early warning)** berbasis data untuk membantu tim HR mengambil tindakan preventif terhadap potensi attrition.

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

### Persiapan

Masuk ke folder dan install dependencies untuk menginstall dependencies

```
pip install -r requirements.txt
```

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee
Link Dashboard: https://lookerstudio.google.com/reporting/62273fc3-0937-44b7-af99-889c6a3cffe9

## Business Dashboard

Dashboard Human Resources perusahaan Jaya Jaya Maju menunjukkan bahwa dari total 1.058 karyawan, terdapat 179 orang yang mengalami attrition, yang mencerminkan tingkat attrition sebesar 16.9%. Artinya, sebagian besar karyawan, yaitu 83.1%, masih bertahan di perusahaan hingga saat ini. Informasi ini memberikan gambaran umum tentang stabilitas tenaga kerja di perusahaan, dengan tingkat perpindahan karyawan yang tergolong sedang.

Dilihat dari sisi gender, karyawan laki-laki mendominasi dalam hal jumlah maupun angka attrition. Terdapat 108 karyawan laki-laki yang keluar dibandingkan dengan 71 karyawan perempuan, meskipun jumlah laki-laki yang bertahan juga lebih tinggi (512 dibandingkan 367). Hal ini menunjukkan bahwa meskipun dominasi laki-laki terlihat dalam jumlah total, mereka juga lebih rentan terhadap attrition secara absolut.

Faktor work-life balance juga dianalisis dalam dashboard ini. Kategori “High” menjadi yang paling banyak diisi oleh karyawan, dengan 544 orang bertahan dan 94 orang keluar. Namun, menarik untuk dicatat bahwa meskipun memiliki tingkat keseimbangan kerja yang tinggi, angka attrition tetap tinggi, menunjukkan bahwa keseimbangan hidup kerja yang baik belum tentu cukup untuk mempertahankan karyawan. Sementara itu, kategori “Very High” dan “Low” justru mencatat angka keluar yang jauh lebih rendah, meskipun total populasinya juga lebih kecil.

Dari aspek kepuasan kerja, terlihat bahwa karyawan dengan tingkat kepuasan “Very High” dan “High” masih mencatat jumlah yang keluar masing-masing sebanyak 39 dan 62 orang. Di sisi lain, kelompok dengan kepuasan “Low” menunjukkan attrition sebesar 46 orang, yang merupakan proporsi cukup besar dibanding total kelompok tersebut. Ini mengindikasikan bahwa meskipun kepuasan rendah berdampak negatif terhadap retensi, tingkat kepuasan tinggi tidak serta-merta menjamin loyalitas karyawan.

Analisis hubungan sosial di tempat kerja juga memberikan wawasan penting. Karyawan dengan hubungan kerja yang tergolong “High” dan “Very High” tetap mencatat angka attrition yang signifikan (49 dan 52 orang), tetapi angka tertinggi secara proporsional ditemukan pada kelompok dengan hubungan “Low”, yakni 46 orang dari 201. Ini menandakan bahwa kualitas hubungan interpersonal di tempat kerja sangat berpengaruh terhadap keputusan karyawan untuk bertahan atau meninggalkan perusahaan.

Terakhir, dari segi usia, kelompok 25–34 tahun menjadi kelompok dengan angka keluar tertinggi (85 orang), disusul oleh kelompok usia 35–44 tahun dengan 39 orang. Sedangkan kelompok usia lebih muda (18–24) dan lebih tua (55–64) menunjukkan angka attrition yang jauh lebih rendah. Pola ini sesuai dengan tren umum di dunia kerja, di mana karyawan usia muda dan dewasa awal lebih aktif berpindah kerja dibanding kelompok lainnya.

Secara keseluruhan, laporan ini menunjukkan bahwa meskipun perusahaan memiliki tingkat retensi yang cukup tinggi, terdapat tantangan khusus yang perlu diperhatikan, terutama pada kelompok usia produktif dan faktor hubungan kerja. Oleh karena itu, disarankan agar perusahaan lebih fokus dalam membina relasi kerja yang sehat serta meninjau kembali strategi retensi terhadap kelompok usia muda yang cenderung lebih mobile secara karier.

## Conclusion

Proyek analisis Human Resources pada perusahaan Jaya Jaya Maju telah berhasil mengidentifikasi pola dan faktor-faktor yang berkontribusi terhadap terjadinya attrition (perpindahan karyawan). Dengan memanfaatkan visualisasi data dalam bentuk dashboard serta evaluasi model prediksi klasifikasi, diperoleh pemahaman mendalam bahwa meskipun tingkat retensi karyawan secara umum masih tergolong tinggi (83.1%), terdapat kelompok-kelompok spesifik yang memiliki risiko tinggi untuk keluar dari perusahaan.

Secara demografis, karyawan laki-laki dan kelompok usia 25–34 tahun menunjukkan angka attrition yang lebih tinggi dibanding kelompok lain. Di sisi lain, variabel seperti work-life balance, kepuasan kerja, dan terutama kualitas hubungan antarpegawai memiliki pengaruh yang signifikan terhadap keputusan karyawan untuk bertahan atau meninggalkan perusahaan. Temuan ini menunjukkan bahwa faktor non-finansial dan psikososial di lingkungan kerja memiliki peran krusial dalam retensi karyawan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Fokus pada peningkatan kualitas hubungan kerja dan budaya organisasi, karena faktor ini terbukti berkontribusi signifikan terhadap keputusan karyawan untuk bertahan.

- Tingkatkan perhatian terhadap kelompok karyawan muda, khususnya usia 25–34 tahun, melalui jalur pengembangan karier, mentoring, dan fleksibilitas kerja.

- Evaluasi dan perbaiki model prediktif yang digunakan, terutama dalam menangani ketidakseimbangan data, agar bisa digunakan secara efektif sebagai sistem peringatan dini (early warning system).

- Lakukan exit interview secara sistematis dan terdigitalisasi untuk melengkapi data dashboard dengan wawasan kualitatif yang lebih mendalam.
