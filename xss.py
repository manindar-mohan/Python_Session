import mechanize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', required='True',
                    help='Enter the vulnerable url')
# url = "http://testphp.vulnweb.com/"
args = parser.parse_args()
url = args.url

browser = mechanize.Browser()
with open('xss_payloads.txt') as f:
    for line in f:
        print(line)
        browser.open(url)
        browser.select_form(nr=0)
        browser["searchFor"] = line
        res = browser.submit()
        content = res.read()

        #  check the attack vector is printed in the response.

        x = str(content, 'UTF-8').find(line)
        if x > 0:
            print("Possible XSS is found")
        else:
            print("Test case failed")
