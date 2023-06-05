
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLYDIVIDEMODULOleftPOWERnonassocLESSTHANLESSEQUALEQUALNOTEQUALGREATEREQUALGREATERTHANleftANDleftORrightNOTAND ASSIGN COMMA COMMENT DIVIDE EQUAL GREATEREQUAL GREATERTHAN ID LBRACE LESSEQUAL LESSTHAN LPAREN MINUS MODULO MULTIPLY NOT NOTEQUAL NUMBER OR PLUS POWER RBRACE RPAREN SEMICOLONstart : emptystart : assignment_statement\n             | start assignment_statementempty :expression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULTIPLY expression\n                  | expression DIVIDE expression\n                  | expression MODULO expression\n                  | expression POWER expression\n                  | expression LESSTHAN expression\n                  | expression LESSEQUAL expression\n                  | expression EQUAL expression\n                  | expression NOTEQUAL expression\n                  | expression GREATEREQUAL expression\n                  | expression GREATERTHAN expression\n                  | expression AND expression\n                  | expression OR expressionexpression : NOT expressionexpression : NUMBER\n                  | IDassignment_statement : ID ASSIGN expression SEMICOLON'
    
_lr_action_items = {'ID':([0,1,2,3,5,6,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[4,4,-1,-2,-3,7,7,-22,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'$end':([0,1,2,3,5,11,],[-4,0,-1,-2,-3,-22,]),'ASSIGN':([4,],[6,]),'NOT':([6,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'NUMBER':([6,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'SEMICOLON':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,11,-20,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'PLUS':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,12,-20,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'MINUS':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,13,-20,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'MULTIPLY':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,14,-20,-19,14,14,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'DIVIDE':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,15,-20,-19,15,15,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'MODULO':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,16,-20,-19,16,16,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'POWER':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,17,-20,-19,17,17,17,17,17,-10,-11,-12,-13,-14,-15,-16,-17,-18,]),'LESSTHAN':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,18,-20,-19,18,18,18,18,18,18,None,None,None,None,None,None,-17,-18,]),'LESSEQUAL':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,19,-20,-19,19,19,19,19,19,19,None,None,None,None,None,None,-17,-18,]),'EQUAL':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,20,-20,-19,20,20,20,20,20,20,None,None,None,None,None,None,-17,-18,]),'NOTEQUAL':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,21,-20,-19,21,21,21,21,21,21,None,None,None,None,None,None,-17,-18,]),'GREATEREQUAL':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,22,-20,-19,22,22,22,22,22,22,None,None,None,None,None,None,-17,-18,]),'GREATERTHAN':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,23,-20,-19,23,23,23,23,23,23,None,None,None,None,None,None,-17,-18,]),'AND':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,24,-20,-19,24,24,24,24,24,24,24,24,24,24,24,24,-17,-18,]),'OR':([7,8,10,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,],[-21,25,-20,-19,25,25,25,25,25,25,25,25,25,25,25,25,25,-18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'empty':([0,],[2,]),'assignment_statement':([0,1,],[3,5,]),'expression':([6,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,],[8,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> empty','start',1,'p_start_empty','start_from_scratch.py',100),
  ('start -> assignment_statement','start',1,'p_start','start_from_scratch.py',104),
  ('start -> start assignment_statement','start',2,'p_start','start_from_scratch.py',105),
  ('empty -> <empty>','empty',0,'p_empty','start_from_scratch.py',110),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','start_from_scratch.py',114),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','start_from_scratch.py',115),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_binop','start_from_scratch.py',116),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','start_from_scratch.py',117),
  ('expression -> expression MODULO expression','expression',3,'p_expression_binop','start_from_scratch.py',118),
  ('expression -> expression POWER expression','expression',3,'p_expression_binop','start_from_scratch.py',119),
  ('expression -> expression LESSTHAN expression','expression',3,'p_expression_binop','start_from_scratch.py',120),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression_binop','start_from_scratch.py',121),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','start_from_scratch.py',122),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_binop','start_from_scratch.py',123),
  ('expression -> expression GREATEREQUAL expression','expression',3,'p_expression_binop','start_from_scratch.py',124),
  ('expression -> expression GREATERTHAN expression','expression',3,'p_expression_binop','start_from_scratch.py',125),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','start_from_scratch.py',126),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','start_from_scratch.py',127),
  ('expression -> NOT expression','expression',2,'p_expression_unary','start_from_scratch.py',136),
  ('expression -> NUMBER','expression',1,'p_expression','start_from_scratch.py',144),
  ('expression -> ID','expression',1,'p_expression','start_from_scratch.py',145),
  ('assignment_statement -> ID ASSIGN expression SEMICOLON','assignment_statement',4,'p_statement_assign','start_from_scratch.py',159),
]