X,Y=map(int,input().split())
if (X+Y*2)%2 or (Y%2 and X<2):
    print('NO')
else:
    print('YES')