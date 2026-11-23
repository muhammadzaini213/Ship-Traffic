"""Ekstraksi fitur objek kapal dalam satuan fisik."""

from typing import Iterable

import numpy as np
from skimage.measure import regionprops


def area(region: object) -> float:
    """Mengembalikan luas objek dalam piksel."""
    return float(region.area)


def perimeter(region: object, pixel_size_m: float) -> float:
    """Mengembalikan perimeter objek dalam meter."""
    return float(region.perimeter) * pixel_size_m


def major_axis_length(region: object, pixel_size_m: float) -> float:
    """Mengembalikan panjang sumbu utama objek dalam meter."""
    return float(region.axis_major_length) * pixel_size_m


def minor_axis_length(region: object, pixel_size_m: float) -> float:
    """Mengembalikan panjang sumbu minor objek dalam meter."""
    return float(region.axis_minor_length) * pixel_size_m


def aspect_ratio(region: object, pixel_size_m: float) -> float:
    """Mengembalikan rasio sumbu utama terhadap sumbu minor."""
    major = major_axis_length(region, pixel_size_m)
    minor = minor_axis_length(region, pixel_size_m)
    return major / minor if minor > 0 else np.nan


def eccentricity(region: object) -> float:
    """Mengembalikan eksentrisitas bentuk objek."""
    return float(region.eccentricity)


def compactness(region: object, pixel_size_m: float) -> float:
    """Mengembalikan indeks kompaktes berdasarkan perimeter dan luas."""
    area_m2 = area(region) * (pixel_size_m ** 2)
    perimeter_m = perimeter(region, pixel_size_m)
    return (perimeter_m ** 2) / (4 * np.pi * area_m2) if area_m2 > 0 else np.nan


def mean_intensity(region: object) -> float:
    """Mengembalikan intensitas rata-rata objek."""
    return float(region.mean_intensity)


def shape_features(label_image: np.ndarray, intensity_image: np.ndarray,
                   pixel_size_m: float) -> Iterable[dict]:
    """Mengembalikan fitur bentuk dan intensitas per objek.

    Input: label_image, intensity_image, dan ukuran satu piksel dalam meter.
    Output: iterable kamus dengan area (piksel dan m2), perimeter, sumbu
    utama/minor, rasio aspek, eksentrisitas, kompaktes, dan intensitas rata-rata.
    Konversi m2 dan hektar menggunakan ukuran piksel serta skala spasial yang
    diberikan; skimage.measure.regionprops menjadi sumber pengukuran bentuk.
    """
    pixel_area_m2 = pixel_size_m ** 2
    for region in regionprops(label_image, intensity_image=intensity_image):
        major = getattr(region, "axis_major_length", 0.0) * pixel_size_m
        minor = getattr(region, "axis_minor_length", 0.0) * pixel_size_m
        area_pixels = float(region.area)
        area_m2 = area_pixels * pixel_area_m2
        aspect_ratio = major / minor if minor > 0 else np.nan
        perimeter_m = float(region.perimeter) * pixel_size_m
        compactness = (
            (perimeter_m ** 2) / (4 * np.pi * area_m2)
            if area_m2 > 0 else np.nan
        )
        yield {
            "label": region.label,
            "area_pixels": area_pixels,
            "area_m2": area_m2,
            "area_ha": area_m2 / 10000.0,
            "perimeter_m": perimeter_m,
            "major_axis_m": major,
            "minor_axis_m": minor,
            "aspect_ratio": aspect_ratio,
            "eccentricity": float(region.eccentricity),
            "compactness": compactness,
            "mean_intensity": float(region.mean_intensity),
        }
