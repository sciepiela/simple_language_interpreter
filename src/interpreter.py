symbols = [' ', '(', ')', '{', '}', ';', '\n']
keywords = ['var', 'logic', 'if', 'while', 'true', 'false']
token_type = {
    # Operatory matematyczne
    '+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH', '=': 'EQUAL',
    # poniżej inne znaczki
    '.': 'DOT', ',': 'COMMA', ':': 'SEMICOLON', '(': 'LPAREN', ')': 'RPAREN', '{': 'LBRACE', '}': 'RBRACE',
    # logiczne
    '==': 'DEQUAL', '<=': 'LEQUAL', '>=': 'GEQUAL', '<': 'LESS', '>': 'GREATER', '&': 'AND', '|': 'OR', '!': 'NOT',
}

class Interpreter:
    def __init__ (self): 
        self.input_line = ""
        self.had_error = False
        self.source_code = ""
        self.lexemes = []


    def run_self (self):
        print("In order to quit type: 'quit;'\nIn order to run your code type: 'run;'")
        while self.input_line != "quit;":
            self.prompt()

            if self.input_line == "run;":
                self.scanner()
                self.tokenizer()
                print(self.tokens)

            self.source_code += self.input_line
            if self.had_error:
                self.throw_error()


    def prompt (self):
        self.input_line = input("> ")

    def throw_error(self):
        pass

    def scanner(self):
        lexeme = ""
        for i, char in enumerate(self.source_code):
            if char not in symbols:
                lexeme += char
                if i + 1 < len(self.source_code):
                    next_char = self.source_code[i + 1]
                    if next_char in symbols:
                        self.lexemes.append(lexeme)
                        lexeme = ""
                else:
                    self.lexemes.append(lexeme)
                    lexeme = ""
            else:
                self.lexemes.append(char)
                lexeme = ""

    def tokenizer(self):
            self.tokens = []
            
            for lexem in self.lexemes:
                if lexem in (' ', '\n', '\t', '\r'):
                    continue
                if lexem in keywords:
                    t_type = lexem.upper()
                elif lexem in token_type:
                    t_type = token_type[lexem]
                elif lexem.isdigit():
                    t_type = 'NUMBER'
                else:
                    t_type = 'IDENTIFIER'
                    
                self.tokens.append((t_type, lexem))


def main():
    interpreter = Interpreter()
    interpreter.run_self()

main()