import random
c1=0
c2=0
for i in range(1,6):
        random_integer1 = random.randint(1, 10)
        random_integer2 = random.randint(1, 10)
        print("Number 1 is",random_integer1)
        print("Number 2 is",random_integer2)

        c=random.randint(1,3)

        if c==1:
            n=int(input("Enter Add =>"))
            if n==random_integer1+random_integer2:
                print("Correct")
                c1=c1+1
            else:
                print("Wrong")
                c2=c2+1
        elif c==2:
            n=int(input("Enter Sub ="))
            if n==random_integer1-random_integer2:
                print("Correct")
                c1=c1+1
            else:
                print("Wrong")
                c2=c2+1
        elif c==3:
            print("Enter Mul Answer")
            n=int(input("Enter Mul ="))
            if n==random_integer1*random_integer2:
                print("Correct")
                c1=c1+1
            else:
                print("Wrong")
                c2=c2+1
       
print("Correct count : ",c1)
print("Wrong count : ",c2)