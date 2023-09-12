# programme for a place vlaue and Face value

def place_value_face_value(number, digit_position):
    # Check if the digit_position is valid
    if digit_position < 1:
        return "Invalid digit position"

    divisor = 1
    for _ in range(digit_position - 1):
        divisor *= 10

    # Calculate the face value
    face_value = (number // divisor) % 10

    # Calculate the place value
    place_value = face_value * divisor

    return f"Face value of digit at position {digit_position}: {face_value}, Place value: {place_value}"


# Example usage
print(" enter the four digit number")
num = int(input())
digit_position = 3
result = place_value_face_value(num, digit_position)
print(result)
