import math
ls=[]
Arm_num=[]
e=0
en=input("Input the number of Digits : ")
if (int(en)<=22):
    y=math.pow(10,int(en))
    y0=math.pow(10,int(en)-1)
    for i in range(int(y0),int(y)):
        T=str(i)
        for i in range(0,len(T)):
            ls.append(int(T[i]))
            e+=math.pow(ls[i],len(T))
       
        ls.clear()
        if (int(T)==int(e)):
            print("Armstrong","==",int(e))
            Arm_num.append(int(e))
        else:
            print("Not")
        e=0
        
else:
    pass
print ("The Armstrong Numbers is :",Arm_num)
