from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os
import sys

# Path to your downloaded service account key
SERVICE_ACCOUNT_FILE = "uploader.json"

# Set the Drive API scope
SCOPES = ["https://www.googleapis.com/auth/drive"]

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

drive_service = build("drive", "v3", credentials=credentials)


# Upload a file
def upload_file(file_path, folder_id=None):
    file_metadata = {"name": os.path.basename(file_path)}

    if folder_id:
        file_metadata["parents"] = [folder_id]

    media = MediaFileUpload(file_path, resumable=True)

    uploaded_file = (
        drive_service.files()
        .create(body=file_metadata, media_body=media, fields="id")
        .execute()
    )

    print(f"Uploaded file ID: {uploaded_file.get('id')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_zip_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    folder_id = "1-eSpABx1mxWSiEGr_qolFiF2K5XTT3LT"  # Still hardcoded, or make it an arg too if you want

    upload_file(file_path, folder_id)
