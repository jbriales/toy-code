#!/usr/bin/env python3
# coding=utf-8
"""
Toy example for Dropbox API
"""

import dropbox
from pathlib import Path

def main():
    path_token = Path.home() / '.config' / 'joplin' / 'TOKEN_corporate'
    with path_token.open('r') as f:
        token = f.read().strip()

    dbx = dropbox.Dropbox(token)
    dbx.users_get_current_account()

    path = ''
    files = dbx.files_list_folder(path=path)

    try:
        res = dbx.files_list_folder(path)
    except dropbox.exceptions.ApiError as err:
        print('Folder listing failed for', path, '-- assumed empty:', err)
        # return {}
    else:
        rv = {}
        for entry in res.entries:
            rv[entry.name] = entry

    pass


if __name__ == '__main__':
    main()
