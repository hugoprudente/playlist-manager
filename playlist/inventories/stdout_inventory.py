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
                if format is not None and format:
                    try:
                        formatted = delimiter.join(
                            format.format(w) for w in line.values()
                        )
                    except Exception:
                        formatted = format.format(*tuple(line.values()))
                else:
                    formatted = delimiter.join(
                        "{0}".format(w) for w in line.values()
                    )

                sys.stdout.write(formatted)
                sys.stdout.write("\n")
        else:
            if extra_data is not None:
                sys.stdout.write(extra_data)
            sys.stdout.write(data)
