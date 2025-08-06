students = {1: 33, 22: 34, 3: 18, 44: 45, 50: 20, 12: 30, 33: 25}
passing = 30
c1=0
c2=0
n=int(input("Enter: \n1 For Pass \n2 For Fail \n3 For Both \nEnter="))

for k,v in students.items():
    if n==1:
        if v>=30:
            c1=c1+1
            print(k,"Pass")

    elif n==2:
        if v<30:
            c2=c2+1
            print(k,"Fail")

    elif n==3:
        if v>=30:
            c1=c1+1
            print(k,"Pass")
        elif v<30:
            c2=c2+1
            print(k,"Fail")

print("\nTotal Pass=",c1)
print("\nTotal Fail=",c2)
