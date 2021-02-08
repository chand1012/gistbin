import json
import os
import sys

import requests
from random_words import RandomWords


def safe_list_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None

def create_auth(username, token):
    user_home = os.environ.get("HOME")
    if user_home is None or 'win32' in sys.platform:
        user_home = os.environ.get("USERPROFILE")
        
    keyfile_dir = os.path.join(user_home, ".gistbin")
    keyfile_path = os.path.join(keyfile_dir, 'auth.json')
    while True:
        if os.path.exists(keyfile_dir):
            with open(keyfile_path, 'w') as keyfile:
                data = {
                    'username': username,
                    'key': token
                }
                keyfile.write(json.dumps(data))
            break
        else:
            os.makedirs(keyfile_dir)

def get_auth():
    user_home = os.environ.get("HOME")
    if user_home is None or 'win32' in sys.platform:
        user_home = os.environ.get("USERPROFILE")

    keyfile_dir = os.path.join(user_home, ".gistbin")
    keyfile_path = os.path.join(keyfile_dir, 'auth.json')
    auth = {}
    with open(keyfile_path) as keyfile:
        auth = json.loads(keyfile.read())
    return auth.get('username'), auth.get('key')

def create_gist(file_string, name=None, desc=None, public=True, verbose=False, raw=False):
    # this will create a gist
    # and print out the url
    url = 'https://api.github.com/gists'
    if name is None:
        rw = RandomWords()
        name = '_'.join(rw.random_words(count=3)) + '.txt'
    if desc is None:
        desc = 'Uploaded with Gistbin!'

    if verbose:
        print(name)
        print(desc)
    
    body = {
        'public': public,
        'files': {}
    }
    body['description'] = desc
    body['files'][name] = {'content': file_string}

    if verbose:
        print(f'Post Request Body:\n{body}')

    session = requests.Session()
    username, token = get_auth()
    
    session.auth = (username, token)
    session.headers = {'accept':'application/vnd.github.v3+json', 'User-Agent':'Gistbin'}

    response = session.post(url, json=body).json()

    if verbose:
        print('Github Response:')
        print(response)

    if raw:
        print(response['files'][name].get('raw_url'))
    else:
        gist_id = response.get('id')
        print(f'https://gist.github.com/{username}/{gist_id}')
    
    session.close()


def create_multi_gist(file_dict, desc=None, public=True, verbose=False):
    url = 'https://api.github.com/gists'

    if desc is None:
        desc = 'Uploaded with Gistbin!'

    if verbose:
        print(file_dict)
        print(desc)
    
    body = {
        'public': public,
        'desc': desc,
        'files': file_dict
    }

    if verbose:
        print(f'Post request body: {body}')
    
    session = requests.Session()
    username, token = get_auth()
    
    session.auth = (username, token)
    session.headers = {'accept':'application/vnd.github.v3+json', 'User-Agent':'Gistbin'}

    response = session.post(url, json=body).json()

    if verbose:
        print('Github Response:')
        print(response)
    
    gist_id = response.get('id')
    print(f'https://gist.github.com/{username}/{gist_id}')

    session.close()

def get_file_metadata(file_contents, verbose=False):
    comment_delimiters = ['#', '//', '--', '<!--']
    name = None
    description = None
    public = False
    if type(file_contents) == str:
        for line in file_contents.splitlines():
            if any(line.startswith(x) for x in comment_delimiters):
                if 'name:' in line:
                    index = line.index('name:')
                    name = line[index+5:].replace(' ', '')
                    if '-->' in name:
                        name = name.replace('-->', '')
                if 'desc:' in line:
                    index = line.index('desc:')
                    description = line[index+5:]
                    if '-->' in description:
                        description = description.replace('-->', '')
                if 'public:' in line:
                    if 'true' in line.lower():
                        public = True

    if verbose:
        print('Gotten metadata:')
        print(f'Name: {name}')
        print(f'Description: {description}')
        print(f'Public: {public}')
                
    return name, description, public