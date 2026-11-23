"""Pembungkus operasi morfologi dan pelabelan komponen."""

import numpy as np
from skimage import morphology
from skimage.measure import label


def opening(binary: np.ndarray, footprint_size: int = 3) -> np.ndarray:
    """Melakukan opening untuk menghilangkan noise kecil."""
    return morphology.opening(binary, morphology.disk(footprint_size)).astype(np.uint8)


def closing(binary: np.ndarray, footprint_size: int = 3) -> np.ndarray:
    """Melakukan closing untuk menutup lubang kecil."""
    return morphology.closing(binary, morphology.disk(footprint_size)).astype(np.uint8)


def connected_components(binary: np.ndarray) -> tuple[np.ndarray, int]:
    """Melabeli komponen terhubung biner dengan skimage.measure.label."""
    return label(binary, connectivity=2, return_num=True)
