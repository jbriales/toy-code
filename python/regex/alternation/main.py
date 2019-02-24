#!/usr/bin/env python2
# coding=utf-8
"""
Toy example for regex alternation
"""
import re


def main():
    list_strings = re.findall(r'(foo|bar)', r"foo quz")
    list_strings = re.findall(r'(foo|bar)', r"bar quz")
    list_strings = re.findall(r'(foo|bar)', r"foo bar quz")

    match = re.search(
        r'\b(a|the|one) reason(|s) (for|of)\b',
        "this is the reason for that"
    )
    print('Found: %s' % match.group())

    match = re.search(
        r'\b(a|the|one) reason(|s) (for|of)\b',
        "this is the reason for that"
    )
    print('Found: %s' % match.group())

    # Search and find after ' '
    match = re.search(
        r'(^| )the',
        "this is the reason for that"
    )
    print('Found: %s' % match.group())
    print('Captured group: \'%s\'' % match.group(1))

    # Search and find after '^'
    match = re.search(
        r'(^| )the',
        "the reason is"
    )
    print('Found: %s' % match.group())
    print('Captured group: \'%s\'' % match.group(1))

    re.sub(r'the', r'a', "this is the reason for that")

    re.sub(r'(^| )t:', r'\1title:', "t:for t: bar")


if __name__ == '__main__':
    main()
