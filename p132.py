#return

def square(x):
    return x * x

result = square(5)
print("Square is", result)


#position argument
def g(name, age):
    print("Hello", name, "you are", age, "years old.")

g("P", 21)

#keyword argument
g(age=21, name="P")
