f1=open("abc", 'r')
c1=0
c2=0
while True:
    ch=f1.read(1)
    
    if not ch:
        break
    
    if ch.isupper():
        c1+=1
    if ch.islower():
        c2+=1
    
f1.close()
print("Total upper characters are", c1)
print("Total lower characters are", c2)