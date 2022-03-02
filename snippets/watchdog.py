#!/usr/bin/env python3

import signal


class Watchdog(Exception):
    def __init__(self, time=5):
        self.time = time

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(self.time)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)

    def handler(self, signum, frame):
        raise self

    def __str__(self):
        return f"The function took more than {self.time:d}s to complete"


def watchdog(func, t):
    def wrapped(*args, **kwargs):
        try:
            with Watchdog(t):
                return func(*args, **kwargs)
        except Watchdog as w:
            print(w)
            return None

    return wrapped
