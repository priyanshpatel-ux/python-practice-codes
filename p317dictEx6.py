students = {1: 33, 22: 34, 3: 18, 44: 45, 50: 20, 12: 30, 33: 25}
names = {1: "Ram", 22: "Jayul", 3: "Rahul", 44: "Anjali", 50: "Riya", 12: "Hiral", 33: "Karan"}

n=(input("Enter Name= "))
c=0
for k,v in names.items():
    if n==v:
        m=students[k]
        print("Name is",v," marks ",m, "rollno ",k)
        c=1
        break

if c==0:
    print("Not Found")