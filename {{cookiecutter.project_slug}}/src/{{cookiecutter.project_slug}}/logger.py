import os
import logging

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO").upper())
logger = logging.getLogger("{{cookiecutter.project_slug}}")
