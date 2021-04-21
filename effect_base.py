import abc
import numpy as np


class EffectBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def apply(self, src: np.array, rate: int, sample_width: int) -> np.array:
        raise NotImplementedError("Abstract method not implemented!")
