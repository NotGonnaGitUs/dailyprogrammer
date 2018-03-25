def encrypt(l,c):
    astart = ord("a")
    capstart = ord("A")
    ordl = ord(l)
    if ordl>=astart:
        return chr((astart+((ordl-astart+c)%26)))
    else:
        return chr((capstart+((ordl-capstart+c)%26)))

def decrypt(l,c):
    astart = ord("a")
    capstart = ord("A")
    ordl = ord(l)
    if ordl>=astart:
        return chr((astart+((ordl-astart-c)%26)))
    else:
        return chr((capstart+((ordl-capstart-c)%26)))


raw_string = input("Enter the message ")
enter_cipher = int(input("Enter the cipher code in number"))
command = input("Enter (e) to encode or (d) to decode")
encoded = ""
if command == "e":
    for each in raw_string:
        encoded += encrypt(each,enter_cipher)
elif command == "d":
    for each in raw_string:
        encoded += decrypt(each,enter_cipher)
else:
        command = input("Enter (e) to encode or (d) to decode")

print(encoded)
