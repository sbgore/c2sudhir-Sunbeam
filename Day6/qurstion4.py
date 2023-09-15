# 5)Calculate the sum and average of the digits present in a string
# Str1="Python83737@#8496"
str1 = "Python83737@#8496"
digit_sum = 0
digit_count = 0

for char in str1:
    if char.isdigit():
        digit_sum += int(char)
        digit_count += 1

if digit_count > 0:
    digit_avg = digit_sum / digit_count
else:
    print(f"digit avg=0")

print(f"sum of the digit is{digit_sum}")
print(f"digit avg is {digit_avg:.2f}")
