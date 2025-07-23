india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

c1=input("Enter First City name= ")
c2=input("Enter Second City name= ")

if c1 in india and c2 in india:
    print("Both cities are in india")
elif c1 in pakistan and c2 in pakistan:
    print("Both cities are in pakistan")
elif c1 in bangladesh and c2 in bangladesh:
    print("Both cities are in bangladesh")

else:
    print("They don't belong to same country")