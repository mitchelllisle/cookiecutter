import os
from glob import glob

from cookiecutter import main, utils


def test_default_project(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter('.', no_input=True, output_dir=testing_dir)
    assert utils.make_sure_path_exists(testing_dir) is True

    project_folder = os.listdir(testing_dir)
    assert project_folder == ['my_project']

    directory_contents = glob(f'{testing_dir}/{project_folder[0]}/*', recursive=True)

    for f in directory_contents:
        assert f.replace(f'{testing_dir}/{project_folder[0]}/', '') in expected_folders


def test_docs_are_ommited(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter(
        '.', no_input=True, output_dir=testing_dir, extra_context={'generate_docs': False}
    )
    assert utils.make_sure_path_exists(testing_dir) is True

    project_folder = os.listdir(testing_dir)
    assert project_folder == ['my_project']

    directory_contents = glob(f'{testing_dir}/{project_folder[0]}/*', recursive=True)

    assert f'{testing_dir}/{project_folder[0]}/docs' not in directory_contents


def test_entrypoint(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter(
        '.', no_input=True, output_dir=testing_dir, extra_context={'entrypoint': True}
    )
    assert utils.make_sure_path_exists(testing_dir) is True

    with open(f'{testing_dir}/my_project/pyproject.toml') as f:
        text = f.read()
        assert 'my_project = { callable = "my_project.__main__:main"}' in text


def test_no_entrypoint(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter(
        '.', no_input=True, output_dir=testing_dir, extra_context={'entrypoint': False}
    )
    assert utils.make_sure_path_exists(testing_dir) is True

    with open(f'{testing_dir}/my_project/pyproject.toml') as f:
        text = f.read()
        assert 'my_project = { callable = "my_project.__main__:main"}' not in text
