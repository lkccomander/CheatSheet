import sys


# first python
# set up and methods for the Usodd  US --- Decimal
# For positive US ODDS: DECIMAL ODDS = (USODDS/100) +1
# for negative US ODDS: DECIMAL ODDS = (100/USODDS ) +1


#print("Hello World!!")
#print(7 * 7)
#print()
#print("the end")
#print('The use of string "OOO" XX')
#print("Hello" + "Concat")

greeting = "Hello \n to US odd Decimal Odd Script!!\n"
usodd = ''
usodd1 = ''
flag = True
# comment

print(greeting + " ***************** " )


while usodd1 != 'x':
    usodd1 = input("Please enter the value of the odd:\n")
    pdodd = float(usodd1)
    print(":CHECK:", pdodd)
    result = ""

    if pdodd < 0:
        pdodd = pdodd * (-1)
        print(":PDODD:", pdodd)
        dodd = (100/pdodd)+1
        result = format(dodd)
    elif pdodd >= 100:
        dodd = (pdodd/100)+1
        result = format(dodd)
    elif pdodd >= 2.0:
        dodd = (pdodd - 1 ) * 100
        result = str("+"+str(dodd))

    elif pdodd <= 2.0 and pdodd >= 0:
        dodd = (-100)/(pdodd-1)
        result = dodd

    else:
        dodd = 0

    print("\nDecimal odd:\n:", format(result))
-109


# sys.exit()



#print('DEFAULT:'+usodd+' \n Enetred by the user' +usodd1+' 120')

#splitstring = "This is a \n a split\n string. \n"
#print(splitstring)
#pUsodd = Usodd()
