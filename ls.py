import sys
import os
from os.path import getsize

l=sys.argv[1:]

for file_name in l:
    dirpath = os.path.abspath(file_name)

    print('File Name = ',file_name,',','Size = ',getsize(dirpath)," Bytes")  
