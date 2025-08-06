marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19
}

n=(input("Enter Name Which u want to delete= "))

if n in marks:
    del marks[n]
    print("New Marks=", marks)