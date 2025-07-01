mon=int(input("Enter monday's temperature =>"))
tue=int(input("Enter tuesday's temperature =>"))
wed=int(input("Enter wednesday's temperature =>"))
thu=int(input("Enter thursday's temperature =>"))
fri=int(input("Enter friday's temperature =>"))
sat=int(input("Enter saturday's temperature =>"))
sun=int(input("Enter sunday's temperature =>"))

total= mon + tue + wed + thu + fri + sat + sun
avg= total / 7

print("Total = ",total)
print("average = ",avg)