#Menu driven program using functions
def lenstr():
    j=input("enter the string whose lenght you want")
    print("the lenght of",j,"is",len(j))
    return
def palin():
    k=input("enter a string")
    j=k
    f=k[::-1]
    if(f==j):
        print("the given string is a palindome")
    else:
        print("it is not a palindrome")
    
  
    return
def upper():
    k=input("enter a string")
    f=k.upper()
    print("the sring in uppercase is ",f)
   
    return
def reverse():
    k=input("enter a straing")
    f=k[::-1]
    print("reverse of the string is ",f)
 
    return
choice=0
ch='y'
while(ch=="y"):
    print("Menu")
    print("Enter 1 to find the lenght of the given string")
    print("Enter 2 to check for palindromes ")
    print("Enter 3 to change to uppercase")
    print("Enter 4 to reverse the string")
    print("Enter 5 to Quit")
    choice=int(input("Enter your choice"))
    if(choice==1):
        lenstr()
    elif(choice==2):
        palin()
    elif(choice==3):
        upper()
    elif(choice==4):
        reverse()
    else:
        break
    ch=input("do you wish to continue y or n?")
