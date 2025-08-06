t1 = (11, 22, 33, 44, 55)
val = int(input("Enter value= "))

pos=t1.index(val)

if val in t1:
    print("Index of", val, "is:", pos)
else:
    print(val, "not found")