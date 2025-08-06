f1=open("abc", 'r')
f2=open("pqr","w")

while True:
    ch=f1.read(1)
    
    if not ch:
        break
    f2.write(ch)

f1.close()
f2.close()
print("Copied")

"""
1->2 space X

1->2 vowel X

1->2 upper X

1->2 upper
 ->3 lower

1->2 vowel
 ->3 other

"""