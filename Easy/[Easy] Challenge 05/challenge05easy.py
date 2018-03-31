import random
def generate(length):
    out = []
    for i in range(length):
        out.append(random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()",1)[0])
    return "".join(out)

length = int(input("Enter the desired password length "))
number = int(input("Enter number of passwords to generate "))

f=open("pass.txt",'a')
for i in range(number):
    passw = generate(length)
    f.write(passw+"\n")
    print (passw)
f.close()
