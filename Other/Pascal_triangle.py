ls=[]
for item in range(8):
        count = len(ls)
        ls = [1 if i == 0 or i == count else ls[i-1]+ls[i] for i in range(count+1)]
        print(ls)


