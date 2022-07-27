import os
from glob import glob

from cookiecutter import main, utils


def test_default_project(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter('.', no_input=True, output_dir=testing_dir)
    assert utils.make_sure_path_exists(testing_dir) is True

    project_folder = os.listdir(testing_dir)
    assert project_folder == ['my_project']

    directory_contents = glob(f'{testing_dir}/{project_folder[0]}/*', recursive=True)

    assert all(
        [
            f.replace(f'{testing_dir}/{project_folder[0]}/', '') in expected_folders
            for f in directory_contents
        ]
    )


def test_docs_are_ommited(cookiecutter_config, expected_folders, testing_dir):
    main.cookiecutter(
        '.', no_input=True, output_dir=testing_dir, extra_context={'generate_docs': False}
    )
    assert utils.make_sure_path_exists(testing_dir) is True

    project_folder = os.listdir(testing_dir)
    assert project_folder == ['my_project']

    directory_contents = glob(f'{testing_dir}/{project_folder[0]}/*', recursive=True)

    assert f'{testing_dir}/{project_folder[0]}/docs' not in directory_contents
