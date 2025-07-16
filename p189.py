import random
list1=[]
list2=[]
list3=[]

m=int(input("Enter limit =>"))

list1=[]
for i in range(1,m+1):
    y=random.randint(0,20)
    list1.append(y)
r=int(input("Enter Number=>")) 

for n in list1:
    if n>r:
        list2.append(n)

print(list1)
print(list2)