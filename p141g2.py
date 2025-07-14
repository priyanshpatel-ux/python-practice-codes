print("Number Guessing Game")
print("Guess a number between 1 and 10")
import random
random_integer = random.randint(1, 10)
c=0
y=1
n=0
while y!=n:
    y=int(input("Enter your guess ="))
    
    if y==random_integer:
        print("Correct")
        c=c+1
        break
    elif y>random_integer:
        print("Lower")
        c=c+1
    else:
        print("Higher")
        c=c+1

print("Counter = ",c)