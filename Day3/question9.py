#10) write a function to return compound interest
def compound_interest(principal, rate, time, comp_per_year):
    # Calculate the compound interest
    amount = principal * (1 + (rate / comp_per_year)) ** (comp_per_year * time)
    # Calculate the interest earned (amount - principal)
    interest = amount - principal
    return interest

# Example usage:
principal = 1000  # Initial principal amount
rate = 0.05      # Annual interest rate (5%)
time = 3         # Number of years
comp_per_year = 12  # Compounded monthly

interest = compound_interest(principal, rate, time, comp_per_year)
print(f"Compound interest earned: Rs {interest:.2f}")
