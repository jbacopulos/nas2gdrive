# NAS Backup to Google Drive

This project automates the process of backing up a NAS directory by zipping its contents and uploading the archive to Google Drive using the Google Drive API.

## Structure

- `main.py`: Python script to upload a given file to Google Drive.
- `backup.sh`: Bash script to zip the NAS folder and invoke the Python script.
- `.env`: Environment variables used by `backup.sh`.

## Requirements

- Python 3.8+
- `pip` installed
- A Google Cloud service account with a JSON key
- Google Drive API enabled for your project

## Installation

1. **Clone this repository** and navigate into it:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up the Python environment**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install google-api-python-client google-auth google-auth-oauthlib
   ```

3. **Prepare your `.env` file**:

   Create a `.env` file in the project directory:

   ```bash
   NAS_DIR="/path/to/your/nas"
   BACKUP_DIR="/path/to/your/backup_folder"
   PYTHON_SCRIPT="/path/to/this/project/main.py"
   ```

4. **Add your Google service account credentials**:

   - Download your service account JSON key from Google Cloud Console.
   - Save it as `uploader.json` in the project directory.

5. **Set up your Google Drive Folder ID**:

   - In `main.py`, update the `folder_id` variable with the ID of the Google Drive folder where you want to upload the backup.
   - Optionally, you can modify the script to pass `folder_id` as an argument instead of hardcoding.

## Usage

Instead of manually running the backup script, **schedule it using a cron job**.

1. **Make the `backup.sh` script executable**:

   ```bash
   chmod +x backup.sh
   ```

2. **Edit the user's crontab**:

   ```bash
   crontab -e
   ```

3. **Add the following line** to run the backup every 10 days at 2:00 AM:

   ```bash
   0 2 */10 * * /home/backupuser/nas2gdrive/backup.sh >> /home/backupuser/nas2gdrive backup.log 2>&1
   ```

   This will:
   - Execute the `backup.sh` script every 10 days at 2:00 AM.
   - Append output and errors to `backup.log` in the same directory.

## Example Directory Structure

```
.
├── .env
├── .venv/
├── backup.sh
├── backup.log
├── main.py
└── uploader.json
```

## Example `.env` file

```dotenv
NAS_DIR="/srv/dev-disk-by-uuid-xxx/NAS"
BACKUP_DIR="/home/backupuser/backups"
PYTHON_SCRIPT="/home/backupuser/nas2gdrive/main.py"
```

## Troubleshooting

- **Authentication errors**: Make sure the service account has access to the target Google Drive folder.
- **Missing modules**: Verify you activated the virtual environment and installed the required Python packages.
- **Permissions**: Ensure that `backup.sh` has execute permissions (`chmod +x backup.sh`).
- **Environment issues in cron**: Since cron jobs use a minimal environment, ensure that absolute paths are correctly specified in `.env` and scripts.
