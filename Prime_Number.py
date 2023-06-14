from math import sqrt

def isPrime(n):
    f=1
    i=2
    if(n==0 or n==1): #corner case
        f=0
    if(n==2):
        f=1
    while(i<=sqrt(n)):
        if(n%i==0):
            f=0
        i+=1
    
    return f

f1=isPrime(int(input("Enter a number")))
if(f1==1):
    print("Prime number")
elif(f1==0):
    print("Not a prime number")




