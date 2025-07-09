print("5 KM Race")


for i in range(1,6):    
    print("You have completed",i,"KM")
    
    n=(input("are you tired? \n Enter="))
    if n=='no' and i==5:
        print("Congratulations You Have completed The Race")

    elif n=="yes":
        print("You didn't finish the race")
        break
 