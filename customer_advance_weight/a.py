Paid_Amount = []
Paid_Amount.append("97878.60")
Total_Purchase_Amount= float(Paid_Amount[0])

Sale_Amount=[] 
Sale_Amount.append("197878.60")
Total_Sale_Amount = float(Sale_Amount[0])

balance = Total_Purchase_Amount - Total_Sale_Amount
balance_Amount = abs(round(balance))
print(balance_Amount)

if Total_Sale_Amount < Total_Purchase_Amount:
    print(9)
elif Total_Sale_Amount==Total_Purchase_Amount:
    print(6)    
else:
    print(7)    
    
    
    
a =  97870.60
b = 135353
v = a - b  # Subtract b from a
expected_output = abs(round(v))  # Take the absolute value and round
print(expected_output)

if 220129.02 == 99174:
    print(3)

elif 220129.02 > 99174:
    print(7)

elif 220129.02 < 99174:
    print(8)