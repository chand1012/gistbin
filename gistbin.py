import sys
import json
import os
from io import BytesIO
from lib import safe_list_get, create_gist

if __name__=='__main__':
    if safe_list_get(sys.argv, 1) == 'login':
        key = input("Enter GitHub access token: ").rstrip()
        keyfile_dir = os.path.join(os.environ.get("HOME"), ".gistbin")
        keyfile_path = os.path.join(keyfile_dir, 'auth.json')
        while True:
            if os.path.exists(keyfile_dir):
                with open(keyfile_path, 'w') as keyfile:
                    data = {
                        'key':key
                    }
                    keyfile.write(json.dumps(data))
                break
            else:
                os.mkdir(keyfile_dir)
        print("Keyfile saved.")
    else:
        file_buffer = BytesIO()
        lines = []
        for line in sys.stdin:
            lines += [line]
        with open(file_buffer, 'w') as input_file:
            for line in lines:
                input_file.write(line)
        create_gist(file_buffer)
