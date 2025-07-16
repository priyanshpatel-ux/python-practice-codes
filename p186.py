import random
list1=[]
list2=[]
list3=[]

n=int(input("Enter limit =>"))

list1=[]
for i in range(1,n+1):
    y=random.randint(1,20)
    list1.append(y)

print(list1)

list2=[]
for x in list1:
    if x % 2 ==0:
        list2.append(x)
    else:
        list3.append(x)

print(list2)    
print(list3)