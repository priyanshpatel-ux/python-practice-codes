t1 = (1, 2, 3, 4)
t2=()

l1=list(t1)

for  x in t1:
    l1.append(x*x)

t2=tuple(l1)

print(t2)