
x=input("Enter file name")
try:
    
    with open(x,'r') as fhand:
        l=0
        dict={}
        for line in fhand:
            line=line.rstrip()
            
            line=line.lower()
            for word in line.split():
                dict[word]=dict.get(word,0)+1
            
        print(dict)
    
except FileNotFoundError:
    print("File not found")
