#!/usr/bin/env python3

import numpy as np


def angular_mean(a, degrees=False):
    if degrees:
        a = np.deg2rad(a)

    m = np.arctan2(np.mean(np.sin(a)), np.mean(np.cos(a)))

    if degrees:
        m = np.rad2deg(m)

    return m


if __name__ == "__main__":
    angles = [[350, 10], [90, 180, 270, 360], [10, 20, 30]]
    for a in angles:
        print(angular_mean(a, degrees=True))
