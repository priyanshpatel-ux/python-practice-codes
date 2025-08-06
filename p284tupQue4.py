t1 = (11, 22, 33, 44, 55)

n = int(input("Enter data= "))

l1 = list(t1)
l1.append(n)

t1 = tuple(l1)

print("Updated=", t1)