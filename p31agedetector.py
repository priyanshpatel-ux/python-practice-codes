age=int(input("Enter Age="))

if age>=0 and age<=12:
    print("Child")

elif age>=13 and age<=19:
    print("teenager")

elif age>=20 and age<=64:
    print("adult")

elif age>=65:
    print("senior")