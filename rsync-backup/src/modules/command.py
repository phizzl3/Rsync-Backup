"""
Rsync command generation and execution helpers.

This module builds the shell command used to copy files with rsync,
optionally enabling delete and progress flags based on the user settings.
"""

import subprocess


def run_rsync_command(
    source, target, del_choice=None, display_progress_details=False
) -> None:
    """Build and run the rsync command for a backup operation.

    Args:
        source (Path): Path to the source file or folder to copy.
        target (Path): Path to the destination folder for the backup.
        del_choice (str, optional): User choice for the delete flag.
        display_progress_details (bool, optional): Whether to include
            rsync progress output.
    """
    # Escape spaces in paths so the shell command remains valid.
    source = str(source).replace(" ", "\\ ")
    target = str(target).replace(" ", "\\ ")

    # Start with no optional flags and enable them only when requested.
    del_flag = ""
    progress_flag = ""

    if del_choice == "y":
        del_flag = "--delete "
    if display_progress_details:
        progress_flag = "--progress "

    # Run the rsync command in the shell with the selected options.
    subprocess.run(
        f"rsync -av {progress_flag}{del_flag}{source} {target}/",
        shell=True,
        check=False,
    )
