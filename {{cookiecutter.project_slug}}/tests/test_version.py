import re

from {{cookiecutter.project_slug}} import __version__


def test_version():
    match = re.search(r'^\d+\.\d+\.\d+$', __version__)
    assert match is not None
