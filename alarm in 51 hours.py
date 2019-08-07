h = int (input("how many hours until the alarm goes off?")
D=(h-14)//24
H = int(h-14)%24
if H=0:
    print("The alarm go off in",D,"days at 2 pm")
    if H<=10:
        t= 14+H
        print("The alarm go off in",D,"days at",t,"pm")
    else:
        t=14+H-24
        print("The alarm go off in",D,"days at",t,"am")
