#!/usr/bin/env python3
# coding=utf-8
"""
Check syntactic sugar for different Python function calls
"""

import subprocess
import os


def foo(bar, quz, opt1='a def opt1 value', opt2='a def opt2 value'):
    print(bar)
    print(quz)
    print(opt1)
    print(opt2)


# Use function above with unpacked arguments
print('\nCall the usual way:')
foo('bar', 'quz')

d = {
    'quz': 'a quz value',
    'bar': 'a bar value',
    'opt1': 'a opt1 value',
    'opt2': 'a opt2 value',
}
print('\nCall with unpacked dict:')
foo(**d)

print('\nCall with explicit positional arguments:')
foo(bar='a bar value', quz='a quz value', opt1='a opt1 value')

print('\nCall with explicit positional arguments (changed order!):')
foo(quz='a quz value', bar='a bar value', opt1='a opt1 value')
foo(quz='a quz value', opt1='a opt1 value', bar='a bar value')

print('\nCall with implicitly ordered optional arguments:')
foo('a bar value', 'a quz value', 'a opt1 value', 'a opt2 value')
