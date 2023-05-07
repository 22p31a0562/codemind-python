def gcd_find(list):
     result=list[0]
     for x in list[1:]:
         if result<x:
             res=result
             result=x
             x=res
         while x!=0:
             res=x
             x=result%x
             result=res
     return result
n=int(input())
list1=list(map(int,input().split()))
print(gcd_find(list1))
