#!/usr/bin/python3
"""Write a Python
script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request
    import urllib.parse
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
