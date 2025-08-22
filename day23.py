#Sum of Series...x+x^n/x!
x=int(input("Enter Number x : "))
n=int(input("Enter Number n : "))
s=x
f=1
print(x,end=' + ')
for i in range(2,n+1):
    if i<n:
        print(str(x)+"^"+str(i)+"/"+str(i)+"!",end=' + ')
    else:
        print(str(x)+"^"+str(i)+"/"+str(i)+"!")
    f=f*i
    s+=x**i/f
print("Sum of Series is:",round(s,2))
