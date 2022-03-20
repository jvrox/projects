f=open(r"D:\backup nov 2018 lenovo backup\nov2018 lenovo\lenovo backup\JIYA VERMA\Python\testfile.txt","r")
f2=f.read()
p=0
k=0
for i in f2:
    if i.isupper():
        p=p+1
    elif i.islower():
        k=k+1
    else:
        pass
print(p)
print(k)
f.close()
    
