#Here we just created a input call which can do lexer operation and basic computation like adding,subtraccting,multipling,dividing
#Through python
# CONSTANTS
DIGITS = '0123456789'   
# ERRORS
class Error:
    def __init__(self, pos_s, pos_end, error_name, details):
        self.pos_s = pos_s
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_s.fn}, line {self.pos_s.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_s, pos_end, details):
        super().__init__(pos_s, pos_end, 'Illegal Character', details)

# POSITION

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

# TOKENS
#Here we just defined a token class 
TT_INTGERS		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS_OPER     = 'PLUS'
TT_MINUS_OPER    = 'MINUS'
TT_MUL_OPER      = 'MUL'
TT_DIV_OPER      = 'DIV'
TT_LPARENTHESIS   = 'LEFTPAREN'
TT_RPARENTHESIS  = 'RIGHTPAREN'
TT_LSQUARE     ='LEFT_SQUARE'
TT_RSQUARE    ='RIGHT_SQUARE'

class Token: #Started creating a constructor class
    def __init__(self, type_, value=None): #Here we first we created a mould for token which should have a type and value
                                            #Then further it process.... 
        self.type = type_
        self.value = value          #Assigned variable names for those arguments
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'   #Here repr__() returns object representation in string format
        return f'{self.type}'      #
# LEXER
class Lexer:   #Lexer class
    def __init__(self, fn, text): #Here we assigining the text as argument we want to process...
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text) #Here we keep on tracking current pos 
        self.current_char = None 
        self.advance()
    
    def advance(self):  #Here we defined advance() which advance each charcter into text..
        self.pos.advance(self.current_char) #Here the character cheking process is started from 0
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):      #Creating a simple tokens which is result at the end 
        tokens = []

        while self.current_char != None: #Here the loop startes with first letter of character
            if self.current_char in ' \t': #In we called those constant's in the if clause 
                self.advance()                    #Then it advances to next character
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS_OPER))      #
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS_OPER))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL_OPER))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV_OPER))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPARENTHESIS))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPARENTHESIS))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token(TT_LSQUARE))
                self.advance()
            elif self.current_char ==']':
                tokens.append(Token(TT_RSQUARE))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.': #Here we checked that the current character is not equal to None
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INTGERS, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

# RUN

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
