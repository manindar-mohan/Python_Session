import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', required='True',
                    help='Enter the vulnerable url')

args = parser.parse_args()
url = args.url

response = requests.get(url)

# print(response.headers)

header_list = ['Server', 'Set-Cookie', 'Date', 'Via', 'X-Powered-By',
               'Connection', 'Content-Length', 'Content-Type', 'Host',
               'X-Content-Type-Options', 'X-XSS-Protection',
               'Strict-Transport-Security', 'Content-Security-Policy']


for header in header_list:
    try:
        result = response.headers[header]
        print('%s: %s' % (header, result), "\n")
    except Exception as error:
        print('%s: No Details Found' % header, "\n")
