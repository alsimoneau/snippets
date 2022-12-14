#!/usr/bin/env python3

import contextlib

import joblib
from tqdm import tqdm


@contextlib.contextmanager
def tqdm_joblib(tqdm_object):
    def tqdm_print_progress(self):
        if self.n_completed_tasks > tqdm_object.n:
            n_completed = self.n_completed_tasks - tqdm_object.n
            tqdm_object.update(n=n_completed)

    original_print_progress = joblib.parallel.Parallel.print_progress
    joblib.parallel.Parallel.print_progress = tqdm_print_progress

    try:
        yield tqdm_object
    finally:
        joblib.parallel.Parallel.print_progress = original_print_progress
        tqdm_object.close()


def parallelize_progress(func):
    def wrapper(iterable, *args):
        it = list(iterable)
        with tqdm_joblib(tqdm(total=len(it))):
            return joblib.Parallel(n_jobs=-1, prefer="threads")(
                joblib.delayed(func)(i, *args) for i in it
            )

    return wrapper
