f=open(r"D:\backup nov 2018 lenovo backup\nov2018 lenovo\lenovo backup\JIYA VERMA\Python\testfile.txt","r")
f2=f.read()
c=0
for i in f2:
    if i=='a' or i=='e' or i=='i'or i=='o'or i=='u':
        c=c+1
print(c)

