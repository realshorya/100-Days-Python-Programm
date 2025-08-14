#Factors of a Numbers
num=int(input("Enter number to get Factors:"))
count=0
print("Factors are:")
for i in range(1,num+1):
    if num%i==0:
        print(i)
