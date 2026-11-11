symbols = [' ', '(', ')', '{', '}', ';', '\n', '\t']
keywords = ['var', 'logic', 'if', 'while', 'true', 'false']
token_type = {
    # Operatory matematyczne
    '+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH', '=': 'EQUAL',
    # poniżej inne znaczki
    '.': 'DOT', ',': 'COMMA', ';': 'SEMICOLON', '(': 'LPAREN', ')': 'RPAREN', '{': 'LBRACE', '}': 'RBRACE',
    # logiczne
    '==': 'DEQUAL', '<=': 'LEQUAL', '>=': 'GEQUAL', '<': 'LESS', '>': 'GREATER', '&': 'AND', '|': 'OR', '!': 'NOT',
}
"""
Interpreter jest na wczesnym etapie rozwoju, możliwe że w przyszłości część metod trafi do oddzielnych klas
"""

class Interpreter:
    """Główna klasa zarządzająca zasobami interpretera, zawiera również metody odpowiadające za skanowanie i tokenizację"""
    def __init__ (self): 
        self.input_line = ""
        self.had_error = False
        self.source_code = ""
        self.lexemes = []


    def run_self (self):
        """Metoda wykonująca główną pętlę programu (na ten moment obsługa wprowadzania przez terminal)"""
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
        """Metoda wczytująca dane z terminala, możliwe że zostanie usunięta"""
        self.input_line = input("> ")

    def throw_error(self):
        """Po implementacji ta metoda będzie wyrzucała sformatowany błąd"""
        pass

    def scanner(self):
        """Metoda skanująca źródło i dzieląca go na jednoski znaczeniowe (bez klasyfikacji)"""
        self.lexemes = []
        lexeme = ""
        for i, char in enumerate(self.source_code): # enumaerate jest po to aby można było spojżeć naprzód w source_code

            if char not in symbols:
                lexeme += char # wczytujemy znaki do: momentu natrafienia na symbol

                if i + 1 < len(self.source_code): 
                    next_char = self.source_code[i + 1] # zaglądamy krok dalej
                    if next_char in symbols: # jeśli trafiamy na symbol to znaczy, że lexem się kończy
                        self.lexemes.append(lexeme)
                        lexeme = ""
                else: # jeśli kończy się kod źródłowy to nie czytamy dalej
                    self.lexemes.append(lexeme)
                    lexeme = ""
            else: # jeśli trafiamy na symbol to go oddzielnie dodajemy 
                self.lexemes.append(char)
                lexeme = ""

    def tokenizer(self):
        """Metoda ta kategoryzuje lexemy i pomija te które nie pasują do żadnej kategorii"""
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

if __name__ == "__main__":
    main()