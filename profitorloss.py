actual_cost = float(input("enter the cost price"))
sale_amount = float(input("enter the selling price"))

if sale_amount>actual_cost:
    print("profit, by", sale_amount - actual_cost )

else:
    print("It is a loss")

