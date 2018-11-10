#!/usr/bin/python3
import os

for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)
        #dry-run (below)
        print(filename)
