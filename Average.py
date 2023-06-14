l=list()
while(1):
    i=input("Enter number/ done")
    if(i=="done"):
        break
    else:
        l.append(float(i))
    

print(sum(l)/len(l))   
