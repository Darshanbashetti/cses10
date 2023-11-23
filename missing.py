n=int(input())
l=[int(i) for i in input().split()]
for i in range(1, n):
    if i in l:
        pass
    else:
        print(i)
        break