import math

stocks = {
    "info": [600, 630, 620],
    "ril": [1430, 1490, 1567],
    "mtl": [234, 180, 160]
}

while True:
    print("Enter 1 for Print,\nEnter 2 for Add,\nEnter 3 for Exit")
    n = int(input("Enter = "))

    if n==1:
        for k, v in stocks.items():
            avg = sum(v) / len(v)
            print(k, "==>", v, "==> avg:", round(avg,2))
    
    elif n==2:
        name = input("Enter Name=")
        c=0
        for k,v in stocks.items():
            if k==name:
                c=1
            value=int(input("Enter value="))
            stocks[name]=value
            print("Added",stocks)    
        if c==0:
            print("Let's Enter it is not there ")
            value=int(input("Enter Value="))
            stocks[name]=value
            print("Added",stocks)    
    
    elif n==3:
        print("Exit")
        break