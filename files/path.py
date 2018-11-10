#!/usr/bin/env python3
import os
path_testing = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(path_testing)
#print("Displaying current directory path")
current_path = os.getcwd()
print(current_path)
print ("Changing current dir")
chdir = os.chdir('/usr/lib/zabbix/externalscripts')
print(chdir)
abspath = os.path.abspath('test.py')
print ("Function will print current absolute path + 'abspath'")
