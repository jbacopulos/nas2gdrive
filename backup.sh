#!/bin/bash

cd "$(dirname "$0")"

set -o allexport
source .env
set +o allexport

# Variables
ZIP_FILE="$BACKUP_DIR/nas_backup_$(date +%Y%m%d).zip"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Delete the oldest zip file in the backup directory
oldest_zip=$(ls -1t "$BACKUP_DIR"/*.zip 2>/dev/null | tail -n 1)
if [[ -n "$oldest_zip" ]]; then
  echo "Deleting oldest backup: $oldest_zip"
  rm "$oldest_zip"
fi

# Zip NAS contents
zip -r "$ZIP_FILE" "$NAS_DIR"

source .venv/bin/activate
python3 "$PYTHON_SCRIPT" "$ZIP_FILE"
