#Swap Adjecent Sides of a List
a=eval(input("Enter The Values for the List(Enter In Box Brackets):"))
print("List Before Swap")
print(a)
for i in range(0,len(a),2):
    a[i],a[i+1]=a[i+1],a[i]
print("List after Swap")
print(a)
