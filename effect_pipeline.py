from typing import List
from effect_base import EffectBase
import numpy as np


class EffectPipeline:

    def __init__(self, pipeline: List[EffectBase]):
        self.pipeline = pipeline

    def run(self, sample: np.array, rate: int, sample_width) -> np.array:
        for step in self.pipeline:
            sample, rate, sample_width = step.apply(sample, rate, sample_width)
        return sample, rate, sample_width
