#Find Equilateral/Isosceles/Scalene Triangle
a=int(input("Enter Side A:"))
b=int(input("Enter Side B:"))
c=int(input("Enter Side C:"))
if a==b and b==c:
    print("This is Equilateral")
elif a==b or b==c or c==a:
    print("This is Isosceles")
else:
    print("This is scalene")
