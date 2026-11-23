"""Stub segmentasi CFAR untuk implementasi mahasiswa."""

import numpy as np


def segment_cfar(image: np.ndarray, guard_size: int = 3, window_size: int = 11,
                 pfa: float = 1e-6) -> np.ndarray:
    """
    Input:
        image: citra 2D dalam skala linear atau dB.
        guard_size: radius area pelindung sekitar sel diuji.
        window_size: ukuran jendela training.
        pfa: probabilitas false alarm yang ditargetkan.
    Output:
        binary: citra biner hasil segmentasi.
    Parameter:
        guard_size dan window_size disetel dan diuji sensitivitasnya;
        pfa mengontrol ambang false alarm.
    Formula:
        Mahasiswa mendeskripsikan estimasi distribusi latar pada jendela
        training lalu membangun ambang berdasarkan pfa.
    """
    raise NotImplementedError("Implementasi CFAR ditulis oleh mahasiswa.")
