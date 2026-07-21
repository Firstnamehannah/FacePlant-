"""Data model package for FacePlant."""

from pathlib import Path
from .faceplant import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "faceplant.yaml"
