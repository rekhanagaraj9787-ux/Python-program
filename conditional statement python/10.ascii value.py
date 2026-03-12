ch = input("Enter character: ")
ascii_value = ord(ch)

if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
    print("Alphabet")
elif 48 <= ascii_value <= 57:
    print("Digit")
else:
    print("Special Character")