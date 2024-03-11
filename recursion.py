def printrec(a,n):
    if (a>n): 
        return
    print(a)
    printrec(a+1,n)
    print(a)
#printrec(1,3)


# print numbers from 1 to 3:
def reverse(a,n):
    if (n<a):
        return
    print(n)
    reverse(a,n-1)
#reverse(1,3)

# while loops :
# n=3
# i=1
# while(i<=n):
#     print(i)
#     i+=1

# n=5
# i=2
# while (n>=i):
#     print(n)
#     n-=1
    