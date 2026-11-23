"""I/O untuk GeoTIFF dan AOI."""

from pathlib import Path
from typing import Any, Tuple

import numpy as np
import rasterio


def read_geotiff(path: str) -> Tuple[np.ndarray, Any, Any]:
    """Membaca GeoTIFF dan mengembalikan array, transform, serta CRS."""
    with rasterio.open(path) as src:
        array = src.read(1)
        return array, src.transform, src.crs


def save_geotiff(path: str, array: np.ndarray, transform: Any, crs: Any) -> None:
    """Menyimpan array sebagai GeoTIFF satu band."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with rasterio.open(
        path,
        "w",
        driver="GTiff",
        height=array.shape[0],
        width=array.shape[1],
        count=1,
        dtype=array.dtype,
        crs=crs,
        transform=transform,
    ) as dst:
        dst.write(array, 1)


def load_aoi(path: str):
    """Memuat GeoJSON AOI dengan GeoPandas."""
    import geopandas as gpd

    return gpd.read_file(path)
