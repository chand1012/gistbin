import os
import json
import requests
from random_words import RandomWords


def safe_list_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None

def create_auth(username, token):
    keyfile_dir = os.path.join(os.environ.get("HOME"), ".gistbin")
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
            os.mkdir(keyfile_dir)

def get_auth():
    keyfile_dir = os.path.join(os.environ.get("HOME"), ".gistbin")
    keyfile_path = os.path.join(keyfile_dir, 'auth.json')
    auth = {}
    with open(keyfile_path) as keyfile:
        auth = json.loads(keyfile.read())
    return auth.get('username'), auth.get('key')

def create_gist(file_string, name=None, desc=None, public=True, verbose=False):
    # this will create a gist
    # and print out the url
    url = 'https://api.github.com/gists'
    if name is None:
        rw = RandomWords()
        name = '_'.join(rw.random_words(count=3)) + '.txt'
    if desc is None:
        desc = ''

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
    session.headers = {'accept':'application/vnd.github.v3+json', 'User-Agent':'Gistbin Python Application'}

    response = session.post(url, data=json.dumps(body)).text
    if verbose:
        print('Github Response:')
        print(response)
    response = json.loads(response)
    gist_id = response.get('id')

    print(f'https://gist.github.com/{username}/{gist_id}')

