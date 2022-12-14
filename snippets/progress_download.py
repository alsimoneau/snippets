# https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests

import os
from urllib.request import urlopen

import progressbar
import requests


def progress_download(url, block_size=1024):
    site = urlopen(url)
    meta = site.info()
    response = requests.get(url, stream=True)
    bytes = int(meta["Content-Length"])

    pbar = progressbar.DataTransferBar(max_value=bytes).start()
    with open(os.path.basename(url), "wb") as f:
        for i, data in enumerate(response.iter_content(block_size)):
            pbar.update(block_size * i)
            f.write(data)
    pbar.finish()


if __name__ == "__main__":
    progress_download("http://dome.obsand.org:2080/wiki/html/hydropolys.zip")
