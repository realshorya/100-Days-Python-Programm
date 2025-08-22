#List of Prime Number in a Given Range
start=int(input("Enter Starting Number:"))
end=int(input("Enter Ending Number:"))
for num in range(start,end+1):
        for a in range(2,num):
            if num%a==0:
                break
        else:
            print(num,"is Prime")
            
