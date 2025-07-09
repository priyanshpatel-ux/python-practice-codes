n=int(input("Enter Number =>"))
m=int(input("Enter Number =>"))
c=0
s=0

for i in range(1,n+1):
		if i%m:
			print(i)
			c=c+1
			s=s=i
print("Count:", c)
print("Sum:", s)