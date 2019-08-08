h=int(input("How many hours until the alarm goes off?"))
if h>=0:
    D=int(h//24)
    hh=(h%24+14)%24
    print("The alarm is going off in",D,"day at",hh,":00.")
else:
    input("Time only moves forward, plase input a postive number:")
        

