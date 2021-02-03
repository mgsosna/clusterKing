import numpy as np
from numpy.random import normal
import pandas as pd
from typing import Union, List

N_SAMPLES = 500
NOISE = 0.1

# Rings
MULTIPLIER = 2

# Moons, blobs
X_OFFSET = 0.5
Y_OFFSET = 0.25


class DataGenerator:

    def create_blobs(self,
                     n_samples: int = N_SAMPLES,
                     noise: Union[int, float] = NOISE,
                     x_offset: Union[int, float] = X_OFFSET,
                     y_offset: Union[int, float] = Y_OFFSET) -> dict:
        """
        | Generate x and y coordinates for two clusters
        |
        | -----------------------------------------------------------
        | Parameters
        | ----------
        |  n_samples : int
        |    Number of samples
        |
        |  noise : int, float
        |    How tight the blobs are around their mean
        |
        |  x_offset: int, float
        |    Offset in x dimension. Large values move moons apart,
        |    small move moons closer
        |
        |  y_offset: int, float
        |    Offset in y dimension. Positive values move moons apart,
        |    negative move moons closer
        |
        |
        | Returns
        | -------
        |   dict with keys ['x', 'y']
        """
        x1 = normal(0, noise, n_samples) + x_offset
        x2 = normal(0, noise, n_samples) - x_offset

        y1 = normal(0, noise, n_samples) + y_offset
        y2 = normal(0, noise, n_samples) - y_offset

        return {'x': [*np.concatenate([x1, x2]).round(3)],
                'y': [*np.concatenate([y1, y2]).round(3)]}

    def create_rings(self,
                     n_samples: int = N_SAMPLES,
                     noise: Union[int, float] = NOISE,
                     multiplier: Union[int, float] = MULTIPLIER) -> dict:
        """
        | Generate x and y coordinates for two concentric rings whose radii
        | are offset by multiplier.
        |
        | -----------------------------------------------------------------
        | Parameters
        | ----------
        |  n_samples: int
        |    Number of samples
        |
        |  noise : int, float
        |    Noise to add to rings. 0 = perfect curves
        |
        |  multiplier: int, float
        |    Offset for second ring's radius
        |
        |
        | Returns
        | -------
        |   dict with keys ['x', 'y']
        """
        x_range = np.arange(-np.pi, np.pi, (2*np.pi)/n_samples)

        x1 = np.cos(x_range) + normal(0, noise, n_samples)
        y1 = np.sin(x_range) + normal(0, noise, n_samples)

        x2 = multiplier * np.cos(x_range) + normal(0, noise, n_samples)
        y2 = multiplier * np.sin(x_range) + normal(0, noise, n_samples)

        return {'x': [*np.concatenate([x1, x2]).round(3)],
                'y': [*np.concatenate([y1, y2]).round(3)]}

    def create_moons(self,
                     n_samples: int = N_SAMPLES,
                     noise: Union[int, float] = NOISE,
                     x_offset: Union[int, float] = X_OFFSET,
                     y_offset: Union[int, float] = Y_OFFSET) -> dict:
        """
        | Generate x and y coordinates for two crescent moons offset by
        |  x_offset and y_offset.
        |
        | ------------------------------------------------------------------
        | Parameters
        | ----------
        |  n_samples: int
        |    Number of samples
        |
        |  noise : int, float
        |    Noise to add to moons. 0 = perfect curves
        |
        |  x_offset: int, float
        |    Offset in x dimension. Large values move moons apart,
        |    small move moons closer
        |
        |  y_offset: int, float
        |    Offset in y dimension. Positive values move moons apart,
        |    negative move moons closer
        |
        |
        | Returns
        | -------
        |   dict with keys ['x', 'y']
        """
        x_range = np.arange(-np.pi, np.pi, (2*np.pi)/n_samples)
        half_n = int(n_samples/2)

        # First moon
        x1 = np.cos(x_range[:half_n]) + normal(-x_offset, noise, half_n)
        y1 = np.sin(x_range[:half_n]) + normal(-y_offset, noise, half_n)

        # Second moon
        x2 = np.cos(x_range[half_n:]) + normal(x_offset, noise, half_n)
        y2 = np.sin(x_range[half_n:]) + normal(y_offset, noise, half_n)

        return {'x': [*np.concatenate([x1, x2]).round(3)],
                'y': [*np.concatenate([y1, y2]).round(3)]}
