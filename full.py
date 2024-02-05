a=[10,2,4,5,7,8,9]
b=int(input("Enter number : "))
c=[]
for i in a:
    for j in a:
        if j==i:
            continue
        else:
            c=i+j
            if b==c:
                print(c,i,j)
            else:
                continue
    