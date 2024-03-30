import json
from typing import Any, Dict


def load_config(filepath: str) -> Dict[str, Any]:
    """
    Load config from filepath.

    Parameters:
        filepath (str): Path to config file

    Returns:
        data (Dict[str, Any]): Config as dictionary
    """
    with open(filepath) as file:
        data: Dict[str, Any] = json.load(file)
    return data


def create_msg(header: str, msg: str) -> str:
    """
    Create a message to print to terminal.

    Parameters:
        header (str): Message header
        msg (str): Message to print

    Returns:
        (str): Formatted message
    """
    return f"=== {header} ===\n{msg}"
