#!/usr/bin/env python2
# coding=utf-8
"""
Toy example for an immutable nested dictionary via frozendict
Test use as a normal dictionary key
"""
from frozendict import frozendict

# A normal dictionary
a_dict = {
    'aa': 'foo1',
    'ab': 'foo2',
}
print(a_dict)
try:
    # A normal dictionary cannot be used as key (mutable -> unhashable)
    another_dict = {
        a_dict: 'bar'
    }
except TypeError:
    print("Caught ERROR: dict is unhashable")

# A frozen version of the dictionary above
a_dict_frozen = frozendict(a_dict)
print(a_dict_frozen)
# A frozen dictionary can be used as key in another dict (hashable)
another_dict = {
    a_dict_frozen: 'bar'
}  # This works (frozen is immutable)

# A nested dictionary
a_nested_dict = {
    'a': a_dict,
    'b': 'foo3',
    'c': {
        'ca': 4,
        'cb': 5.0
    }
}
a_nested_dict_frozen = frozendict(a_nested_dict)
try:
    a_nested_dict_frozen['b'] = 'bar3'
except TypeError:
    print("Frozen dict value cannot be modified as expected")
# Inner dicts in the frozendict can change! (mutable)
a_nested_dict_frozen['c']['ca'] = 'notsofrozen'
try:
    another_dict = {
        a_nested_dict_frozen: 'bar'
    }  # This works (frozen is immutable)
except TypeError:
    print("Caught ERROR: frozendict elements are mutable")
    print(type(a_nested_dict_frozen['a']))


# Implement a freeze method to freeze inner dicts recursively
def freeze(o):
    if isinstance(o, dict):
        return frozendict({key: freeze(value) for key, value in o.items()})
    # TODO: Deal with numpy and units as well
    return o


a_nested_dict_recursively_frozen = freeze(a_nested_dict)
another_dict = {
    a_nested_dict_recursively_frozen: 'bar'
}  # This works (frozen is immutable)
