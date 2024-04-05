str = "[[1,2,3],[3,4,5]]"
li = [[0]*3]*2
print(li)
print(len(li))
print(len(li[0]))


for i in range (len(li)):
    for j in range (len(li[0])):
        print(li[i][j],end=" ")
    print()

