your = {
    "Clothes": 1100,
    "Shoes": 1000,
    "Watch": 900,
    "Mobile Recharge": 699,
    "Petrol": 1980
}

wife = {
    "Mobile Recharge": 799,
    "DTH recharge": 999,
    "Clothes": 2310,
    "Makeup": 3670,
    "Shoes": 999
}

t1 = sum(your.values())
t2 = sum(wife.values())

print("Your Total=", t1)
print("Wife's Total=", t2)

if t1 > t2:
    print("You are spending more")
elif t2 > t1:
    print("wife is spending more")
elif t1==t2:
    print("Both are equal.")

for x in your:
    if x in wife:
        if your[x] > wife[x]:
            print(x, "you spent more")
            print(your[x], "vs", wife[x])
        
        elif wife[x] > your[x]:
            print(x, "wife spent more")
            print(wife[x], "vs", your[x])
       
        else:
            print(x, "both spent the same")
            print(your[x])
