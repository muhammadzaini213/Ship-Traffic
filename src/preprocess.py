"""Fungsi prapemrosesan citra Sentinel-1."""

from typing import Any, Tuple

import numpy as np
from rasterio.windows import from_bounds


def linear_to_db(array: np.ndarray, eps: float = 1e-10) -> np.ndarray:
    """Mengubah intensitas linear menjadi dB; eps mencegah log nol."""
    return 10.0 * np.log10(np.maximum(array, eps))


def crop_to_aoi(array: np.ndarray, transform: Any, aoi: Any, crs: Any) -> Tuple[np.ndarray, Any]:
    """Memotong array berdasarkan batas AOI; parameter aoi berupa GeoDataFrame."""
    import rasterio

    bounds = aoi.to_crs(crs).total_bounds
    from_rasterio = from_bounds(*bounds, transform=transform)
    with rasterio.MemoryFile() as memfile:
        profile = {"driver": "GTiff", "height": array.shape[0], "width": array.shape[1], "count": 1,
                   "dtype": array.dtype, "crs": crs, "transform": transform}
        with memfile.open(**profile) as dataset:
            dataset.write(array, 1)
            cropped = dataset.read(1, window=from_rasterio)
            cropped_transform = dataset.window_transform(from_rasterio)
    return cropped, cropped_transform


def apply_land_mask(array: np.ndarray, land_mask: np.ndarray) -> np.ndarray:
    """Menerapkan mask daratan; piksel daratan diberi NaN."""
    return np.where(land_mask.astype(bool), np.nan, array)


def contrast_stretch(array: np.ndarray, low_pct: float = 2.0, high_pct: float = 98.0) -> np.ndarray:
    """Merentangkan kontras dari persentil rendah ke persentil tinggi."""
    valid = array[np.isfinite(array)]
    if valid.size == 0:
        return np.array(array, copy=True)
    low, high = np.percentile(valid, [low_pct, high_pct])
    if high <= low:
        return np.array(array, copy=True)
    stretched = (array - low) / (high - low)
    return np.clip(stretched, 0.0, 1.0)


def lee_filter(array: np.ndarray, size: int = 7) -> np.ndarray:
    """Pembungkus tipis Lee filter; parameter size adalah ukuran jendela piksel."""
    from scipy.ndimage import uniform_filter

    mean = uniform_filter(array, size=size)
    mean_sq = uniform_filter(array * array, size=size)
    variance = np.maximum(mean_sq - mean * mean, 0.0)
    overall = np.nanmean(variance)
    noise_variance = max(overall, np.finfo(float).eps)
    weight = variance / (variance + noise_variance)
    return mean + weight * (array - mean)


def median_filter(array: np.ndarray, size: int = 7) -> np.ndarray:
    """Pembungkus tipis filter median; parameter size adalah ukuran jendela piksel."""
    from scipy.ndimage import median_filter as scipy_median

    return scipy_median(array, size=size)
