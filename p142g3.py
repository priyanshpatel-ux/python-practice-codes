import random
print("Number Guessing Game")
print("Guess a number between 1 and 50")

random_integer = random.randint(1, 50)
c=0
y=0
n=1
st=1
ending=50
while y!=n:
    print("Your range",st," == ",ending)
    y=int(input("Enter your guess ="))
    c = c + 1
    
    if y==random_integer:
        print("Correct")
        break
    elif y>random_integer:
        print("Lower")
        ending=y

    elif y<random_integer:
        print("Higher")
        st=y
print("Counter = ",c)