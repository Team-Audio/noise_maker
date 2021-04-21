from typing import Tuple

import numpy as np
import pydub
from pydub import generators

from effect_base import EffectBase


class FiftyHertz(EffectBase):

    def __init__(self, gain=-25):
        self.gain = gain

    def apply(self, src: np.array, rate: int, sample_width: int) -> Tuple[np.array, int, int]:
        length = len(src) / rate

        orig = pydub.AudioSegment(src.tobytes(), frame_rate=rate, sample_width=sample_width, channels=1)
        noise = generators.Square(sample_rate=rate, freq=50).to_audio_segment(length * 1000, 0.0)
        new = noise.overlay(orig, gain_during_overlay=self.gain)

        return new.get_array_of_samples(), new.frame_rate, new.sample_width
