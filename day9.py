#Grade of a Student as per Percentage Marks
per=int(input("Enter the percentage marks secured:"))
if per>=90:
    print("Grade:A+")
elif per>=80:
    print("Grade:A")
elif per>=60:
    print("Grade:B")
elif per>=50:
    print("Grade:C")
else:
    print("Grade:D")
