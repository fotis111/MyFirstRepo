import random
sum1=100
sum2=0
sum3=0
n=0
z=0
x=random.randint(0,100)
y=int(input('mantepse arithmo'))
i=0
while n==0:
    if x==y:
        print('o arithmos einai %d ' %x)
        n=-1
    elif x>=(sum1+sum2)//2:
        z=(sum1+sum2)//2
        print('o arithmos einai isos h panw apo %d ' %((sum1+sum2)//2))
        y=int(input('dwse neo arithmo'))
        #sum3=z
        sum2=z
        
        
    elif x<=(sum1+sum2)//2:
        
        print('o arithmos einai katw apo %d ' %((sum1+sum2)//2))
        y=int(input('dwse neo arithmo'))
        
        sum1=(sum1+sum2)//2
        sum2=z
    else:
        print('o arithmos einai ',x)

    #print('o arithmos einai ',x)
    
