import io
import json
import sys
from pathlib import Path

import jmespath


class StdoutInventory:
    def stdout(
        self, data, extra_data=None, fields=None, format=None, delimiter=","
    ):
        if fields is not None and fields:
            expression = jmespath.compile(fields)
            filtered = expression.search(data)
            for line in filtered:
                if type(line) is dict:
                    items = line.values()
                if type(line) is list:
                    items = line
                else:
                    items = [line]

                if format is not None and format:
                    try:
                        formatted = delimiter.join(
                            format.format(w) for w in items
                        )
                    except Exception:
                        formatted = format.format(*tuple(items))
                else:
                    formatted = delimiter.join("{0}".format(w) for w in items)

                sys.stdout.write(formatted)
                sys.stdout.write("\n")
        else:
            if extra_data is not None:
                sys.stdout.write(extra_data)
            sys.stdout.write(data)
