"""
Program: SigFig Finder
Purpose: To determine the significant figures in an inputed number.
Algorithm Flow/Structure: 
    1. The program will start and prompt user for input
    2. The input (num) will be converted to an int
    3. Num will be used to create an sigfig number class object
        a. When this occurs each digit will be added to an array in the sigfig number class
        b. When added the digits will be converted to sigFig digits
        c. Before initialization is complete which sigFig digits are significant will be determined.
    4. Output will be produced with the significant figures identified

OO:
    an SFnumber will represent a number it will contain SFdigits
    an SFdigit will be represent a digit in a SFnumber and may be indicated as significant
    
"""

class SFnumber:
    
    def display(self):
        print(self.intNum)
        pass
    
    def convertIntToArr(self):
        self.intNum
    
    def __init__(self,num):
        self.intNum = num
        self.convertIntToArr
        self.findSF
        

def main ():
    n = SFnumber(getNum())
    n.display
    
def getNum():
    return int(input("enter number: "))


    