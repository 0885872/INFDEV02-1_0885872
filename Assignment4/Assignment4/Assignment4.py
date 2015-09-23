"""Exercise 1A"""

def convertF2C():
   zero_point = -459,67
   fahrenheit = float(raw_input("Amount(Fahrenheit) to be converted : "))

    """  except ValueError:
   print("That's not an int!")"""

   if (fahrenheit < zero_point):
        output = (fahrenheit - 32) / 1.8
        output = round(output, 2)
        print "Celcius: ", output
   elif(fahrenheit > zero_point):
        print "invalid number"

convertF2C()

"""Exercise 1B"""

def convertC2K():
    celsius = float(raw_input("Amount(Celcius) to be converted : "))
    zero_point_celsius = -273,14
    if(celsius > zero_point_celsius):
        kelvin = celsius + 273.15
        kelvin = round(kelvin, 2)
        print "Kelvin: ", kelvin
    elif(celsius < zero_point_celsius):
        print "Invalid number"

convertC2K()

"""Exercise 1C"""

def absAndRound():
    tweakabs = int(raw_input("Insert number to get absolute"))
    tweakabs = abs(tweakabs)
    print "Absolute : ", tweakabs

absAndRound()

"""Exercise 2"""

