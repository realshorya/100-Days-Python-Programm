#Fabonacci Series up to N Numbers
num=int(input("How Many Elements of a Fabonacci Series are to be printed:"))
a=0
b=1
if num>2:
    print(a,b,end=" ")
    for i in range(num-2):
        c=a+b
        print(c,end=" ")
        a,b=b,c
