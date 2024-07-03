

def drawTree(number):
     
     for x in range(number):

        noOfstars = x
        stars = "*" * noOfstars
        blanks = " " * (number - x)
        print(blanks +stars +'*' + stars)
    



drawTree(4)