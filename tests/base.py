import io
import os.path
from pathlib import Path
from typing import Any, Tuple

import yaml


def assert_yaml_dirs_equal(a: str, b: str) -> None:
    a_files = sorted(Path(a).rglob('*.yaml'))
    b_files = sorted(Path(b).rglob('*.yaml'))

    assert len(a_files) == len(b_files)

    for a_file, b_file in zip(a_files, b_files):
        a_data = _load_tuple_data(a_file)
        b_data = _load_tuple_data(b_file)

        for a_datum, b_datum in zip(a_data, b_data):
            assert a_datum == b_datum, f"""
            Got from {a}: {a_data}
            Expected from {b}: {b_data}
            """


def _load_tuple_data(file: Path) -> Tuple[Any, ...]:
    with file.open(encoding='utf-8') as f:
        content = f.read()
        replaced = content.replace('${PATH_SEPARATOR}', os.path.sep)
        buffer = io.StringIO(replaced)
        return tuple(yaml.safe_load_all(buffer))
