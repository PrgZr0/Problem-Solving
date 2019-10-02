#@Anthor : Prog0Mohamed
#@Date : 12:00 AM - 1/10/2019
#@Info : Armstrong Number

import math
while(1):
   num=raw_input("Enter an Number :- ")
   ls=[]
   count=0
   result=0
   if (int(num)<=1000000000):
      for i in range(0,len(num)):
          ls.append(int(num[i]))
          count=len(num)
          result+=math.pow(ls[i], count)
      if (result==int(num)):
         print("Armstrong")
      else:
         print("Not Armstrong")
   else:
       pass
