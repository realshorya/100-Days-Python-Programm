#Binary Search
a=[15,20,24,30,32,45,48,55]
print(a)
search=int(input("Enter Number to be Searched:"))
beg=0
end=len(a)-1
while beg<=end:
    mid=(beg+end)//2
    if a[mid]==search:
        print("Number Found at",mid+1)
        break
    elif a[mid]>search:
        end=mid-1
    else:
        beg=mid+1
else:
    print("Number is not in List")
