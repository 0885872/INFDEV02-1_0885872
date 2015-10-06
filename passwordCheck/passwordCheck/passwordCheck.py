import re

password = raw_input("Please insert your password ")
if len(password) < 3:
    print "Password is weak"
elif len(password) > 10:
    print "Password contains 10+ characters, password is strong."
elif (password.isupper or password.isspace or password.isdigit) and password == ('[~!@#$%^&*()_+{}":;\']+$'):
    print "Password contains uppercase, space or digits AND special characters. Password is strong."

        #"""create a set containing all your invalid characters, then take the intersection of it and password (in other words, a set containing all unique characters that exist in both the set and the password string). 
        #If there are no matches, the resulting set will be empty, and thus evaluate as False, otherwise it will evaluate as True and print the message."""

elif password == '!' or password == '@' or password == '#' or password == '$' or password == '%' or password == '^' or password == '&' or password == '*' or password == '-' or password == '_':
#('[~!@#$%^&*()_+{}":;\']+$'):
    print "Password contains special characters. Password is medium"
elif password.isupper or password.isspace or password.isdigit:
    print "Password contains uppercase, space or digits. Password is medium."
   
   
    


