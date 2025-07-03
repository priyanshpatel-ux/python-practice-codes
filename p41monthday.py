month=int(input("Enter A Month Number"))
year=int(input("Enter Year"))

if month==1:
    print("Jan",year,'has 31 days')

elif month==2:

    if year %4 ==0:
        print("Feb",year,'has 28 days')
    else:
        print("Feb",year,'has 29 days')

elif month==3:
    print("March",year,'has 31 days')

elif month==4:
    print("April",year,'has 30 days')

elif month==5:
    print("May",year,'has 31 days')

elif month==6:
    print("June",year,'has 30 days')

elif month==7:
    print("July",year,'has 31 days')

elif month==8:
    print("Aug",year,'has 31 days')

elif month==9:
    print("Sept",year,'has 30 days')

elif month==10:
    print("Oct",year,'has 31 days')

elif month==11:
    print("Nov",year,'has 30 days')

elif month==12:
    print("Dec",year,'has 31 days')