a=99

bottle = "bottles"
while a!=0:
    print (a, bottle, "of beer on the wall", a, bottle,"of beer. Take one down and pass it around,",end=" ")
    a-=1


    if (a ==0):
        break

    # New line at least makes it readable
    print (a, end=" ")
    if (a==1):
        bottle = "bottle"
    print (bottle,"of beer on the wall.")
print ("no more bottles of beer on the wall.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
