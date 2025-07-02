age=int(input("Enter Age =>"))
gender=(input("Enter gender (M or F)=>"))
MS=(input("Enter marital status (Y or N)=>"))

if gender=='F':
    print("She will work only in urban areas")

elif gender=='M' and age>=20 and age<=40:
    print("He may work anywhere")

elif gender=='M' and age>=40 and age<=60:
    print("He will work in urban areas only")

else:
    print("Error")