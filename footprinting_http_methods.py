import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', required='True',
                    help='Enter the vulnerable url')

args = parser.parse_args()
url = args.url
method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']

for method in method_list:
    req = requests.request(method, url)
    print("\n", method, req.status_code, req.reason)

    if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
        print('Cross Site Tracing(XST) is possible')
