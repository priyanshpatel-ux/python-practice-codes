rep=int(input("Enter Sugar Level"))

if rep>=80 and rep<=100:
    print("Normal fasting Sugar level")

if rep<80 and rep<100:
    print("Low sugar Level")

if rep>100:
    print("High Sugar Level")