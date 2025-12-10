f = open("prova111.txt","r")
print(f.read())
f.close()

with open("prova111.txt","r") as f:
    print(f.read())