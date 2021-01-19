#!bin/sh

curl -L -o "data.csv" "https://docs.google.com/spreadsheets/d/${GDRIVE_DOCUMENT_ID}/export?format=csv&gid=${GDRIVE_SHEET_ID}"

python3 formatter.py

members=$(cat members.json)

curl -s --user "api:${MAILGUN_API_KEY}" \
    https://api.mailgun.net/v3/lists/${LIST_ADDRESS}/members.json \
    -F upsert=true \
    -F members="$members"

cd /pelican
pelican -d content
