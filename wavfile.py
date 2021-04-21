import numpy as np
import pydub
from typing import Tuple


def read_wavfile(path: str) -> Tuple[int, int, np.array]:
    s = pydub.AudioSegment.from_wav(path)
    return (
        s.frame_rate,
        s.sample_width,
        np.array(s.get_array_of_samples())
    )


def write_wavfile(path: str, arr: np.array, rate: int, sample_width: int):
    s = pydub.AudioSegment(arr, frame_rate=rate, sample_width=sample_width,channels=1)
    s.export(path, format='wav')
