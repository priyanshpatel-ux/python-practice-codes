n=int(input("Enter Number 1="))
m=int(input("Enter Number 2="))

for num in range(n, m):
    y = 0
    if num > 1:   
        for i in range(2,num):

            if num%i==0:
                y=1
                break

    if y==0:    
        print(num,end=" ")
