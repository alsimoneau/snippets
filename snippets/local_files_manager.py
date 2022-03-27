#!/usr/bin/env python3

import os


class LocalFilesManager:
    def __init__(self, *filelist):
        def parse(elem):
            if type(elem) is str:
                elem = [elem, ""]
            if len(elem) != 2:
                raise TypeError(
                    "elements must be single strings or 2-uple of string"
                )
            elem = list(elem)
            if os.path.basename(elem[1]) == "":
                elem[1] += os.path.basename(elem[0])
            return tuple(elem)

        self.filelist = [parse(elem) for elem in filelist]
        self.dirs = {os.path.dirname(elem[1]) for elem in self.filelist} - {""}

    def __enter__(self):
        for dir in self.dirs:
            os.makedirs(dir, exist_ok=True)
        for src, dst in self.filelist:
            os.symlink(os.path.abspath(src), dst)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for src, dst in self.filelist:
            os.remove(dst)
        for dir in self.dirs:
            os.removedirs(dir)
