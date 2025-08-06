marks = {
    "ram   ": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul ": 34,
    "jiya ": 16,
    "sadhana ": 11,
    "meena ": 19,
    "karan ": 20
}

passing = 18

print("Name","  Marks","  Result")

for k,v in marks.items():
    if v>=18:
        print(k," ", v,"    Pass")