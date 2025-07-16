import random
list1=[]
list2=[]
list3=[]

n=int(input("Enter limit =>"))

list1=[]
for i in range(1,n+1):
    y=random.randint(-20,10)
    list1.append(y)

print("Random List=",list1)

list2=[]
for x in list1:
    if x>=0:
        list2.append(x)
    else:
        list3.append(x)

print("Positive List=",list2)    
print("Negative List=",list3)