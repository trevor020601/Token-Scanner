import sys

lexeme = []

#CONSTANTS
CHAR_CLASS = {
    'LETTER'  : 0,
    'DIGIT'   : 1,
    'UNKNOWN' : 99,
    'EOF'     : -1
}

TOKEN_CODES = {
    'INT_LIT'     : 10,
    'IDENT'       : 11,
    'ASSIGN_OP'   : 20,
    'ADD_OP'      : 21,
    'SUB_OP'      : 22,
    'MULT_OP'     : 23,
    'DIV_OP'      : 24,
    'LEFT_PAREN'  : 25,
    'RIGHT_PAREN' : 26
}

def main():
    getChar()
    lex()
    while(nextToken != CHAR_CLASS.get('EOF')):
        lex()


def lookup(ch):
    global nextToken
    match ch:
        case '(':
            addChar()
            nextToken = TOKEN_CODES.get('LEFT_PAREN')
        case ')':
            addChar()
            nextToken = TOKEN_CODES.get('RIGHT_PAREN')
        case '+':
            addChar()
            nextToken = TOKEN_CODES.get('ADD_OP')
        case '-':
            addChar()
            nextToken = TOKEN_CODES.get('SUB_OP')
        case '*':
            addChar()
            nextToken = TOKEN_CODES.get('MULT_OP')
        case '/':
            addChar()
            nextToken = TOKEN_CODES.get('DIV_OP')
        case _:
            addChar()
            nextToken = CHAR_CLASS.get('EOF')
    return nextToken

def addChar():
    global lexeme

    lexeme.append(nextChar)

def getChar():
    global charClass, nextChar
    nextChar = in_fp.read(1)

    if len(nextChar) == 0:
        charClass = CHAR_CLASS.get('EOF')
    elif nextChar.isalpha() == True:
        charClass = CHAR_CLASS.get('LETTER')
    elif nextChar.isdigit() == True:
        charClass = CHAR_CLASS.get('DIGIT')
    else:
        charClass = CHAR_CLASS.get('UNKNOWN')

def getNonBlank():
    global nextChar
    while(nextChar.isspace() == True):
        getChar()

def lex():
    global nextToken
    global lexLen
    global charClass
    global lexeme
    lexLen = 0
    getNonBlank()

    match charClass:
        case 0: #CHAR_CLASS.get('LETTER')
            addChar()
            getChar()
            while (charClass == CHAR_CLASS.get('LETTER') or charClass == CHAR_CLASS.get('DIGIT')):
                addChar()
                getChar()
            nextToken = TOKEN_CODES.get('IDENT')
        case 1: #CHAR_CLASS.get('DIGIT')
            addChar()
            getChar()
            while (charClass == CHAR_CLASS.get('DIGIT')):
                addChar()
                getChar()
            nextToken = TOKEN_CODES.get('INT_LIT')
        case 99: #CHAR_CLASS.get('UNKNOWN')
            lookup(nextChar)
            getChar()
        case -1: #CHAR_CLASS.get('EOF')
            nextToken = CHAR_CLASS.get('EOF')
            lexeme.append('EOF')
        
    print("Next token is: {0}, Next lexeme is {1}\n".format(nextToken, "".join(lexeme)))
    lexeme.clear()
    return nextToken

if __name__ == "__main__":
    print("Python version: ", sys.version, "\n")
    global in_fp
    parse = 0
    try:
        if len(sys.argv) == 2:
            in_fp = open(sys.argv[1], 'r')
            parse = 1
            main()
        elif len(sys.argv) == 1:
            in_fp = open('front.in', 'r')
            parse = 1
            main()
        else:
            print("Usage:\n python scanner_C00441253.py [file_to_parse (Optional, default = front.in)]")
    except:
        print("Invalid Input")
