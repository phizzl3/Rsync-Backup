"""
Backup-log writing helpers for the Rsync Backup app.

This module appends a timestamped entry to the backup log file so each
run records the source and destination paths together with the completion
date and time.
"""

from pathlib import Path
from datetime import datetime


def write_backup_log(source, target, log_file) -> None:
    """Append a completion entry to the backup log file.

    Args:
        source (Path): Path to the source file or folder that was backed up.
        target (Path): Path to the destination folder that received the backup.
        log_file (Path): File where the log entry should be appended.
    """
    # Capture the current timestamp for the log entry.
    date_time = datetime.now()
    current_date_time = date_time.strftime("%m/%d/%Y - %H:%M")

    # Format the entry with the source, target, and completion time.
    log_entry = f"[{source}] -> [{target}] - Complete - {current_date_time}\n"

    # Append the log record to the configured backup log file.
    with open(log_file, "a", encoding="utf-8") as text:
        text.write(log_entry)
