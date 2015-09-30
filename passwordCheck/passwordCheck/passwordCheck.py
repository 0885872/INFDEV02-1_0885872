def passwordCheck():
    password = raw_input("Please insert your password ")
    if len(password) < 3:
        print "Password is weak"
    elif len(password) > 10:
        print "Password contains 10+ characters, password is strong."
    elif password.isupper or password.isspace or password.isdigit:
        print "Password contains uppercase, space or digits. Password is medium."
    


passwordCheck()
