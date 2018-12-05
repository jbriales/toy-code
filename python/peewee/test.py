#!/usr/bin/env python3
# coding=utf-8
"""
Documentation
"""

from testmodels import *
import subprocess
import os


def main():
    for employee in Company.select():
        print(employee.id)
        print(employee.name)

    return True


if __name__ == '__main__':
    main()
