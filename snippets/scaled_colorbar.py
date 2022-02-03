#!/usr/bin/env python3

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def scaled_colorbar(im, size="5%", pad=0.05):
    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", size=size, pad=pad)
    return plt.colorbar(im, cax=cax)


if __name__ == "__main__":
    import numpy as np

    plt.figure()
    im = plt.imshow(np.arange(100).reshape((10, 10)))

    scaled_colorbar(im)
