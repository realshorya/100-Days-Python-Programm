#Reversing a List 
a=[20,18,30,46,11,35]
print("List before Reverse")
print(a)
n=len(a)
for i in range(n//2):
    a[i],a[n-i-1]=a[n-i-1],a[i]
print("List after Reverse")
print(a)
