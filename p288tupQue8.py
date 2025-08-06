t1 = (11, 22, 33, 44, 55)
n=int(input("Enter value="))

if n in list(t1):
    list(t1).remove(n)
    print(t1)
