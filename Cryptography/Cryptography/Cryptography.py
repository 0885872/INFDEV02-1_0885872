word = raw_input("Please insert your words: ")
shiftedAmount = int(raw_input("Insert shifted amount: "))
cryptoLetter = ""
if word.isdigit(): 
    print "invalid entry"
else:
    for x in range (0,len(word)):
        ascii = ord(word[x])
        if ascii >= 122:
            correction = ascii - 122
            cryptoLetter1 = chr(97 + correction)
            cryptoLetter = cryptoLetter + cryptoLetter1
            
        else:
            cryptoDigit = ord(word[x]) + shiftedAmount
            cryptoLetter2 = chr(cryptoDigit)
            cryptoLetter = cryptoLetter + cryptoLetter2
            
        
print cryptoLetter        


          

