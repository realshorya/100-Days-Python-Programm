#Factorial of a number
num=int(input("Enter Number to get Factorial:"))
f=1
for i in range(num,0,-1):
    f=f*i
print("Factorial of",num,"is",f)
