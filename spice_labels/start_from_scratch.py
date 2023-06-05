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

def p_start_empty(p):
    'start : empty'
    pass

def p_start_statement(p):
    'start : assignment_statement'
    pass

def p_start_action_statement(p):
    'start : action_statement'
    pass


def p_empty(p):
    'empty :'
    pass

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression POWER expression
                  | expression LESSTHAN expression
                  | expression LESSEQUAL expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression GREATEREQUAL expression
                  | expression GREATERTHAN expression
                  | expression AND expression
                  | expression OR expression'''
    # Handle binary operators here
    operator = p[2]
    left_operand = p[1]
    right_operand = p[3]
    p[0] = f"{left_operand} {operator} {right_operand}"
    print("Binary Operation: {} {} {}".format(left_operand, operator, right_operand))

def p_expression_unary(p):
    '''expression : NOT expression'''
    # Handle unary operator here
    operator = p[1]
    operand = p[2]
    print("Unary Operation: {}{}".format(operator, operand))


def p_expression(p):
    '''expression : NUMBER
                  | ID'''
    if p.slice[1].type == 'NUMBER':
        p[0] = p[1]
        pass
    else:  # Symbolic expression
        p[0] = p[1]
        # symbol = p[1]
        # if symbol in symbol_table:
        #     p[0] = symbol_table[symbol]
        # else:
        #     print("Error: Symbol '{}' is undefined".format(symbol))
        #     p[0] = None

def p_statement_assign(p):
    'assignment_statement : ID ASSIGN expression SEMICOLON'
    symbol = p[1]
    value = p[3]
    symbol_table[symbol] = value
    print("Assignment: {} = {}".format(symbol, value)) 


# def p_action_statement_module_call(p):
#     'action_statement : ID LPAREN parameter_values RPAREN action_end'
#     module_name = p[1]
#     parameters = p[3]
#     print("Module Call: {}({})".format(module_name, parameters))

# def p_parameter_values(p):
#     '''parameter_values : expression
#                         | expression COMMA parameter_values'''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = [p[1]] + p[3]

# def p_parameter_values_single(p):
#     'parameter_values : parameter_value'
#     p[0] = [p[1]]

# def p_parameter_value_with_name(p):
#     'parameter_value : ID ASSIGN expression'
#     parameter_name = p[1]
#     parameter_value = p[3]
#     p[0] = (parameter_name, parameter_value)


def p_error(p):
    if p:
        print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
    else:
        print("Syntax error: Unexpected end of input")

# Symbol table
symbol_table = {}


parser = yacc.yacc()

def process_input(input_text):

    # Lexer instance
    lexer = lex.lex()

    # Parser instance    
    lexer.input(input_text)

    # Print the generated tokens
    for token in lexer:
        print(token)

    print(parser.parse(input_text, lexer=lexer))


process_input("")
process_input("""
     a = 12; 
     b = 13;
     c = a;
     d = a + 12;
     can(d=12, h=13);

    """)
              