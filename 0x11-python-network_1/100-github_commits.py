#!/usr/bin/python3
"""
Write a Python script that takes 2
arguments in order to solve this challenge.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    response = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(argv[2], argv[1]))
    commits = response.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
