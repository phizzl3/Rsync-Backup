"""
* This is a sample configuration module for loading JSON data *

This module loads configuration data from a JSON file,
applies default values if the file is not found,
and processes the data to generate a configuration dictionary for import.

Modify this module to use loadconfig.py to suit your needs in loading your
configuration data.
"""

from dataclasses import dataclass
from pathlib import Path

# TODO Import the load_config function from its relative path
from .loadconfig import load_config

# TODO Update to your desired JSON file location
JSON = Path().home() / "PyAppFiles" / "Rsync Backup" / "config.json"

# TODO Update to your Default values for your JSON data
DEFAULTS = {
    "write logs": True,
    "display progress details": True,
    "remove deleted files from destination": False,
}

# Load (or set defaults) config json data
data = load_config(json_path=JSON, default_data=DEFAULTS)

# TODO Work with the JSON data to generate your configuration values
# important_number = data["write logs"] ** 2
# working_dir = data["working folder name"]
# file_name = data["output file name"].lower()

# TODO Update this formatted config data (Import this)
# CONFIG = {
#     "write logs": data["write logs"],
#     "display progress details": data["display progress details"],
#     "remove deleted files from destination": data["remove deleted files from destination"],
# }

@dataclass
class Config:
    write_logs: bool
    display_progress_details: bool
    remove_deleted_files_from_destination: bool
    
CONFIG = Config(
    write_logs=data["write logs"],
    display_progress_details=data["display progress details"],
    remove_deleted_files_from_destination=data["remove deleted files from destination"]
)


# TODO Or just load the config JSON data without modification (OR Import this)
# CONFIG2 = load_config(json_path=JSON, default_data=DEFAULTS)

# Example usage/test of the configuration data
if __name__ == "__main__":
    print("CONFIG:", CONFIG)
    # print("CONFIG2:", CONFIG2)
