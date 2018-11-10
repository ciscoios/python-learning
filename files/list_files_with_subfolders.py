#!/usr/bin/python3
import os
for foldername, subfolders, filenames in os.walk('/tmp'):
    print('The folder is ' + foldername)
    print('The subfolders in ' + foldername + ' are: ' + str(subfolders))
    print('the filenames in ' + foldername + ' are: ' + str(filenames))
    print()

