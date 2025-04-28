#!/bin/bash

set -o allexport
source .env
set +o allexport

# Variables
ZIP_FILE="$BACKUP_DIR/nas_backup_$(date +%Y%m%d).zip"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Zip NAS contents
zip -r "$ZIP_FILE" "$NAS_DIR"

# Run your Python script with the zip file as an argument
python3 "$PYTHON_SCRIPT" "$ZIP_FILE"
