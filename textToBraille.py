#Convert Text String to Braille
import json

#Initialize user input variable
userInput = ""

#Function: Convert Text String to Braille
def solution(convertMe):
    countQuo = 0 #Determins if " is opening or closing
    conversionChart = json.loads ("""
            {"a": "100000",
             "b": "110000",
             "c": "100100",
             "d": "100110",
             "e": "100010",
             "f": "110100",
             "g": "110110",
             "h": "110010",
             "i": "010100",
             "j": "010110",
             "k": "101000",
             "l": "111000",
             "m": "101100",
             "n": "101110",
             "o": "101010",
             "p": "111100",
             "q": "111110",
             "r": "111010",
             "s": "011100",
             "t": "011110",
             "u": "101001",
             "v": "111001",
             "w": "010111",
             "x": "101101",
             "y": "101111",
             "z": "101011",
             "'": "001000",
             " ": "000000",
             "?": "011001",
             "!": "011010",
             "&": "111101",
             ",": "010000",
             "_": "001001",
             ".": "010011",
             "#": "001111",
             "#": "001111",
             ";": "011000",
             ":": "010010",
             "(": "111011011011",
             ")": "011111011011",
             "<": "111011011011",
             ">": "011111011011",
             "/": "001100",
             "@": "001101",
             "+": "011010",
             "-": "010010",
             "*": "001010",
             "0": "010110",
             "1": "100000",
             "2": "110000",
             "3": "100100",
             "4": "100110",
             "5": "100010",
             "6": "110100",
             "7": "110100",
             "8": "110110",
             "9": "010100",
             "capital": "000001",
             "decimal": "000101",
             "number": "001111",
             "accent": "000100",
             "openingQuo": "010010",
             "closingQuo": "011001"
    }""")

    brailleSolution = ""
    for element in convertMe:
        if element == "\"" and countQuo == 0:
            brailleSolution += conversionChart["openingQuo"]
            countQuo =+ 1
        if element == "\"" and countQuo == 1:
            brailleSolution += conversionChart["openingQuo"]
            countQuo = 0
        else:
            if element.isdigit() == True:
                brailleSolution += conversionChart["number"] + conversionChart[element]
            elif element.isupper() == True:
                brailleSolution += conversionChart["capital"] + conversionChart[element.lower()]
            elif element.islower() == True:
                brailleSolution += conversionChart[element]
            else:
                brailleSolution += conversionChart[element]
    return brailleSolution

#Loops input prompt for user until input is equal to "exit"
while userInput != "exit":
    userInput = input()
    print ("problem: " + userInput)
    solve = solution(userInput)
    print ("solution: " + str(solve))
    if solve == "01100101011110000110100101110100":
        #print ("solution:" + solution(userInput))
        print ("Exit command detected: Exiting program.")
        break
