age=int(input("Enter Age="))
gender=(input("Enter Gender="))
days=int(input("Enter No. Of Days="))

if age>=18 and age<30 and gender=='M':
    wage1=days*700
    print("700 Per Day",wage1)


elif age>=18 and age<30 and gender=='F':
    wage2=days*750
    print("750 Per Day",wage2)

elif age>= 30 and age<= 40 and gender=='M':
    wage3=days*800
    print("800 Per Day",wage3)


elif age>= 30 and age<= 40 and gender=='F':
    wage4=days*850
    print("850 Per Day",wage4)
