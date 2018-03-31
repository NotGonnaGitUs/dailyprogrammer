# text = input("Enter the telphone number. ")


def validate(text):
    count = 0
    extracted = ""
    override = True
    for each in text:
        if each.isdigit():
            count += 1
            extracted += each
        if each == "/" or each == ":":
            override = False
    if override and (count == 7 or count == 10):
        print (text, "Valid number")
    else:
        print (text, "Invalid number")


inputs = "1234567890, 123-456-7890, 123.456.7890, (123)456-7890, (123) 456-7890 , 456-7890., 123-45-6789, 123:4567890, 123/456-7890. "

listed = inputs.split(sep=", ")

print (listed)
for each in listed:
    validate(each)

validate (input("Please enter your number to validate. "))
