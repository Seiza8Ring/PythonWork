#Task 4: Price List Formatter
item1 = input("Enter Name of item: ")
price1 = float(input("Enter price of item: "))
item2 = input("Enter Name of item: ")
price2 = float(input("Enter price of item: "))
item3 = input("Enter Name of item: ")
price3 = float(input("Enter price of item: "))

price1t = round(price1 *0.06, 2)
price2t = round(price2 *0.06, 2)
price3t = round(price3 *0.06,2)

print(f"""{item1} costs ${price1} with ${price1t} tax.
{item2} costs ${price2} with ${price2t} tax.
{item3} costs ${price3} with ${price3t} tax.""")
