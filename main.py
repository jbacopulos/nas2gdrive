from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

SCOPES = ["https://www.googleapis.com/auth/drive"]


def upload_file(file_path, folder_id=None):
    credentials = Credentials(
        None,
        refresh_token=os.getenv("REFRESH_TOKEN"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        scopes=os.getenv("SCOPES"),
    )

    credentials.refresh(Request())

    drive_service = build("drive", "v3", credentials=credentials)

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

    script_dir = Path(__file__).resolve().parent
    dotenv_path = script_dir / ".env"

    load_dotenv(dotenv_path=dotenv_path)
    upload_file(file_path, os.getenv("FOLDER_ID"))
