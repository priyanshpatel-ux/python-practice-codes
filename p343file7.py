f1=open("abc", 'r')
c1=0
c2=0
while True:
    ch=f1.read(1)
    if not ch:
         break
    if ch in ['a','e','i','o','u']:
         c1+=1
    if ch not in ['a','e','i','o','u']:
         c2+=1
f1.close()
print("Total vowels are",c1)
print("Total other characters are",c2)

