#!/usr/bin/env python3

import joblib


def parallelize(func):
    def wrapper(iterable, *args):
        return joblib.Parallel(n_jobs=-1, prefer="threads")(
            joblib.delayed(func)(i, *args) for i in iterable
        )

    return wrapper


if __name__ == "__main__":

    @parallelize
    def process(i, x):
        return sum(j ** i for j in range(x))

    process(range(100), 10)
