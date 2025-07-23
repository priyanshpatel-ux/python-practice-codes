list=[11, 44, 500, 22, 99, 11, 22, 66, 2]

n=int(input("Enter value= "))
c=0

for i in list:
    if i==n:
        c=c+1

        print("Appears",c)