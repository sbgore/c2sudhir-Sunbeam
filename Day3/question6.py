def simple_interest(P, R, T):
    intrest = P * R * T / 100
    return intrest


# function call
p = int(input("enter the principal\n"))
t = int(input("enter the time period\n"))
r = float(input("enter the rate per year\n"))
result=simple_interest(p, r, t)
print(f"-----------------------SIMPLE INTREST IS:{result}............................\n")
