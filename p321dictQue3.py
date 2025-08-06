marks = {
    "ram": 33,
    "rahul": 45,
    "manav": 30,
    "jayul": 34,
    "meena": 29,
    "siddhi": 48
}
c=0
n=(input("Enter Name"))

for k in marks:
    if n==k:
        print("Yes, it exists")
        c=1
        break
if c==0:
    print("No it doesn't exists")
