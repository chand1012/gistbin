import argparse
import json
import os
import sys
from io import BytesIO

from lib import create_gist, create_auth

if __name__=='__main__':
    # args stuff
    parser = argparse.ArgumentParser(description="A commandline tool for GitHub Gists.")
    parser.add_argument('name', action='store_const', const='name', help='Gives your gist a name. Default is random.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enables verbose output.')
    parser.add_argument('desc', action='store_const', const='desc', help='Gives your gist a description.')
    parser.add_argument('--login', action='store_true', help='Login to GitHub Gists.')
    parser.add_argument('-p', '--private', action='store_false', help='Sets your Gist to private so only those with the link can see.')
    args = parser.parse_args()

    if args.login:
        username = input("Enter GitHub username: ").rstrip()
        key = input("Enter GitHub access token: ").rstrip()
        create_auth(username, key)
        print("Keyfile saved.")
    else:
        file_string = ''
        for line in sys.stdin:
            file_string += line + '\n'
        
        create_gist(file_string, name=args.name, desc=args.desc, public=args.private, verbose=args.verbose)
