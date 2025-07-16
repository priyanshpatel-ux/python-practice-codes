import random
list1=[]
n=int(input("Enter limit =>"))

list1=[]
for i in range(1,n+1):
    y=random.randint(1,20)
    list1.append(y)

print(list1)

