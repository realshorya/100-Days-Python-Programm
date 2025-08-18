#Check Number is Palindrome or Not
num=int(input("Enter Number:"))
a=num
sum=0
while num>0:
    d=num%10
    sum=sum*10+d
    num=num//10
if a==sum:
    print(sum,"Is Palindrome")
else:
    print("Its not Palindrome because Reverse of Number is:",sum)
