#!bin/sh

wget -O "data.csv" "https://docs.google.com/spreadsheets/d/${GDRIVE_DOCUMENT_ID}/export?format=csv&gid=${GDRIVE_SHEET_ID}"

python3 formatter.py

python3 mailing.py

cd /pelican
pelican -d content
