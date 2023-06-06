import ply.lex as lex
import ply.yacc as yacc
import re


tokens = (
    'ID',
    'LPAREN',
    'RPAREN',
    'SEMICOLON', 
    'COMMA',
    'EQUALS',          
    )


# Token handlers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_EQUALS = r'='

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters
t_ignore = ' \t'  

def t_error(t):
    global error_count
    error_count += 1
    if error_count >= 5:
        raise Exception("Too many errors. Parsing stopped.")
    else:
        print("Syntax error at line {}: Unexpected token {}".format(t.lineno, t.type))
        t.lexer.skip(1)  


# Grammar rules

def p_start(p):
    '''start : empty
             | statement start'''
    p[0] = p[1]  # Optional handling of the current statement 

def p_empty(p):
    'empty :'
    pass  

def p_statement(p):
    '''statement : module_call'''   

def p_module_call(p):
    'module_call : ID  parameter_values  SEMICOLON'
    module_name = p[1]
    parameter_values = p[2]
    print("Module statement: {}({})".format(module_name, parameter_values))         

def p_parameter_values(p):
    '''parameter_values : LPAREN parameter_value_list RPAREN'''
    p[0] = p[2]

def p_parameter_value_list(p):
    '''parameter_value_list : parameter_value
                            | parameter_value_list COMMA parameter_value'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

          


error_count = 0  # Counter for tracking the number of errors

def p_error(p):
    global error_count
    error_count += 1
    if error_count >= 1:
        raise Exception("Too many errors. Parsing stopped.")
    else:
        if p:
            print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
        else:
            print("Syntax error: Unexpected end of input")       

parser = yacc.yacc()

def process_input(input_text):
    global error_count
    error_count = 0

    # Lexer instance
    lexer = lex.lex()

    # Parser instance    
    lexer.input(input_text)

    # Print the generated tokens
    for token in lexer:
        print(token)

    print(parser.parse(input_text, lexer=lexer)) 


process_input(              
"""
filament(false);
pure_vitamin_slide(BEHIND); 
spokes();   
"""  
)    

"""
ModuleCall(name='filament', parameter_values=['false'])
ModuleCall(name='pure_vitamin_slide', parameter_values=['BEHIND']); 
ModuleCall(name='spokes', parameter_values=[]); 
"""
