f1 = open("/Users/priyanshpatel/Downloads/abcde.txt", 'r')

#file location= "/Users/priyanshpatel/Downloads/abcde.txt", 'r'

while True:
    c = f1.read(1)

    if not c:
        print("End of file")
        break
    print(c)

f1.close()
