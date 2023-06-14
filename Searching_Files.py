x=input("Enter file name")
try:
    
    with open(x,'r') as fhand:
        l=0
        for line in fhand:
            if(line.startswith("From") or line.startswith("from")):
                l+=1
                print(line.rstrip())
    print("Number of line: ",l)
except FileNotFoundError:
    print("Error opening the file")


