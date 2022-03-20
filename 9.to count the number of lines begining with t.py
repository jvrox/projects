f=open(r"D:\backup nov 2018 lenovo backup\nov2018 lenovo\lenovo backup\JIYA VERMA\Python\testfile.txt","r")
f2=f.readlines()
print(f2)
p=0
k=0
for i in f2:
    if i[0]=='t'or i[0]=='T':
        p=p+1
   
print(p)

f.close()
