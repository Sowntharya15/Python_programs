#sum of n natural numbers : 
def sum(a,n,s):
    if a>n:
        return 
    s=s+a
    sum(a+1,n,s)
    print(s)
sum(1,5,0)