#Cross Diagram
n=int(input("Enter the size of Diagram:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or j==n+1-i or i==n or j==n or i==1 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
