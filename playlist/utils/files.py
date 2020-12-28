import io
import os


def read_file(path, **kwargs):
    content = ""
    with io.open(path, **kwargs) as open_file:
        content = open_file.read().strip()
    return content
