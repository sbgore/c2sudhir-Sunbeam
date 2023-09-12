def avg(num1, num2, num3):
    assert isinstance(num3, object)
    result = num1 + num2 + num3 / 3
    return result


# main function
number1 = 10
number2 = 20
number3 = 30
ans = number1 + number2 + number3
print(f"avg {number1} {number2} {number3} is {ans}")
