marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25
}

passing = 18
c1=0
c2=0

for k,v in marks.items():
    if v>=18:
        c1=c1+1

print("\nTotal Pass=",c1)
