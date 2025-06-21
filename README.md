# NAS Backup to Google Drive

This project automates the process of backing up a NAS directory by zipping its contents and uploading the archive to Google Drive using the Google Drive API.

## Structure

- `main.py`: Python script to upload a given file to Google Drive.
- `backup.sh`: Bash script to zip the NAS folder and invoke the Python script.
- `.env`: Environment variables used by `backup.sh` and `main.py`.

## Requirements

- Python 3.8+
- `pip` installed
- Google OAuth Credentials
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
   pip install google-api-python-client google-auth google-auth-oauthlib python-dotenv
   ```

3. **Prepare your `.env` file**:

   Create a `.env` file in the project directory:

   ```bash
   NAS_DIR="/path/to/your/nas"
   BACKUP_DIR="/path/to/your/backup_folder"
   PYTHON_SCRIPT="/path/to/this/project/main.py"
   CLIENT_ID="YOUR GOOGLE OAUTH CLIENT ID"
   CLIENT_SECRET="YOUR GOOGLE OAUTH CLIENT SECRET"
   REFRESH_TOKEN="YOUR GOOGLE OAUTH REFRESH TOKEN"
   FOLDER_ID="THE GOOGLE DRIVE FOLDER TO SAVE BACKUPS"
   ```

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
   0 2 */10 * * /home/backupuser/nas2gdrive/backup.sh >> /home/backupuser/nas2gdrive backups.log 2>&1
   ```

   This will:
   - Execute the `backup.sh` script every 10 days at 2:00 AM.
   - Append output and errors to `backups.log` in the same directory.

## Example Directory Structure

```
.
├── .env
├── .venv/
├── backup.sh
├── backups.log
└── main.py
```

## Example `.env` file

```dotenv
NAS_DIR="/srv/dev-disk-by-uuid-xxx/NAS"
BACKUP_DIR="/home/backupuser/backups"
PYTHON_SCRIPT="/home/backupuser/nas2gdrive/main.py"
CLIENT_ID="291527076548-asdfasdfasdfasdfasdfasdf.apps.googleusercontent.com"
CLIENT_SECRET="GOCSPX-asdfasdfasdfasdfasdf-Oe9r1"
REFRESH_TOKEN="1//asdfasdfasdfasdfasdf-L9IrqyA-asdfasdfasdfasdfasdfasdfasdf-R8"
FOLDER_ID="1-asdfasdfasdfasdfasdfasdf"
```

## Troubleshooting

- **Missing modules**: Verify you activated the virtual environment and installed the required Python packages.
- **Permissions**: Ensure that `backup.sh` has execute permissions (`chmod +x backup.sh`).
- **Environment issues in cron**: Since cron jobs use a minimal environment, ensure that absolute paths are correctly specified in `.env` and scripts.
