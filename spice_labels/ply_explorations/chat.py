import ply.lex as lex
import ply.yacc as yacc


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'POWER'),
    ('nonassoc', 'LESSTHAN', 'LESSEQUAL', 'EQUAL', 'NOTEQUAL', 'GREATEREQUAL', 'GREATERTHAN'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('right', 'NOT'),
)


# Token list
tokens = (
    'NUMBER',
    'ID',
    'ASSIGN',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMENT',
    'COMMA',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'POWER',
    'LESSTHAN',
    'LESSEQUAL',
    'EQUAL',
    'NOTEQUAL',
    'GREATEREQUAL',
    'GREATERTHAN',
    'AND',
    'OR',
    'NOT',
)


# Token regex definitions
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POWER = r'\^'
t_LESSTHAN = r'<'
t_LESSEQUAL = r'<='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATEREQUAL = r'>='
t_GREATERTHAN = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Ignored characters
t_ignore = ' \t'


# Token handlers
def t_NUMBER(t):
    r'[-+]?\d+(\.\d+)?([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


# Line comment handling
def t_COMMENT(t):
    r'\/\/.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error handler
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Grammar rules
def p_start(p):
    '''start : 
             | statement
             | start statement'''
    pass


# def p_empty(p):
#     'empty :'
#     pass


def p_expression(p):
    '''expression : NUMBER
                  | ID'''
    if p.slice[1].type == 'NUMBER':
        p[0] = p[1]
    else:  # Symbolic expression
        symbol = p[1]
        if symbol in symbol_table:
            p[0] = symbol_table[symbol]
        else:
            print("Error: Symbol '{}' is undefined".format(symbol))
            p[0] = None


def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMICOLON'
    symbol = p[1]
    value = p[3]
    symbol_table[symbol] = value
    print("Assignment: {} = {}".format(symbol, value))


def p_error(p):
    if p:
        print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
    else:
        print("Syntax error: Unexpected end of input")


# Symbol table
symbol_table = {}

# Lexer instance
lexer = lex.lex()

# Parser instance
parser = yacc.yacc()


def process_input(input_text):
    result = parser.parse(input_text, lexer=lexer)
    if result is not None:
        print(result)


process_input("")
# process_input("""


#      a = 12;
#      b = a;
#     """)
