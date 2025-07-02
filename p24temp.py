Temp=int(input("Enter a Temperature =>"))

if Temp<0:
    print("Freezing Atmosphere")

elif Temp>=0 and Temp<=10:    
    print("Very cold atmosphere")

elif Temp>=10 and Temp<=20:
    print("Cold Atmosphere")

elif Temp>=20 and Temp<=30:
    print("Normal Atmosphere")

elif Temp>=30 and Temp<=40:
    print("Hot atmosphere")

elif Temp>40:
    print("Very hot atmosphere")
