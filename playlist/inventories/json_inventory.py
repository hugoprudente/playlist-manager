import io
import json
import sys
from pathlib import Path

import jmespath


class JSONInventory:
    def write_file(
        self,
        file_path,
        data,
        extra_data=None,
        fields=None,
        format=None,
        merge=True,
    ):
        # raw data
        local_data = data

        file_path = Path(file_path)
        if file_path.exists() and merge:  # pragma: no cover
            with io.open(str(file_path)) as open_file:
                sys.stdout.write("merge")
                sys.stdout.write("\n")
                # object_merge(json.load(open_file), file_data)

        with io.open(
            str(file_path),
            "w",
        ) as open_file:
            json.dump(local_data, open_file)

    def stdout(self, data, extra_data=None, fields=None, format=None):
        if fields is not None and fields:
            expression = jmespath.compile(fields)
            sys.stdout.write(json.dumps(expression.search(data)))
            sys.stdout.write("\n")
        else:
            if extra_data is not None:
                sys.stdout.write(json.dumps(extra_data))
                sys.stdout.write("\n")
            sys.stdout.write(json.dumps(data))
            sys.stdout.write("\n")
