"""

A script to quickly generate an archive command for Rsync.
Gets source directory and target directory via drag-and-drop.
Archives source directory and its contents into target directory.
(Optionally) adds a log file into the target directory with date 
and time of backup completion.

"""


from modules import (
    display_title,
    display_completed,
    get_target,
    get_source,
    run_rsync_command,
    clear_screen,
    write_backup_log,
)
from modules.configuration import CONFIG

# TODO UPDATE this to your desired version number
VERSION = "0.3.0"
"""Package version."""

# WRITE_BACKUP_LOG = Config.write_backup_log
"""Flag to write the backup log file to the target directory."""

clear_screen()
display_title(VERSION)

SOURCE = get_source()
TARGET = get_target()

run_rsync_command(SOURCE, TARGET)

display_completed(SOURCE, TARGET)

if CONFIG.write_logs:
    write_backup_log(SOURCE, TARGET)
