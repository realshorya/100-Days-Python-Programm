#Swap 1st half of a List with 2nd half
a=eval(input("Enter the values for the List(Enter In Box Brackets):"))
print("List Before Half Swap")
print(a)
n=len(a)
if n%2==0:
    gap=n//2
else:
    gap=n//2+1
for i in range(n//2):
    a[i],a[i+gap]=a[i+gap],a[i]
print("List After Half Swap")
print(a)
