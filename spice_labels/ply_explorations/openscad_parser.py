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
#t_ignore = ' \t\n'
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

# Lexer instance
lexer = lex.lex()

# Grammar rules


  

# def p_expression_binop(p):
#     '''expression : expression PLUS expression
#                   | expression MINUS expression'''
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]



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
    print("Binary Operation: {} {} {}".format(left_operand, operator, right_operand))

def p_expression_unary(p):
    '''expression : NOT expression'''
    # Handle unary operator here
    operator = p[1]
    operand = p[2]
    print("Unary Operation: {}{}".format(operator, operand))

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_argument_list(p):
    '''argument_list : empty
                     | expression
                     | parameter_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1]

def p_parameter_list(p):
    '''parameter_list : empty
                      | parameter
                      | parameter COMMA parameter_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_parameter(p):
    '''parameter : ID
                 | ID ASSIGN expression'''
    if len(p) == 2:
        p[0] = (p[1], None)  # Parameter without default value
    else:
        p[0] = (p[1], p[3])  # Parameter with default value


def p_action_statement_module_call(p):
    'action_statement : ID LPAREN parameter_values RPAREN module_ending'
    module_name = p[1]
    parameters = p[3]
    print("Module Call: {}({})".format(module_name, parameters))

def p_parameter_values(p):
    'parameter_values : parameter_values COMMA parameter_value'
    p[0] = p[1] + [p[3]]

def p_parameter_values_single(p):
    'parameter_values : parameter_value'
    p[0] = [p[1]]

def p_parameter_value_with_name(p):
    'parameter_value : ID ASSIGN expression'
    parameter_name = p[1]
    parameter_value = p[3]
    p[0] = (parameter_name, parameter_value)

def p_module_ending_semicolon(p):
    'module_ending : SEMICOLON'
    pass

def p_module_ending_module_call(p):
    'module_ending : action_statement'
    pass

def p_module_ending_block(p):
    'module_ending : LBRACE module_statements RBRACE'
    pass

def p_module_statements(p):
    'module_statements : module_statements action_statement'
    pass

def p_module_statements_single(p):
    'module_statements : action_statement'
    pass

def p_statement_assign(p):
    'assignment_statement : ID ASSIGN expression SEMICOLON'
    # Handle assignment here
    print("Assignment: {} = {}".format(p[1], p[3]))    

def p_expression_func_call(p):
    'expression : ID LPAREN argument_list RPAREN'
    # Handle function call here
    function_name = p[1]
    arguments = p[3]
    print("Function Call: {}({})".format(function_name, arguments))    

def p_function_definition(p):
    'function_definition : ID LPAREN argument_list RPAREN ASSIGN expression SEMICOLON'
    # Handle function definition here
    print("Function Definition: {}({}) = {}".format(p[1], p[3], p[6]))    


def p_module_definition(p):
    'module_definition : ID LPAREN argument_list RPAREN LBRACE module_body RBRACE'
    # Handle module definition here
    print("Module Definition: {} ({})".format(p[1], p[3]))    

def p_argument_list(p):
    '''argument_list : ID
                     | ID COMMA argument_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]       

# def p_module_body(p):
#     'module_body : COMMENT'
#     # Handle module body here
#     print("Module Body: {}".format(p[1]))

def p_top_level_statement(p):
    '''top_level_statement : statement
                           | module_definition
                           | function_definition'''
    p[0] = p[1]

 
    
def p_module_body(p):
    '''module_body : empty
                   | module_body statement
                   | module_body module_definition
                   | module_body top_level_statement
                   | module_body function_definition'''
    if len(p) == 2:
        p[0] = []  # Empty module body
    else:
        # p[0] = p[1] + [p[2]]  # Concatenate module body statements
        p[0] = p[1] + ([p[2]] if p[2] is not None else []) 


     

def p_error(p):
    if p:
        print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
    else:
        print("Syntax error: Unexpected end of input")

def p_empty(p):
    'empty :'
    pass    

# Parser instance
parser = yacc.yacc()

# Test inputs
result = parser.parse("")
print("Result", result)
result = parser.parse("// Joe is really great")
print("Result", result)
result = parser.parse("a = 1;")
print("Result", result)

# Output
print("Parsing complete.")



input_text = """
// This is a comment


x = 5 + 3;  // This is a comment too!
module myModule() {
    // Module body
}

module takes_args(a, b, c, d) {

}

myModule();

myModule() takes_args

"""

# Parsing
#result = parser.parse(input_text)


