f1=open("abc", 'r')
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        pass
    else:
        print(ch,end="")
f1.close()

"""
1) vowels X
2) upper X
3) vowel ? other ?
4) upper? lower?
5) upper 7
6) vowel 9

"""