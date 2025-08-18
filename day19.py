#Sum of Digits of a Number
num=int(input("Enter Number:"))
a=num
sum=0
while num>0:
    d=num%10
    sum+=d
    num=num//10
print("Sum of",a,"is",sum)
