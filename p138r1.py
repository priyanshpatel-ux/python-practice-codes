import random
c1=0
c2=0
n=int(input("Enter 1 for Add,\nEnter 2 for Sub \nEnter = "))

if n==1:
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

elif n==2:
    for i in range(1,6):
        random_integer1 = random.randint(1, 10)
        random_integer2 = random.randint(1, 10)
        print("Number 1 is",random_integer1)
        print("Number 2 is",random_integer2)

        c=int(input("Enter Sub =>"))

        if c==random_integer1-random_integer2:
            print("Correct")
            c1=c1+1
        else:
            print("Wrong")
            c2=c2+1


    print("Correct count : ",c1)
    print("Wrong count : ",c2)