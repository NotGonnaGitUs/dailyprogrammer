morse = {"A" : ".-", 	"B" : "-...", 	"C" : "-.-.", 	"D" : "-..", "E" : ".",	"F" : "..-.",	"G" : "--.", 	"H" : "....", 	"I" : "..",	"J" : ".---", 	"K" : "-.-", 	"L" : ".-..", 	"M" : "--", 	"N" : "-.", 	"O" : "---", 	"P" : ".--.", 	"Q" : "--.-", 	"R" : ".-.", 	"S" : "...", 	"T" : "-", 	"U" : "..-", 	"V" : "...-", 	"W" : ".--", 	"X" : "-..-", 	"Y" : "-.--", 	"Z" : "--..", 	"0" : "-----", 	"1" : ".----", 	"2" : "..---", 	"3" : "...--", 	"4" : "....-", 	"5" : ".....", 	"6" : "-....", 	"7" : "--...", 	"8" : "---..", 	"9" : "----."}

a_morse = {".-" : "A", 	"-..." : "B", 	"-.-." : "C", 	"-.." : "D", 	"." : "E", 	"..-." : "F", 	"--." : "G", 	"...." : "H", 	".." : "I", 	".---" : "J", 	"-.-" : "K", 	".-.." : "L", 	"--" : "M", 	"-." : "N", 	"---" : "O", 	".--." : "P", 	"--.-" : "Q", 	".-." : "R", 	"..." : "S", 	"-" : "T", 	"..-" : "U", 	"...-" : "V", 	".--" : "W", 	"-..-" : "X", 	"-.--" : "Y", 	"--.." : "Z", 	"-----" : "0", 	".----" : "1", 	"..---" : "2", 	"...--" : "3", 	"....-" : "4", 	"....." : "5", 	"-...." : "6", 	"--..." : "7", 	"---.." : "8", 	"----." : "9"}



def encoder (text):
    morse_text =""
    for each in text:
        morse_text += morse[each]
        morse_text +=" "
    return morse_text

def decoder (morse_text):
    list_of_words = morse_text.split(" / ")
    decoded = ""
    for each in list_of_words:
        letters = each.split(" ")
        for e in letters:
            decoded += a_morse[e]
        decoded += " "

    return decoded

while True:
    command = input("Morse text convereter. Enter (e) for encoding or (d) for decoding.")
    if (command=="e"or command =="d"):
        text = input("Enter text ").upper()
        if (command == "d"):
            print (decoder(text))
        else:
            print (encoder(text))
        break
    else:
        print ("Invalid input")
