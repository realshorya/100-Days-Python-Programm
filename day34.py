#Linear Search
a=[35,40,28,20,42,25]
print(a)
search=int(input("Enter Number to be Searched:"))
for i in range(0,len(a)):
    if a[i]==search:
        print("Number Found")
        break
else:
    print("Not Found in List")
