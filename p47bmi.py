bmi=int(input("Enter BMI"))

if bmi<18.5:
    print("underweight")

if bmi<=18 and bmi<29:
    print("normal")

if bmi<=25 and bmi<29.9:
    print("overweight")

if bmi>=30:
    print("obese")
