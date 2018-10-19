#!/usr/bin/env python2
# coding=utf-8
"""
Find key with maximum value in dictionary
"""

d = {
    'a': 1.0,
    'b': 2.0,
    'c': 3.0
}

for key in d:
    print key

# Explanation:
# max(*args, key=fun) finds max by taking the `arg` in the list `*args`
# that maximizes fun(arg)
# Since expanding a dictionary with *d returns a list of its keys,
# we need a key fun that returns the actual numerical value for each key (read the dict)
key_max = max(d, key=lambda key: d[key])
print("Key with max value: %s -> %f" % (key_max, d[key_max]))
