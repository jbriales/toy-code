#!/usr/bin/env python2
# coding=utf-8

import traceback
from termcolor import colored


def print_green(str):
    print(colored(str, 'green'))


def print_red(str):
    print(colored(str, 'red'))


def test():
    # A normal string with no special characters, even if unicode, does well
    str_unicode_all_ascii = u"all ascii symbols"
    print("Write string with ascii only:")
    with open('test', 'w') as f:
        f.write(str_unicode_all_ascii)
        print_green("Succeeded writing: " + str_unicode_all_ascii)

    str_unicode_non_ascii = u"\u2192"
    print("Write string with unicode special characters:")
    with open('test', 'w') as f:
        try:
            f.write(str_unicode_non_ascii)
            print_green("Succeeded writing: " + str_unicode_non_ascii)
        except UnicodeEncodeError:
            print_red(traceback.format_exc(str_unicode_non_ascii))
            print_red("Failed writing: " + str_unicode_non_ascii)

    # Another option: Directly .encode('utf-8') or .decode('utf-8') where necessary
    print("Write string with unicode special characters, using explicit encode:")
    with open('test', 'wb') as f:
    # with open('test', 'w') as f:  # This fails, due to str type instead of unicode
        # NOTE: Writing mode needs to be byte here?
        try:
            f.write(str_unicode_non_ascii.encode('utf-8'))
            print_green("Succeeded writing: " + str_unicode_non_ascii)
        except UnicodeEncodeError:
            print_red(traceback.format_exc(str_unicode_non_ascii))
            print_red("Failed writing: " + str_unicode_non_ascii)


# Try native mode
print("Test native mode")
print("================")
test()
# Try compatibility mode
print("")
print("Test compatibility mode")
print("=======================")
from io import open
test()

