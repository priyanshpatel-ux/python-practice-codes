n = int(input("Enter Number => "))
c=0

for i in range(1,n+1):
    if i%7==0:
        print(i)
        c=c+1

print("count : ",c)