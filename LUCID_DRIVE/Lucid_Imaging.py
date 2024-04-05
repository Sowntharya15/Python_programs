n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=i
even=0
for i in range(n):
    if i%2==0:
        even+=i
a=sum-even
if a in l:
    l.remove(a)
    print(l)
else:
    print("No element to remove")









            






    
    
    