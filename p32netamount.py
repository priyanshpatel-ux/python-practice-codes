price=int(input("Enter Marked Price="))

if price> 10000:
    dis1=0.20
    afterdis1=price-dis1
    print("after discount",afterdis1)

elif price > 7000 and price <= 10000:
    dis2= 0.15
    afterdis2=price-dis2
    print("after discount",afterdis2)

elif price >= 7000:
    dis3 = 0.10
    afterdis3=price-dis3
    print("after discount",afterdis3)

else:
    dis4= 0.0
    afterdis4=price-dis4
    print("after discount",afterdis4)