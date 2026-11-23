"""Konfigurasi pusat untuk proyek deteksi trafik kapal."""

RANDOM_SEED = 42
PIXEL_AREA_M2 = None  # TODO: isi luas satu piksel dalam m2 setelah pixel_size_m pada scene table tersedia

DATA_DIR = "TODO_DRIVE_DATA_FOLDER"
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
AOI_PATH = "aoi/aoi.geojson"
SCENE_TABLE_PATH = "data/scene_table.csv"
GROUND_TRUTH_PATH = "ground_truth/ground_truth.csv"
RESULTS_DIR = "results"
