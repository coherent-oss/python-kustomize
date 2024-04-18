from pathlib import Path

import yaml


def assert_yaml_dirs_equal(a, b):
    a_files = sorted(Path(a).rglob('*.yaml'))
    b_files = sorted(Path(b).rglob('*.yaml'))

    assert len(a_files) == len(b_files)

    for a_file, b_file in zip(a_files, b_files):
        with open(str(a_file), encoding='utf-8') as f:
            a_data = tuple(yaml.safe_load_all(f))
        with open(str(b_file), encoding='utf-8') as f:
            b_data = tuple(yaml.safe_load_all(f))

        for a_datum, b_datum in zip(a_data, b_data):
            assert a_datum == b_datum, f"""
            Got from {a}: {a_data}
            Expected from {b}: {b_data}
            """
