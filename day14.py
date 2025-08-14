#Perfect number or not
num=int(input("Enter number:"))
fact=0
for i in range(1,num):
    if num%i==0:
        fact+=i
if fact==num:
    print(num,"is a Perfect Number")
else:
    print(num,"is not a Perfect Number")
