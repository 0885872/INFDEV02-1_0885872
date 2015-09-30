word = raw_input("Please insert your words: ")
shiftedAmount = int(raw_input("Insert shifted amount: "))
if word.isdigit(): 
    print "invalid entry"
else:
    for x in range (0,len(word)):
        cryptoDigit = ord(word[x]) + shiftedAmount
        cryptoLetter = chr(cryptoDigit)
        print cryptoLetter
        


          

