import csv
import json
import os

import requests

INPUT_CSV = 'data.csv'
LIST_ADDRESS = os.getenv('LIST_ADDRESS')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')


def udpate_mailing_list(mailing_list):
    return requests.post(
        f'https://api.mailgun.net/v3/lists/{LIST_ADDRESS}/members.json',
        auth=('api', MAILGUN_API_KEY),
        data={'upsert': True, 'members': json.dumps(mailing_list)}
    )


def main():
    with open(INPUT_CSV) as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)
        mailing_list = [{'address': row['E-mail:']} for row in reader]
    udpate_mailing_list(mailing_list)


if __name__ == '__main__':
    main()
