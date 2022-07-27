import logging
import os
import shutil

logging.basicConfig(level=os.environ.get('LOG_LEVEL', 'INFO').upper())
logger = logging.getLogger(__name__)


def remove_paths() -> None:
    """Remove paths if generate_docs is False

    If you ask cookiecutter to generate docs then we will generate a docs/ folders with
    the necessary doc structure as well as mkdocs.yaml and requirements for docs. When it is set
    to False this function will run to remove all folders/files associated with the docs
    Returns:

    """
    paths = [
        '{%- if cookiecutter.generate_docs == "False" -%} docs {% endif %}',
        '{%- if cookiecutter.generate_docs == "False" -%} requirements/docs.txt {% endif %}',
        '{%- if cookiecutter.generate_docs == "False" -%} mkdocs.yaml {% endif %}',
    ]

    logger.debug(f'there are {len(paths)} to remove')
    for path in paths:
        logger.debug(f'removing {path}')
        path = path.strip()
        if path and os.path.exists(path):
            if os.path.isdir(path):
                logger.debug(f'removing {path} as folder')
                shutil.rmtree(path)
            else:
                logger.debug(f'removing {path} as file')
                os.remove(path)


if __name__ == '__main__':
    remove_paths()
