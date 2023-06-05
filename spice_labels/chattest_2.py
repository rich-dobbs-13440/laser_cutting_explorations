import ply.lex as lex
import ply.yacc as yacc

# Token list
tokens = (
    'NUMBER',
    'ID',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMENT',  # Added token for comments
)

# Token regex definitions
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Ignored characters
t_ignore = ' \t'

# Line comment handling
def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Lexer instance
lexer = lex.lex()

# Grammar rules
def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    # Handle assignment here
    print("Assignment: {} = {}".format(p[1], p[3]))

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_function_call(p):
    'function_call : ID LPAREN RPAREN'
    # Handle function call here
    print("Function Call: {}".format(p[1]))

def p_module_definition(p):
    'module_definition : ID LPAREN RPAREN LBRACE module_body RBRACE'
    # Handle module definition here
    print("Module Definition: {}".format(p[1]))

def p_module_body(p):
    'module_body : COMMENT'
    # Handle module body here
    print("Module Body: {}".format(p[1]))

def p_error(p):
    print("Syntax error")

# Parser instance
parser = yacc.yacc()

# Test input
input_text = """
x = 5 + 3;
module myModule() {
    // Module body
}
"""

# Parsing
result = parser.parse(input_text)

# Output
print("Parsing complete.")
