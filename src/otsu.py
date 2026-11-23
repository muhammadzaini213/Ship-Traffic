"""Stub segmentasi Otsu untuk implementasi mahasiswa."""

from typing import Optional

import numpy as np


def segment_otsu(image: np.ndarray, threshold: Optional[float] = None) -> np.ndarray:
    """
    Input:
        image: citra 2D dalam skala linear atau dB.
        threshold: ambang awal opsional untuk eksperimen sensitivitas.
    Output:
        binary: citra biner hasil segmentasi.
    Parameter:
        threshold digunakan sebagai ambang pengganti hanya jika ditentukan.
    Formula:
        Mahasiswa mendeskripsikan dan mengimplementasikan pemaksimalan
        variance antarkelas untuk menentukan ambang Otsu dari histogram.
    """
    raise NotImplementedError("Implementasi Otsu ditulis oleh mahasiswa.")
