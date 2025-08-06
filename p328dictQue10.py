marks = {
    "ram": 33,
    "rahul": 45
}

name=(input("Enter Name="))
marks1=int(input("Enter Marks="))

dict = marks
marks[name] = marks1

print("New Marks=", dict)