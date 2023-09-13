# get the quantity from user
qantity = int(input("enter the quantity"))
# per-unit price
unit_price = 5
# formula for calculation
total = qantity * unit_price
if qantity > 30:
    discount_price = total * 0.10
    total -= discount_price
    print(f"price after dicount of {qantity} is {discount_price}")
elif qantity > 50:
    price = total * 0.15
    total -= price
    print(f"price after the discount for {qantity} is {total}")
else:
    print(f"total pricer Rs: {total:.2f}")
