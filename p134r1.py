def max2(n,m):
    if n>m:
        return n
    else:
        return m

n=int(input("Enter no. 1="))
m=int(input("Enter no. 2="))
result = max2(n,m)
print("Greater Number =", result)