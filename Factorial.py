def fact(n):
    if(n==0 or n==1):
        f=1
    else:
        f=n*fact((n-1))
    return f


print("Factorial= ", fact(int(input("Enter a number"))))