n=int(input("Enter Number =>"))
s1=0
s2=0
for i in range(1,n+1):
    if i%2==0:
        print(i*i,end=" + ")

    else:
        print(i*i*i,end=" + ")

        s1=s1+i*i
        s2=s2+i*i*i
print("\nSum = ",s1,s2)