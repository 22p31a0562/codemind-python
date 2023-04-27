p,r,t=map(int,input().split())
c=p*(pow((1 + r / 100), t))
a=format(c,".2f")
print(a)
