import math
a=raw_input("Enter an Number :- ")
ls=[]
b=0
e=0
if (int(a)<=1000000000):
   for i in range(0,len(a)):
       ls.append(int(a[i]))
       b=len(a)
else:
    pass
for i in range(0,len(ls)) :
   e+=math.pow(ls[i], b)
   
if (e==int(a)):
   print("Armstrong")
else:
   print("Not Armstrong")
