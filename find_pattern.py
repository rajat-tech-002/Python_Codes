import re
import sys

l=sys.argv[1:len(sys.argv)-1]
pattern =sys.argv[-1]

print(l)
print(pattern)

for file_name in l:
    f=open(file_name)
    print('Inside File: ', file_name )
    for line in f:
        if pattern in line:
            print(line)