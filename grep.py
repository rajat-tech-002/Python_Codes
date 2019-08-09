import sys

l=sys.argv[1:]
print('\n')
for file_name in l:
    f=open(file_name)
    print('Printing :',file_name,'\n')
    for line in f:
        print(line)
    print('\n')    
        
       