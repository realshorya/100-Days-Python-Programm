#Remove Duplicate from a List
a=eval(input("Enter the values for the List(Enter in box Bracket):"))
print("List Before remove Duplicate")
print(a)
i=0
while i<len(a):
    if a.count(a[i])>1:
        a.remove(a[i])
    else:
        i+=1
print("List After Remove Duplicate")
print(a)
