students = {1: 33, 22: 34, 3: 18, 44: 45, 50: 20, 12: 30, 33: 25}

roll = int(input("Enter Roll Number= "))
c=0

for k,v in students.items():
    if roll==k:
        print("Marks are=",v)
        c=1
        break

if c==0:
    print("Not Found")