print("Removing empty strings from a list")
list1=["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]
list2=[]
for i in list1:
    if i != "":
        list2.append(i)
list1=list2
print(list1)
