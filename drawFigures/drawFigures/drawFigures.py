import sys
star = "*"
space = " "
saveWidth = ""
saveWidthSec = ""
enter = "\n"




print "Let's get happy, let's draw figures!"
figureChoice = raw_input("""Choose what kind of figure you want to draw: 
1square, 2square, 1triangle, 2triangle, circle or smiley? : """)



# Let's draw a square of stars
if figureChoice == "1square":

    figureHeight = int(raw_input("height of the figure should be: "))
    figureWidth = int(raw_input("width of the figure shoud be: "))

    for x in range(0,figureWidth):
        saveWidth = saveWidth + star
    for t in range(0,(figureHeight)):
        print saveWidth

# Let's draw a square with empty space inside
if figureChoice == "2square":

    figureHeight = int(raw_input("height of the figure should be: "))
    figureWidth = int(raw_input("width of the figure shoud be: "))

    for x in range(0,figureWidth + 2):
        saveWidth = saveWidth + star

    for t in range(0,(figureWidth - 2)):
        saveWidthSec = saveWidthSec + space

    for s in range(0,(figureHeight + 1)):
        if s== 0 or s == figureHeight:
            print saveWidth
        else:
            print star, saveWidthSec, star
        
# Let's draw a triangle(like stairs)     
elif figureChoice == "1triangle":
    figureWidth = int(raw_input("width of the figure shoud be: "))
    for x in range(0, figureWidth):
        saveWidth = saveWidth + star
        print saveWidth

# Let's draw a triangle(like a spike)
elif figureChoice == "2triangle":
    figureWidth = int(raw_input("width of the figure shoud be: "))
    for t in range(0, figureWidth):
        saveWidthSec = saveWidthSec + star
    


