#Leap Year or Non-Leap Year
year=int(input("Enter The Year:"))
if year%100==0:
    if year%400==0:
        print(year,"is Leap Year")
    else:
        print("Its not a Leap Year")
else:
    if year%4==0:
        print(year,"is Leap Year")
    else:
        print("Its not a Leap Year")
