"""
Entry point for the Rsync backup workflow.

This module collects the source and destination paths via the helper
modules in this package, optionally asks about deleting files that no
longer exist in the source, runs the rsync backup command, and reports
completion. It can also write a timestamped backup log when enabled.
"""

from modules import (
    display_title,
    display_completed,
    display_deleted_files_message,
    get_target,
    get_source,
    run_rsync_command,
    clear_screen,
    write_backup_log,
    CONFIG,
)

VERSION = "1.0.0"
"""Package version."""

del_choice = None

# Show the startup screen before collecting user input.
clear_screen()
display_title(VERSION)

# Ask the user for the source and destination folders.
SOURCE = get_source()
TARGET = get_target()

# Optionally confirm whether deleted files should also be removed in the
# destination folder.
if CONFIG.remove_deleted_files_from_destination:
    del_choice = display_deleted_files_message()

# Run the backup operation with the chosen options.
run_rsync_command(
    SOURCE,
    TARGET,
    del_choice=del_choice,
    display_progress_details=CONFIG.display_progress_details,
)

# Report the result to the user.
display_completed(SOURCE, TARGET)

# Write a timestamped backup log when logging is enabled.
if CONFIG.write_log:
    write_backup_log(SOURCE, TARGET, log_file=CONFIG.log_file)
