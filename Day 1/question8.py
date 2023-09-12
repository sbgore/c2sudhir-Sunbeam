# telephone bill calculator
# Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.
# Get the number of calls from the user
num_calls = int(input("Enter the number of calls: "))

# Initialize the base charge
base_charge = 200

# Initialize variables for additional charges
additional_charge_50 = 0
additional_charge_50_100 = 0
additional_charge_above_100 = 0

# Calculate additional charges based on the number of calls
if num_calls > 100:
    additional_calls = num_calls - 100

    if additional_calls <= 50:
        additional_charge_50 = additional_calls * 0.60
    else:
        additional_charge_50 = 50 * 0.60
        additional_calls -= 50

    if additional_calls > 0:
        if additional_calls <= 50:
            additional_charge_50_100 = additional_calls * 0.50
        else:
            additional_charge_50_100 = 50 * 0.50
            additional_calls -= 50

    if additional_calls > 0:
        additional_charge_above_100 = additional_calls * 0.40

# Calculate the total bill
total_bill = base_charge + additional_charge_50 + additional_charge_50_100 + additional_charge_above_100

# Display the total bill
print(f"Your monthly telephone bill is: Rs. {total_bill:.2f}")
