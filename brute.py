import requests
import re
import sys
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

def do_request(secret, value):
    # Put any cookies here
    cookies = {'PHPSESSID': 'asdf'}
    # POST or GET data goes here
    guess = b'asdf'
    data = {'key': guess}
    # Need any custom HTTP headers?
    headers = {'Host': 'localhost'}

    response = None
    retrycount = 0
    while retrycount < 10:
        try:
            # Perform the request, POST in this case
            r = requests.post('http://hack.me', cookies=cookies, data=data, headers=headers, timeout=1)
            break
        except requests.exceptions.Timeout:
            # A timeout occured, retry or fail?
            print(',', end='')
            sys.stdout.flush()
            retrycount += 1

    if r.status_code == 500:
        # Deal with this here or in the loop above...
        raise Exception("Server error")
    # Any other status codes need special treatment?

    # Extract whatever we need from the response
    result = re.search('Result: ([0-9]+\.[0-9]+)', response.text)
    if not result:
        raise Exception("Invalid response received: {}".format(response.text))

    value = float(result.group(1))

    return value

secret = []

# Use a ProcessPoolExecutor here if tasks are computationally expensive (bypass GIL)
with ThreadPoolExecutor(max_workers=12) as executor:
    while True:
        futures_to_value = {executor.submit(do_request, secret, v): v for v in range(256)}

        # we could also use concurrent.futures.wait() here, but this allows us to exit early if we detect that our previous guess was incorrect
        for future in as_completed(futures_to_value):
            val = future.result()

            # Do something with val and the future here
