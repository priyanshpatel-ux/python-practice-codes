count = {
    "china": 143,
    "india": 136,
    "usa": 32,
    "uk": 21
}

while True:
    print("Enter 1 for Print,\nEnter 2 for Add,\nEnter 3 for Remove,\nEnter 4 for Query,\nEnter 5 for Exit")
    n=int(input("Enter="))

    if n==1:
        for k,v in count.items():
            print(k,"==>",v) 
        
    if n==2:
        name = input("Enter Name=")
        c=0
        for k,v in count.items():
            if k==name:
                c=1
                print("Already exist")
                break
        if c==0:
            print("Let's Enter it is not there ")
            value=int(input("Ente population"))
            count[name]=value
            print("Added",count)
            
    elif n == 3:
        name = input("Enter Name to Remove = ")
        c = 0
        for k in count:
            if k == name:
                c = 1
                del count[name]
                print("Removed. New List =", count)
                break
        if c == 0:
            print("Country not found")

    elif n == 4:
        name = input("Enter Name to Query = ")
        c = 0
        for k, v in count.items():
            if k == name:
                c = 1
                print("Population of", name, "=", v)
                break
        if c == 0:
            print("Country not found")
    
    elif n == 5:
        print("Exit")
        break

    else:
        print("Only Enter 1,2,3,4,5")

