import ply.lex as lex
import ply.yacc as yacc
import re


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
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON', 
    'COMMENT', 
    'BLOCKCOMMENT', 
    'INCLUDE_STATEMENT', 
    'USE_STATEMENT',
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters
t_ignore = ' \t'  


# Token regex definitions
t_BLOCKCOMMENT = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'



# Line comment handling
def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_INCLUDE_STATEMENT(t):
    r'include\s+<[^*?<>]*>'
    match = re.match(r'include\s+<([^*?<>]*)>', t.value)
    t.value = match.groups(0)[0] 
    return t


def t_USE_STATEMENT(t):
    r'use\s+<[^*?<>]*>'
    match = re.match(r'use\s+<([^*?<>]*)>', t.value)
    t.value = match.groups(0)[0] 
    return t


# Token handlers
def t_NUMBER(t):
    r'[-+]?\d+(\.\d+)?([eE][-+]?\d+)?'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t




t_EQUALS = r'='
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

  

# Error handler
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Grammar rules

def p_start(p):
    '''start : empty
             | assignment_statement
             | action_statement
             | line_comment
             | block_comment             
             | module_definition
             | function_definition
             | include_statement
             | use_statement'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass


def p_statement_assign(p):
    'assignment_statement : ID EQUALS expression SEMICOLON'
    symbol = p[1]
    value = p[3]
    symbol_table[symbol] = value
    print("Assignment: {} = {}".format(symbol, value)) 

def p_action_statement(p):
    'action_statement : ID LPAREN parameter_values RPAREN action_end'
    module_name = p[1]
    parameter_values = p[3]
    print("Action statement: {}({})".format(module_name, parameter_values))    


def p_line_comment(p):
    '''line_comment : COMMENT'''
    pass 

def p_block_comment(p):
    '''block_comment : BLOCKCOMMENT'''
    # Your logic to handle block comments goes here
    p[0] = p[1]  # Store the block comment text in p[0]

def p_module_definition(p):
    '''module_definition : ID parameter_list LBRACE RBRACE'''
    pass

def p_function_definition(p):
    'function_definition : ID parameter_list EQUALS expression SEMICOLON'
    # Your logic to handle function definition goes here
    print("Function definition:", p[1], p[3], "=", p[6])

def p_include_statement(p):
    'include_statement : INCLUDE_STATEMENT'
    filepath = p[1]
    # Handle the include statement here
    print("Include: {}".format(filepath))

def p_use_statement(p):
    'use_statement : USE_STATEMENT'
    filepath = p[1]
    # Handle the use statement here
    print("Use: {}".format(filepath))

def p_parameter_list(p):
    '''parameter_list : LPAREN parameter_item_list RPAREN
                      | LPAREN RPAREN'''
    # Your logic to handle parameter list goes here
    if len(p) == 4:
        p[0] = p[2]  # If parameters are present, assign them to p[0]
    else:
        p[0] = []  # Empty parameter list

def p_parameter_item_list(p):
    '''parameter_item_list : parameter_item
                           | parameter_item_list COMMA parameter_item'''
    # Your logic to handle multiple parameter items goes here
    if len(p) == 2:
        p[0] = [p[1]]  # Single parameter item
    else:
        p[0] = p[1] + [p[3]]  # Concatenate parameter items

def p_parameter_item(p):
    '''parameter_item : ID
                      | ID EQUALS expression'''
    # Your logic to handle a parameter item goes here
    if len(p) == 2:
        p[0] = (p[1], None)  # Parameter without default value
    else:
        p[0] = (p[1], p[3])  # Parameter with default value




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

 

def p_parameter_values(p):
    '''parameter_values : expression
                        | expression COMMA parameter_values'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_action_end_semicolon(p):
    'action_end : SEMICOLON'
    pass


def p_action_end_block(p):
    'action_end : LBRACE start RBRACE'
    pass        


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


# # Empty 
# process_input("")
# # Single numeric assignment
# process_input("""
#      a = 12; 
#     """)


# Include statement syntax
process_input("include <ScadStoicheia/centerable.scad>");
process_input("
use <ScadStoicheia/visualization.scad>
# # Multiple numeric assignment
# process_input("""
#      a = 12; 
#      b = 13;
#     """)
#     #  "
#     #  can(d, h);

#     # """)
              