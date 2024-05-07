from logger import logging
from exception import CustomException


from pathlib import Path
from box import Box
import sys
import os
import yaml


def read_yaml(path: Path) -> Box:
    """
    Read YAML file and return data as Box object.

    Args:
    path (Path): Path to the YAML file.

    Returns:
    Box: Data from the YAML file as a Box object.

    Raises:
    CustomException: If an error occurs during reading the YAML file.
    """

    try:
        with open(path) as y_file:
            data = yaml.safe_load(y_file)
            if data is None:
                raise Exception("YAML file is empty or invalid.")
            else:
                logging.info(f"Reading {path} yaml file")
                return Box(data)
    except Exception as e:
        raise CustomException(e,sys)


def read_doc(path: Path) ->str:
    try:
        # Open text document
        with open(path, "r") as doc:
            doc_content = doc.read()

        return doc_content

    except Exception as e:
        raise CustomeException(e,sys)

if __name__ == "__main__":
    x = read_yaml(Path("config.yaml"))