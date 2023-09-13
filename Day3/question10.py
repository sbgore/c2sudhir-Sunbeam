# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
def telephonebill(n):
    # base price is 200 for 100 calls
    calls = 100
    base_price = 200
    n=int(n)
    if n > 100 and n < 150:
        total = n - calls
        bill = total * 0.60+200
        print(f"bill for 100 and next 50 call {bill}")
    elif n > 150 and n < 200:
        total = n - calls
        bill = total * 0.50+200
        print(f"bill fir calls above 150 and next 50 calls{bill}")
    elif n > 200:
        total = n - calls
        bill = total * 0.40+200
        print(f"bill for the calls above 200 {bill}")
    else:
        print(f" price for calls up to 100 is {base_price:.2f}")


# function
no_of_call = input("enter the no of calls")
telephonebill(no_of_call)
