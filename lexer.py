import re

line = raw_input()
count = 1
state = 0

reserved_words = {
	'log': 1,
	'true': 1,
	'false': 1,
	'importar': 1,
	'math': 1,
	'sqrt': 1,
	'fabs': 1,
	'pow': 1,
	'cos': 1,
	'sin': 1,
	'pi': 1,
	'e': 1,
	'for': 1,
	'in': 1,
	'funcion': 1,
	'retorno': 1,
	'end': 1,
}

def delta(lexema, column, line, state, c):
	if state == 0:
		if c == '{':
			print "<token_llave_izq,%d,%d>" %(line,column)
			return (0,0)
		elif c == '}':
			print "<token_llave_der,%d,%d>" %(line,column)
			return (0,0)
		elif c == '#':
			print "<token_com,%d,%d>" %(line,column)
			return (0,0)
		elif c == '[':
			print "<token_cor_izq,%d,%d>" %(line,column)
			return (0,0)
		elif c == ']':
			print "<token_cor_der,%d,%d>" %(line,column)
			return (0,0)
		elif c == '(':
			print "<token_par_izq,%d,%d>" %(line,column)
			return (0,0)
		elif c == ')':
			print "<token_par_der,%d,%d>" %(line,column)
			return (0,0)
		elif c == '.':
			print "<token_point,%d,%d>" %(line,column)
			return (0,0)
		elif c == '+':
			print "<token_mas,%d,%d>" %(line,column)
			return (0,0)
		elif c == '-':
			print "<token_menos,%d,%d>" %(line,column)
			return (0,0)
		elif c == '*':
			print "<token_mul,%d,%d>" %(line,column)
			return (0,0)
		elif c == '/':
			print "<token_div,%d,%d>" %(line,column)
			return (0,0)
		elif c == '%':
			print "<token_mod,%d,%d>" %(line,column)
			return (0,0)
		elif c == '^':
			print "<token_pot,%d,%d>" %(line,column)
			return (0,0)
		elif c == '>':
			return (1,0)
		elif c == '<':
			return (2,0)
		elif c == '=':
			return (3,0)
		elif c == '&':
			return (4,0)
		elif c == '|':
			return (5,0)
		elif c == '!':
			return (6,0)
		elif re.match(r'[0-9]', c):
			return (7,0)
		elif re.match(r'[a-z]', c):
			if lexema+c in reserved_words:
				print "<%s,%d,%d>" %(lexema+c,line,column)
				return (11,0)
			else:
				return (10,0)

	if state == 1:
		if c == '=':
			print "<token_mayor_igual,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "<token_mayor,%d,%d>" %(line,column)
			return (0,1)

	if state == 2:
		if c == '=':
			print "<token_menor_igual,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "<token_menor,%d,%d>" %(line,column)
			return (0,1)

	if state == 3:
		if c == '=':
			print "<token_igual_num,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "<token_assign,%d,%d>" %(line,column)
			return (0,1)

	if state == 4:
		if c == '&':
			print "<token_and,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "Error lexico(linea:%d, posicion:%d)" %(line,column)
			return (-1,0)

	if state == 5:
		if c == '=':
			print "<token_mayor_igual,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "<token_mayor,%d,%d>" %(line,column)
			return (0,1)

	if state == 6:
		if c == '=':
			print "<token_diff_num,%d,%d>" %(line,column)
			return (0,0)
		else:
			print "<token_not,%d,%d>" %(line,column)
			return (0,1)

	if state == 7:
		if re.match(r'[0-9]', c):
			return (7,0)
		elif c == '.':
			return (8,0)
		else:
			print "<token_integer,lexema,%d,%d" %(line, column)
			return(0,1)

	if state == 8:
		if re.match(r'[0-9]', c):
			return(9,0)
		else:
			print "<token_integer,lexema,%d,%d" %(line, column)
			return(0,2)

	if state == 9:
		if re.match(r'[0-9]', c):
			return(9,0)
		else:
			print "<token_float,lexema,%d,%d" %(line, column)
			return(0,1)

	if state == 10:
		if re.match(r'[0-9]', c):
			return(9,0)
		else:
			print "<token_float,lexema,%d,%d" %(line, column)
			return(0,1)

while len(line):

	for i in xrange(len(line)): 
		if line[i] == " ":
			continue
		


	count += 1