#Diamond Hole Pattern
n=int(input("Enter the size of Pattern:"))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print("*",end=" ")
    for k in range(1,2*i-1):
        print(" ",end=" ")
    for l in range(n,i-1,-1):
        print("*",end=" ")
    print()
for i in range(n+1,1,-1):
    for j in range(0,n-i+2):
        print("*",end=" ")
    for k in range(2*i-1,3,-1):
        print(" ",end=" ")
    for l in range(0,n-i+2):
        print("*",end=" ")
    print()
