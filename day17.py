#HCF of Two Numbers(Long Division Method)
a=int(input("Enter Number A:"))
b=int(input("Enter Number B:"))
rem=0
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("LCM is",rem)
