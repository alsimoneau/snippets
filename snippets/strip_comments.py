#!/usr/bin/env python3


def strip_comments(item, token="#"):
    """Generator. Strips comments and whitespace from input lines.

    This generator strips comments, leading/trailing whitespace, and
    blank lines from its input.

    Arguments:
        item (obj):  Object to strip comments from.
        token (str, optional):  Comment delimiter.  Defaults to ``#``.

    Yields:
        str:  Next non-blank line from ``item`` with comments and
            leading/trailing whitespace removed.

    Credits: Doug R., StackOverflow
    """

    for line in item:
        s = line.split(token, 1)[0].strip()
        if s != "":
            yield s


if __name__ == "__main__":
    text = """# header
    # long header
    some data
    # more comments
    some more data"""

    for line in strip_comments(text):
        print(line)
