#List of Armstrong Numbers from 100 to 1000
print("List of Armstrong Number from 100 to 1000")
for i in range(100,1000):
    s=0
    num=i
    while num>0:
        d=num%10
        s+=d**3
        num=num//10
    if i==s:
        print(i,"is Armstrong Number")
