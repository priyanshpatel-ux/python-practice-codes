n=int(input("Enter Number =>"))
c1=0
s1=0
c2=0
s2=0

for i in range(1,n+1):

    if i%2==0:
        c1=c1+1
        s1=s1+i
        print(i,"is EVEN")
    else:
        c2=c2+1
        s2=s2+i
        print(i,"is ODD")

print("Even count is",c1,"and the sum is",s1)
print("Odd  count is",c2,"and the sum is",s2)


