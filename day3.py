# Student Report Card
name=input("Enter Student name:")
m1=float(input("Enter Marks of First Subject:"))
m2=float(input("Enter Marks of Second Subject:"))
m3=float(input("Enter Marks of Third Subject:"))
m4=float(input("Enter Marks of Fourth Subject:"))
m5=float(input("Enter Marks of Fifth Subject:"))
total=m1+m2+m3+m4+m5
avg=total/5
print("-"*30)
print("Student Name:",name)
print("Total Marks:",total,"/ 500.0")
print("Total Percentage:",avg,"%")
if avg>=33:
    print("Congratulations You Promoted To NEXT CLASS")
else:
    print("OOPS!! Failed :(( ")
print("-"*30)
