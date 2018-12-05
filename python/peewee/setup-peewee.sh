#!/bin/sh
# bash script to create peewee models corresponding to toy database

python3 -m pwiz -e sqlite "testDB.sqlite" > testmodels.py
