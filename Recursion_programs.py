#sum of n natural numbers : 
def sum(n):
    if (n<=1):
        return n
    return n + sum(n - 1)
# print(sum(5))

# factorial of a number using while loop:
# n=5
# fact=1
# i=1
# while (i<=n):
#     fact = fact * i
#     i+=1
# print(fact)

# factorial using recursion :
def factorial(n):
    if (n==0):
        return 1
    return n * factorial(n-1)
#print(factorial(5))

#fibonocci using while loop:
# n=5
# a=0
# b=1
# print(a,b,end=" ")
# i = 2
# while(i <= n):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c
#     i += 1

# fibonocci using recursion :
def fibonocci(n):
    if n <= 1:
        return n
    return fibonocci(n-1) + fibonocci(n-2)
n=5
for i in range(n+1):
    print(fibonocci(i),end=" ")


    