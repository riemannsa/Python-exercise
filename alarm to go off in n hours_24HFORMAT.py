
h=int(input("How many hours until the alarm goes off?"))

while h<0:
    h2=int(input("Time only moves forward, plase input a postive number:"))
    if h2<0:
        print ("No negative input accepted, program ends for repeatly invalid input.")
        break
    else:
        h=h2
        break

while h==0:
     print("The alarm goes off now.")
     break
    
while h>0:
    if h<=24:
        D=0
    else:
        D=int(h//24)
        
    hh=(h%24+14)%24
    print("The alarm is going off in",D,"day at",hh,":00.")
    break


    
   
      
   
        

