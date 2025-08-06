f1=open("abc", 'r')
f2=open("pqr","w")

while True:
    ch=f1.read(1)
    
    if not ch:
        break


    if ch.isupper():
        f2.write(ch)
        print("",end="")
    else:
        print(ch,end="")

f1.close()
f2.close()