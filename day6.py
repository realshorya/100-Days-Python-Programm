# Electricity Bill Generation
unit=int(input("Enter Unit Consumed by Consumer:"))
if unit<=200:
    total=unit*4
elif unit<=500:
    total=800+(unit-200)*6
elif unit<=800:
    total=800+1800+(unit-500)*8
else:
    total=800+1800+2400+(unit-800)*10
print("Total Amount to be Paid:",total)
    
