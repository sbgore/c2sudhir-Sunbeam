def translate(str2):
    result = ""
    for i in str2:
        if i not in "aeiou' '":
            result += i + "o" + i
        else:
            result += i

    print(result)


str1 = "this is fun"
translate(str1)
