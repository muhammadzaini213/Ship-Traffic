# Deteksi Trafik Kapal pada Koridor Masalembo, Laut Jawa

Proyek ini merupakan tugas mata kuliah Pengolahan Citra Digital di Institut Teknologi Kalimantan untuk mendeteksi dan mengevaluasi trafik kapal pada koridor Masalembo, Laut Jawa, menggunakan citra Sentinel-1 GRD (IW, polarisasi VV) dari sekurang-kurangnya tiga tanggal. Proyek membangun alur kerja eksplorasi, prapemrosesan, segmentasi, ekstraksi fitur, dan evaluasi dengan kebenaran dasar buatan tim.

## Tim

- Anggota 1: **TODO_NAMA_ANGGOTA_1**
- Anggota 2: **TODO_NAMA_ANGGOTA_2**

## Struktur repository

```text
README.md
requirements.txt
.gitignore
aoi/                 # batas Area of Interest GeoJSON
data/                # informasi dataset dan tabel pemandu
  raw/               # GeoTIFF mentah disimpan lokal/Drive, bukan Git
ground_truth/        # pedoman pelabelan kebenaran dasar
notebooks/           # alur kerja 01-05
src/                 # utilitas dan stub pembelajaran
results/             # gambar, peta, dan tabel keluaran
docs/                # proposal dan catatan kerja
```

## Menjalankan di Google Colab

1. Unggah atau hubungkan Google Drive.
2. Buka salah satu notebook pada folder `notebooks/` melalui Google Colab.
3. Jalankan sel pengaturan pertama untuk mengganti repo, memasang pustaka, dan menyiapkan direktori data.
4. Ganti `TODO_DRIVE_DATA_FOLDER` dengan folder Drive yang berisi berkas mentah; tautannya dicatat di `data/README.md`.
5. Jalankan notebook secara berurutan dari `01_eksplorasi.ipynb` sampai `05_evaluasi.ipynb`.

## Menjalankan secara lokal

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Versi pustaka

Persyaratan minimum tercantum di `requirements.txt`: NumPy, SciPy, OpenCV-Python, scikit-image, Rasterio, Matplotlib, pandas, GeoPandas, Shapely, dan Jupyter.

## Seed acak dan reproducibility

Proyek menggunakan `RANDOM_SEED = 42`, didefinisikan di `src/config.py`. Untuk mengulang hasil dari data mentah hingga angka akhir:

1. Unduh citra Sentinel-1 GRD yang tercantum di `data/scene_table.csv` dari sumber data yang disepakati, namun isi tabel pada lembar ini tetap TODO.
2. Letakkan berkas mentah pada folder Drive sesuai pola `S1_YYYYMMDD_VV.tif`.
3. Simpan AOI sebagai `aoi/aoi.geojson` dalam EPSG:4326.
4. Jalankan notebook 01 sampai 05 secara berurutan dan simpan keluaran pada folder `results/`.
5. Catat parameter, perubahan, evaluasi, dan tautan commit dalam dokumen pada folder `docs/`.

## Tautan data

`TODO_TAUTAN_GOOGLE_DRIVE_DATASET` — tautan belum diisi.

## Atribusi

"Contains modified Copernicus Sentinel data 2026"

## Catatan algoritma inti

Core algorithm **Otsu dan CFAR dilaksanakan sendiri oleh mahasiswa** dalam `src/otsu.py` dan `src/cfar.py`. Repository awal hanya menyediakan signature dan NotImplementedError agar implementasi tidak diberikan sebelumnya.
