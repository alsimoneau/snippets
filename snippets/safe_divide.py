#!/usr/bin/env python3
import numpy as np


def safe_divide(a, b):
    """Safely divide two arrays, with 0 as a result of a division by 0."""
    with np.errstate(divide="ignore", invalid="ignore"):
        c = np.true_divide(a, b)
        c[c == np.inf] = 0
        c = np.nan_to_num(c)
    return c


if __name__ == "__main__":
    print(safe_divide(np.random.random(5), np.arange(5)))
