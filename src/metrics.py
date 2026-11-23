"""Metrik evaluasi deteksi objek terhadap kebenaran dasar."""

from typing import Iterable, Tuple

import numpy as np


def match_detections(ground_truth_points: Iterable[Tuple[float, float]],
                     detected_points: Iterable[Tuple[float, float]],
                     distance_threshold: float) -> tuple[np.ndarray, np.ndarray]:
    """Memasangkan titik dengan kriteria jarak Euclidean terdekat.

    Setiap kebenaran dasar hanya boleh cocok satu deteksi dan sebaliknya.
    Titik yang berjarak melebihi distance_threshold dianggap salah deteksi
    atau negatif palsu. Merupakan aturan pencocokan sederhana untuk notebook.
    """
    truth = np.asarray(list(ground_truth_points), dtype=float).reshape(-1, 2)
    detections = np.asarray(list(detected_points), dtype=float).reshape(-1, 2)
    if truth.size == 0:
        return np.full(detections.shape[0], -1, dtype=int), np.array([], dtype=int)
    if detections.size == 0:
        return np.array([], dtype=int), np.full(truth.shape[0], -1, dtype=int)

    distances = np.linalg.norm(truth[:, None, :] - detections[None, :, :], axis=2)
    matches = []
    for _ in range(min(truth.shape[0], detections.shape[0])):
        index = np.unravel_index(np.argmin(distances), distances.shape)
        if distances[index] > distance_threshold:
            break
        truth_index, detection_index = index
        matches.append((truth_index, detection_index))
        distances[truth_index, :] = np.inf
        distances[:, detection_index] = np.inf

    truth_match = np.full(truth.shape[0], -1, dtype=int)
    detection_match = np.full(detections.shape[0], -1, dtype=int)
    for truth_index, detection_index in matches:
        truth_match[truth_index] = detection_index
        detection_match[detection_index] = truth_index
    return detection_match, truth_match


def confusion_matrix(
    detection_match: np.ndarray,
    truth_match: np.ndarray,
) -> np.ndarray:
    """Mengembalikan matriks kebingungan 2x2 untuk hasil pencocokan deteksi.

    Urutan baris/kolom adalah [[TN, FP], [FN, TP]], tanpa piksel latar yang
    tidak teruji. Elemen TN mengikuti representasi acuan evaluasi objek.
    """
    tp = int(np.count_nonzero(detection_match >= 0))
    fp = int(np.count_nonzero(detection_match < 0))
    fn = int(np.count_nonzero(truth_match < 0))
    tn = 0
    return np.array([[tn, fp], [fn, tp]], dtype=int)


def precision(tp: int, fp: int) -> float:
    """Menghitung precision = TP / (TP + FP)."""
    return tp / (tp + fp) if tp + fp else 0.0


def recall(tp: int, fn: int) -> float:
    """Menghitung recall = TP / (TP + FN)."""
    return tp / (tp + fn) if tp + fn else 0.0


def f1_score(tp: int, fp: int, fn: int) -> float:
    """Menghitung F1 sebagai harmonik precision dan recall."""
    p = precision(tp, fp)
    r = recall(tp, fn)
    return 2 * p * r / (p + r) if p + r else 0.0


def iou(tp: int, fp: int, fn: int) -> float:
    """Menghitung Intersection over Union untuk deteksi objek."""
    return tp / (tp + fp + fn) if tp + fp + fn else 0.0


def overall_accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    """Menghitung akurasi keseluruhan (TP + TN) / jumlah semua kasus."""
    total = tp + tn + fp + fn
    return (tp + tn) / total if total else 0.0
