"""
Terminal display helpers for the Rsync Backup app.

This module centralizes the user-facing messages shown in the console,
including the startup banner, completion summary, and the confirmation
prompt for removing deleted files from the destination.
"""


def display_title(version) -> None:
    """Print the app banner shown at startup.

    Args:
        version (str): Package version displayed in the banner.
    """
    # Build the ASCII title string and print it to the terminal.
    title = f"""
    V{version}
    ██████╗ ███████╗██╗   ██╗███╗   ██╗ ██████╗      
    ██╔══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝      
    ██████╔╝███████╗ ╚████╔╝ ██╔██╗ ██║██║           
    ██╔══██╗╚════██║  ╚██╔╝  ██║╚██╗██║██║           
    ██║  ██║███████║   ██║   ██║ ╚████║╚██████╗      
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝      
    ██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
    ██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝
    ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
    ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                        :phiZzL3        
"""

    print(title)


def display_completed(source, target) -> None:
    """Show the final backup summary after a run completes.

    Args:
        source (Path): Path pointing to the source file or folder.
        target (Path): Path pointing to the destination folder.
    """
    # Print a simple completion summary for the user.
    print("=" * 65)
    print("\n Archive of:")
    print(f" {source}")
    print("\n Into:")
    print(f" {target}")
    print("\n Complete.")


def display_deleted_files_message() -> str:
    """Prompt the user before removing deleted files from the destination."""
    # Ask for confirmation and return the user's choice as lowercase text.
    choice = input(
        "\n Would you like to remove deleted files from the destination?\n NOTE: This cannot be undone. (y/n): "
    )
    if choice.lower() == "y":
        print("\n Deleted files from source will be removed from destination.\n")
    return choice.lower()
