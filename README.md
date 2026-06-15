# Rsync-Backup

Rsync-Backup is a small macOS/Linux utility for running rsync-based backups from a simple drag-and-drop workflow. It asks for a source path and a destination folder, optionally confirms whether deleted files should also be removed from the destination, and then runs the rsync command for you.

## What the app does

- Accepts the source file or directory and the destination folder by dragging them into the terminal window.
- Uses rsync with the standard archive flags and optional progress output.
- Optionally removes deleted files from the destination when you confirm that behavior.
- Optionally writes a timestamped backup log entry after the copy completes.

## Requirements

- rsync must be installed and available on your PATH.
- Python 3 is required to run the script directly.
- The project also includes PyInstaller support for packaging the app into a standalone executable.

## How to use it

1. Run the entry point from the project root or the src folder:

   ```bash
   python rsync-backup/src/rsync_backup.py
   ```

2. Drop the source file or directory into the terminal window when prompted.
3. Drop the destination folder when prompted.
4. If the app is configured to ask about deleted files, confirm whether you want deleted items removed from the target directory.
5. The backup runs, a completion message is shown, and a log entry may be written if logging is enabled.

## Current behavior and options

The current app flow is implemented in the main entry file and helper modules:

- The startup screen is shown first.
- The source and destination paths are collected via drag-and-drop.
- The optional delete behavior is prompted only when the config setting allows it.
- The rsync command runs using the selected options.
- A completion message is displayed after the backup finishes.
- If logging is enabled, the backup log file is appended with the source, target, and timestamp.

## Helper files that are written automatically

The app stores helper files in the user support directory:

- macOS/Linux: ~/PyAppFiles/Rsync Backup/

The following files are created or used there:

### 1. config.json

Location:

```text
~/PyAppFiles/Rsync Backup/config.json
```

Purpose:

- Stores the app settings used at runtime.
- If the file does not exist, the app creates it automatically using default values.

Default settings written to the file:

```json
{
  "write log": true,
  "display progress details": true,
  "remove deleted files from destination": true
}
```

How to update it:

- Open the file in a text editor.
- Change the boolean values to match your preferred behavior.
- Keep the JSON valid: use double quotes, commas, and proper brackets.
- Save the file and restart the app.

If you want to restore the defaults, delete the existing config.json file and run the app again. The application will recreate it with the built-in defaults.

### 2. README.txt

Location:

```text
~/PyAppFiles/Rsync Backup/README.txt
```

Purpose:

- Explains the configuration file and how to customize it.
- This file is generated alongside config.json when the file is first created.

How to use it:

- Read it for guidance if you are unsure about the JSON fields.
- You can update it manually if you want to keep your own notes, but the app does not depend on it for runtime behavior.

### 3. Backup_Log.txt

Location:

```text
~/PyAppFiles/Rsync Backup/Backup_Log.txt
```

Purpose:

- Records each backup run in append-only format.
- Each entry includes the source path, destination path, and completion date/time.

How to use it:

- Leave it in place to keep a running history of backups.
- Open it at any time to review previous backup runs.
- Clear the file manually if you want to start a fresh log.
- The log is only written when the application setting for logging is enabled.

## Notes about the configuration options

The configurable values are:

- write log: turn backup logging on or off.
- display progress details: show rsync progress output during the run.
- remove deleted files from destination: allow the app to ask whether deleted source files should also be removed from the target.

## PyInstaller build info

To build a standalone executable:

```bash
pyinstaller -F -n "Rsync Backup" rsync-backup/src/rsync_backup.py
```

If you want to package the app for distribution, make sure rsync is available in the target environment as well.
