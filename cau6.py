# câu 6:
def isBalanced(equation):
    roundBracketCount = 0
    squareBracketCount = 0
    curlyBracketCount = 0

    for letter in equation:
        if (letter == '('):
            roundBracketCount += 1
        if (letter == ')'):
            roundBracketCount -= 1
        if (letter == '['):
            squareBracketCount += 1
        if (letter == ']'):
            squareBracketCount -= 1
        if (letter == '{'):
            curlyBracketCount += 1
        if (letter == '}'):
            curlyBracketCount -= 1
        
    if roundBracketCount != 0:
        print("Equation is missing a round bracket")
    if curlyBracketCount != 0:
        print("Equation is missing a curly bracket")
    if squareBracketCount != 0:
        print("Equation is missing a square bracket")
    if roundBracketCount == 0 and curlyBracketCount == 0 and squareBracketCount == 0:
        print("Equation is error free")

isBalanced("(2x)^2 + ({9")
