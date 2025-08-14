#Profit or Loss Calculator
cp=int(input("Enter Actual Amount of Product:"))
sp=int(input("Enter Selling Amount of Product:"))
if sp>cp:
    print("You are in Profit of",sp-cp,"rs")
elif sp==cp:
    print("No Profit or Loss")
else:
    print("You are in Loss of",cp-sp,"rs")
