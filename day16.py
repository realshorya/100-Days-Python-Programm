#LCM of Two Numbers
a=int(input("Enter Number A:"))
b=int(input("Enter Nummber B:"))
if a>b:
    g=a
else:
    g=b
for i in range(g,a*b+1):
    if i%a==0 and i%b==0:
        print("LCM of",a,"and",b,"is",i)
        break
else:
    print("No LCM FOUND!!:(")
