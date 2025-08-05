# Shopping Bill With Discount
p=float(input("Enter Product Price:"))
qty=float(input("Enter Product Quantity:"))
total=p*qty
GST=12*total/100
amount=total+GST
print("-"*30)
print("Product Amount:",total)
print("GST Amount 12%:",GST)
print("Product Total Amount",amount)
if amount<1000:
    print("No Discount Above 1000rs of Shopping")
elif amount>3000:
    disc=0.2*amount
    print("Discount Above 3000rs of Shopping Applied 20%")
    print("Discounted Amount:",round(disc,2))
    print("FINAL AMOUNT:",amount-disc)
else:
    disc=0.1*amount
    print("Discount Above 1000rs of Shopping Applied 10%")
    print("Discounted Amount:",round(disc,2))
    print("FINAL AMOUNT:",amount-disc)    
print("-"*30)
