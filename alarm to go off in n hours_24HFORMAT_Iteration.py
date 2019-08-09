h=int(input("How many hours until the alarm goes off?"))
while h<0:
        input("Time only moves forward, plase input a postive number:")
        h>=0
        D=int(h//24)
        hh=(h%24+14)%24
        print("The alarm is going off in",D,"day at",hh,":00.")




    
        

