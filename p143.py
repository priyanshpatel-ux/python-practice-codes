import random
t= 0

print("Generated Numbers:")
for i in range(5):
    n=random.randint(1, 50)
    t=t+n
    print(n)
print("Sum= ", t)
