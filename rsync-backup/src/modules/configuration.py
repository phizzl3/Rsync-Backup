"""
Configuration loading and defaults for the Rsync Backup app.

This module locates the app support directory, reads the JSON
configuration file when it exists, falls back to built-in defaults when
it does not, and exposes the resulting settings through a small
configuration object used by the rest of the application.
"""

from dataclasses import dataclass
from pathlib import Path

from .loadconfig import load_config

# App support paths used for persistent configuration and logging.
_APP_SUPPORT_DIR = Path().home() / "PyAppFiles" / "Rsync Backup"
_JSON = _APP_SUPPORT_DIR / "config.json"
_LOG_FILE = _APP_SUPPORT_DIR / "Backup_Log.txt"

# Default settings used when the JSON file is missing or incomplete.
_DEFAULTS = {
    "write log": True,
    "display progress details": True,
    "remove deleted files from destination": True,
}

# Load the saved settings, or fall back to the default values.
data = load_config(json_path=_JSON, default_data=_DEFAULTS)


@dataclass
class Config:
    """Container for the runtime configuration values used by the app."""

    write_log: bool
    display_progress_details: bool
    remove_deleted_files_from_destination: bool
    json_path: Path = _JSON
    log_file: Path = _LOG_FILE


# Create the shared configuration object for the rest of the program.
CONFIG = Config(
    write_log=data["write log"],
    display_progress_details=data["display progress details"],
    remove_deleted_files_from_destination=data["remove deleted files from destination"],
    json_path=_JSON,
    log_file=_LOG_FILE,
)
