import numpy as np
from numpy.random import normal
import pandas as pd
from typing import Union, List

N_SAMPLES = 500
NOISE = 0.1

# Rings
MULTIPLIER = 2

# Moons
X_OFFSET = 0.5
Y_OFFSET = 0.25


class DataGenerator:

    def create_rings(self,
                     n_samples: int = N_SAMPLES,
                     noise: Union[int, float] = NOISE,
                     multiplier: Union[int, float] = MULTIPLIER) -> List[dict]:
        """
        | Generate x and y coordinates for concentric rings whose radii are
        | offset by multiplier.
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
        |   list of two dicts in form {'label', 'x', 'y'}
        """

        x_range = np.arange(-np.pi, np.pi, (2*np.pi)/n_samples)

        x1 = np.cos(x_range) + normal(0, noise, n_samples)
        y1 = np.sin(x_range) + normal(0, noise, n_samples)

        x2 = multiplier * np.cos(x_range) + normal(0, noise, n_samples)
        y2 = multiplier * np.sin(x_range) + normal(0, noise, n_samples)

        return [
                {'label': 'A',
                 'x': [*np.round(x1, 3)],
                 'y': [*np.round(y1, 3)]
                },
                {'label': 'B',
                 'x': [*np.round(x2, 3)],
                 'y': [*np.round(y2, 3)]}
               ]

    def create_moons(self,
                     n_samples: int = N_SAMPLES,
                     noise: Union[int, float] = NOISE,
                     x_offset: Union[int, float] = X_OFFSET,
                     y_offset: Union[int, float] = Y_OFFSET) -> List[dict]:
        """
        | Generate x and y coordinates for crescent moons offset by x_offset
        | and y_offset.
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
        |    Offset in x dimension. First moon offset left, second moon
        |    offset right
        |
        |  y_offset: int, float
        |    Offset in y dimension. First moon offset up, second moon
        |    offset down
        |
        |
        | Returns
        | -------
        |   list of two dicts in form {'label', 'x', 'y'}
        """

        x_range = np.arange(-np.pi, np.pi, (2*np.pi)/n_samples)
        half_n = int(n_samples/2)

        # First moon
        x1 = np.cos(x_range[:half_n]) + normal(-x_offset, noise, half_n)
        y1 = np.sin(x_range[:half_n]) + normal(y_offset, noise, half_n)

        # Second moon
        x2 = np.cos(x_range[half_n:]) + normal(x_offset, noise, half_n)
        y2 = np.sin(x_range[half_n:]) + normal(-y_offset, noise, half_n)

        return [
                {'label': 'A',
                 'x': [*np.round(x1, 3)],
                 'y': [*np.round(y1, 3)]
                },
                {'label': 'B',
                 'x': [*np.round(x2, 3)],
                 'y': [*np.round(y2, 3)]}
               ]
