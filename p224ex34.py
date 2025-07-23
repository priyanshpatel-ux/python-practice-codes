list1=["cat", "dog", "elephant", "rat", "hippopotamus", "fox"]

c=0

for x in list1:
    if len(x)>3:
        print(x)
        c=c+1
print("count= ",c)
