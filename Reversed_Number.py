def rev(n):
    r=int(str(n)[::-1])   
    return int(r)

def sum(x): 
    s=0
    while(x!=0):
        d=int(x%10)
        s+=d
        x=int(x/10)
    return s


n1=input("Enter a number")
r1=rev(n1)
print("Reversed num: ",r1)
print("Sum: ", sum(r1))








