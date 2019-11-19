import re
f=open('try')
for i in f:
    a=re.findall('(\S+)\s+(.*)()()',i)
    print(a)