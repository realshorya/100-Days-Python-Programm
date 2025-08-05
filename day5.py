# Roots of Quadratic Equation
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
d=b**2-4*a*c
if d<0:
    print("No Real Roots Are there")
elif d==0:
    r1=r2=-b/(2*a)
    print("Real And Equal Roots Are:",r1,r2)
else:
    r1=(-b+d**0.5)/(2*a)
    r2=(-b-d**0.5)/(2*a)
    print("Real And Unqual Roots Are:",round(r1,2),round(r2,2))
