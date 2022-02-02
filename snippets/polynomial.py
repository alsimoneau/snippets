#!/usr/bin/env python3

import numpy as np


def polynomial(x, *c):
    return np.dot(np.array(x)[:, None] ** np.arange(len(c)), c)


if __name__ == "__main__":
    from scipy.optimize import curve_fit

    x = np.linspace(-5, 5, 101)
    y = np.random.random(len(x)) - 0.5 + 0.5 * x ** 2
    p0, err = curve_fit(polynomial, x, y, p0=[1] * 3)
    print(*p0)
