#!/usr/bin/env python3

import numpy as np


def circle_mask(x, y, shape, r):
    Y, X = np.ogrid[: shape[0], : shape[1]]
    return (X - x) ** 2 + (Y - y) ** 2 < r ** 2


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.imshow(circle_mask(10, 5, (20, 20), 3))
