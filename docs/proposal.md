# Proposal Proyek — Deteksi Trafik Kapal

## 1. Tema dan Sumber Kejadian

TODO: jelaskan tema proyek dan kaitkan kejadian dengan sumber kejadian bernama. Gunakan sitasi Harvard, misalnya: TODO_NAMA_PENULIS (TODO_TAHUN). Tambahkan referensi bibliografi lengkap setelah sumber terverifikasi.

## 2. Pertanyaan Terukur

TODO: nyatakan pertanyaan yang dapat dijawab dengan metrik, misalnya berapa presisi, recall, F1, dan IoU pada sekurang-kurangnya tiga tanggal citra?

## 3. AOI

TODO: deskripsikan koridor Masalembo dalam batas geografis yang telah disepakati. AOI disimpan sebagai `aoi/aoi.geojson` dalam EPSG:4326 dan mendekati 20 × 20 km.

## 4. Rencana Tanggal Citra

TODO: daftarkan sekurang-kurangnya tiga tanggal Sentinel-1 dalam format `YYYY-MM-DD`; jangan inventarisasi tanggal sebelum citra tersedia.

## 5. Rancangan Tujuh Tahap

1. Eksplorasi: memeriksa statistik, histogram, dan konsistensi tiap band serta antartanggal.
2. Prapemrosesan: mengubah intensitas ke dB dan menerapkan crop AOI, mask daratan, serta filter speckle.
3. Segmentasi: membandingkan metode Otsu dan CFAR buatan mahasiswa pada AOI yang sama.
4. Morfologi: membersihkan komponen biner dan melakukan connected component labeling.
5. Ekstraksi fitur: menghitung bentuk, intensitas, dan tekstur tiap objek dalam satuan fisik.
6. Evaluasi: mencocokkan deteksi dengan kebenaran dasar dan menghitung metrik deteksi.
7. Visualisasi: menyusun peta, grafik distribusi ukuran, dan analisis kegagalan.

## 6. Pembagian Peran Dua Orang

- TODO_NAMA_ANGGOTA_1: TODO_PERAN_1
- TODO_NAMA_ANGGOTA_2: TODO_PERAN_2

## 7. Rencana Kebenaran Dasar

TODO: rancang pelabelan 100–200 objek, pembagian peran pelabel, pemeriksaan silang oleh pelabel kedua, dan metode resolusi ketidaksepakatan.
