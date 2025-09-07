#Find Second Highest Number in a List
a=eval(input("Enter the values for the List(Enter in Box Brackets):"))
print("List Values:",a)
n=max(a)
while n in a:
    a.remove(n)
res=max(a)
print("Second Highest Value is",res)
