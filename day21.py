#Sum of Series...1/1+1/2+1/3..1/n
num=int(input("Enter Lenght of Series:"))
s=0
for i in range(1,num+1):
    if i<num:
        print("1/"+str(i),end=' + ')
    else:
        print("1/"+str(i))
    s+=1/i
print("Sum of Series is:",round(s,2))
