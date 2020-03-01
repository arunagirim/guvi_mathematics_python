from fractions import gcd
l=list(map(int,input().split()))
a=l.pop()
b=l.pop()
if gcd(a,b)==1:
  print(1)
else:
  print(0)
