import random
c1=0
c2=0
for i in range(1,6):
    random_integer1 = random.randint(1, 10)
    random_integer2 = random.randint(1, 10)
    print("Number 1 is",random_integer1)
    print("Number 2 is",random_integer2)

    c=int(input("Enter add =>"))

    if c==random_integer1+random_integer2:
        print("Correct")
        c1=c1+1
    else:
        print("Wrong")
        c2=c2+1
    


print("Correct count : ",c1)
print("Wrong count : ",c2)