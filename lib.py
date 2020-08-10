import requests

def safe_list_get(l, index):
    try:
        return l[index]
    except IndexError:
        return None

def create_gist(buffer):
    # this will create a gist
    # and print out the url