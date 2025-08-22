#Sum of Series...x+x^2+x^3..x^n
x=int(input("Enter Value of x : "))
n=int(input("Enter Value of n : "))
s=x
print(x,end=' + ')
for i in range(2,n+1):
    if i<n:
        print(str(x)+"^"+str(i),end=' + ')
    else:
        print(str(x)+"^"+str(i))
    s+=x**i
print("Sum of Series is:",s)
