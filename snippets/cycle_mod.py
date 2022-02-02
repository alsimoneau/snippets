#!/usr/bin/env python3

import numpy as np


def cycle_mod(x, a=2 * np.pi):
    pos, neg = x % a, x % -a
    return np.where(np.abs(neg) < pos, neg, pos)


if __name__ == "__main__":
    print(f"2 * 270deg = {cycle_mod(2 * 270, 360)}")
