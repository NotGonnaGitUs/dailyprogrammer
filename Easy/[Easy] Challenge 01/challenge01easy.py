name = input("What is your name?")
age = input("What is your age?")
reddit_username = input("What is your reddit username?")

output = "Your name is "+name+", you are "+age+" years old, and your username is "+reddit_username+"."

print(output)

f=open("names.txt",'a')
f.write(name+","+age+","+reddit_username+"\n")
f.close()
