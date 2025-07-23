india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

c=input("Enter programming language= ")

if c in india:
    print("india")
elif c in pakistan:
    print("pakistan")
elif c in bangladesh:
    print("bangladesh")

else:
    print("not in the list")