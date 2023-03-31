import json
from typing import Dict, List

import pytest

from cookiecutter import utils

TESTING_DIR = 'test_generated_projects'


@pytest.fixture()
def testing_dir() -> str:
    return TESTING_DIR


@pytest.fixture()
def cookiecutter_config() -> Dict:
    with open('cookiecutter.json') as f:
        config = json.load(f)
    return config


@pytest.fixture()
def expected_folders() -> List:
    folders = [
        'docker',
        'pytest.ini',
        'mkdocs.yaml',
        'Makefile',
        'tests',
        'docs',
        'README.md',
        'pyproject.toml',
        'setup.cfg',
        'src',
    ]
    return folders


@pytest.fixture(scope='function', autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""

    def remove_test_dir():
        utils.rmtree(TESTING_DIR)

    request.addfinalizer(remove_test_dir)
