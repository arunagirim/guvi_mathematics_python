n=int(input())
c=0
for i in range(1,n+1):
  temp=i
  r=0
  while(temp>0):
    d=temp%10
    r=r*10+d
    temp=temp//10
  if i==r:
    c+=1
print(c)
