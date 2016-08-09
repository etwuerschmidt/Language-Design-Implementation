from __future__ import division
import sys
sys.setrecursionlimit(2000)

from collections import OrderedDict

#Wrapper for expressions
class Exp:
	def __init__(self):
		self

#Wrapper for Cool Values
class Cool_Value:
	def __init__(self):
		self

#Holds environment as a dictionary
class Environment:
	def __init__(self, attrs):
		self.attrs = attrs

	def __repr__(self):
		return "%s" % (self.attrs)

#Holds store as a dictionary
class Store:
	def __init__(self, vals):
		self.vals = vals

	def __repr__(self):
		return "%s" % (self.vals)

#Cool Object -> Type of Cool Value
class Cool_Object(Cool_Value):
	def __init__(self, cname, attrs):
		self.cname = cname
		self.attrs = attrs

	def __repr__(self):
		return "%s(%s)" % (self.cname, self.attrs)

#Cool Int -> Type of Cool Object
class Cool_Int(Cool_Object):
	def __init__(self, i):
		self.cname = "Int"
		self.attrs = []
		self.i = i

	def __repr__(self):
		return "Int(%d)" % self.i

#Cool Bool -> Type of Cool Object
class Cool_Bool(Cool_Object):
	def __init__(self, b):
		self.cname = "Bool"
		self.attrs = []
		self.b = b

	def __repr__(self):
		return "Bool(%s)" % self.b

#Cool String -> Type of Cool Object
class Cool_String(Cool_Object):
	def __init__(self, s):
		self.cname = "String"
		self.attrs = OrderedDict()
		self.i = len(s)
		self.s = s

	def __repr__(self):
		return "String(%d, %s)" % (self.i, self.s)

#Void -> Type of Cool Object
class Void(Cool_Value):
	def __init__(self):
		self

	def __repr__(self):
		return "Void"

#Address of a Cool Object
class Cool_Address:
	def __init__(self, i):
		self.i = i

#Class for new expressions
class New(Exp):
	def __init__(self, cname, line):
		self.cname = cname
		self.line = line

	def __repr__(self):
		return "New(%s)" % (self.cname)

#Class for dynamic and self dispatch
class Dispatch(Exp):
	def __init__(self, ro, fname, args, line):
		self.ro = ro
		self.fname = fname
		self.args = args
		self.line = line

	def __repr__(self):
		return "Dispatch(%s, %s, %s)" % (self.ro, self.fname, self.args)

#Class for static dispatch
class StaticDispatch(Exp):
	def __init__(self, ro, typ, fname, args, line):
		self.ro = ro
		self.typ = typ
		self.fname = fname
		self.args = args
		self.line = line

	def __repr__(self):
		return "Dispatch(%s, %s, %s, %s)" % (self.ro, self.typ, self.fname, self.args)

#Class for variables
class Variable(Exp):
	def __init__(self, vname):
		self.vname = vname

	def __repr__(self):
		return "Variable(%s)" % (self.vname)

#Class for assignment statements
class Assign(Exp):
	def __init__(self, vname, rhs):
		self.vname = vname
		self.rhs = rhs

	def __repr__(self):
		return "Assign(%s, %s)" % (self.vname, self.rhs)

#Class for integers -> NOT Cool Ints
class Integer(Exp):
	def __init__(self, i):
		self.i = i

	def __repr__(self):
		return "Integer(%s)" % self.i

#Class for strings -> NOT Cool Strings
class String(Exp):
	def __init__(self, s):
		self.s = s

	def __repr__(self):
		return "String(%s)" % self.s

#Class for bools -> NOT Cool Bools
class Bool(Exp):
	def __init__(self, b):
		self.b = b

	def __repr__(self):
		return "Bool(%s)" % self.b

#Class for if expressions
class If(Exp):
	def __init__(self, pred, t, el):
		self.pred = pred
		self.t = t
		self.el = el

	def __repr__(self):
		return "If(%s) then(%s) else(%s) fi" % (self.pred, self.t, self.el)

#Class for block expressions
class Block(Exp):
	def __init__(self, seq):
		self.seq = seq

	def __repr__(self):
		return "Block(%s)" % (self.seq)

#Class for while loops
class While(Exp):
	def __init__(self, pred, loop):
		self.pred = pred
		self.loop = loop

	def __repr__(self):
		return "While(%s) loop(%s) pool" % (self.pred, self.loop)

#Class for plus expression
class Plus(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "Plus(%s, %s)" % (self.e1, self.e2)

#Class for minus expression
class Minus(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "Minus(%s, %s)" % (self.e1, self.e2)

#Class for times expression
class Times(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "Times(%s, %s)" % (self.e1, self.e2)

#Class for divides expression
class Divide(Exp):
	def __init__(self, e1, e2, line):
		self.e1 = e1
		self.e2 = e2
		self.line = line

	def __repr__(self):
		return "Divide(%s, %s)" % (self.e1, self.e2)

#Class for equals expression
class Equals(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "Equals(%s, %s)" % (self.e1, self.e2)

#Class for less than expression
class LessThan(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "LessThan(%s, %s)" % (self.e1, self.e2)

#Class for less than equal expression
class LessThanEqual(Exp):
	def __init__(self, e1, e2):
		self.e1 = e1
		self.e2 = e2

	def __repr__(self):
		return "LessThanEqual(%s, %s)" % (self.e1, self.e2)

#Class for isvoid expression
class IsVoid(Exp):
	def __init__(self, e1):
		self.e1 = e1

	def __repr__(self):
		return "Isvoid(%s)" % (self.e1)

#Class for not expression
class Not(Exp):
	def __init__(self, e1):
		self.e1 = e1

	def __repr__(self):
		return "Not(%s)" % (self.e1)

#Class for not expression
class Neg(Exp):
	def __init__(self, e1):
		self.e1 = e1

	def __repr__(self):
		return "Neg(%s)" % (self.e1)

#Class for case expression
class Case(Exp):
	def __init__(self, e0, elem, line):
		self.e0 = e0
		self.elem = elem
		self.line = line

	def __repr__(self):
		return "Case(%s) of(%s) esac" % (self.e0, self.elem)

#Class for let expression
class Let(Exp):
	def __init__(self, bind, body):
		self.bind = bind
		self.body = body

	def __repr__(self):
		return "Let(%s) in (%s)" % (self.bind, self.body)

#Class for built in object method abort
class Abort():
	def __init__(self):
		self 

	def __repr__(self):
		return "Abort()"

#Class for built in object method typename
class TypeName():
	def __init__(self):
		self 

	def __repr__(self):
		return "TypeName"

#Class for built in object method copy
class Copy():
	def __init__(self):
		self  
	def __repr__(self):
		return "Copy"

#Class for built in IO method out_string
class Out_String():
	def __init__(self, x):
		self.val = x

	def __repr__(self):
		return "Out_String(%s)" % self.val

#Class for built in IO method out_int
class Out_Int():
	def __init__(self, x):
		self.val = x

	def __repr__(self):
		return "Out_Int(%s)" % str(self.val)

#Class for built in IO method in_int
class In_Int():
	def __init__(self):
		self

	def __repr__(self):
		return "In_Int"

#Class for built in IO method in_string
class In_String():
	def __init__(self):
		self

	def __repr__(self):
		return "In_String"

#Class for built in String method length
class Length():
	def __init__(self):
		self

	def __repr__(self):
		return "Length()"

#Class for built in String method concat
class Concat():
	def __init__(self, s):
		self.s = s

	def __repr__(self):
		return "Concat(%s)" % (self.s)

#Class for built in STring method substr
class Substr():
	def __init__(self, i, l):
		self.i = i 
		self.l = l 

	def __repr__(self):
		return "Substr(%s, %s)" % (self.i, self.l)

#Open up the annotated ast file
filename = sys.argv[1]
file = open(filename, "r")
file_contents = file.readlines()
file_contents = [x.rstrip('\n') for x in file_contents]
class_map = []
imp_map = []
first_index = 0
second_index = 0
third_index = 0
count = 0
check = False
par_num = 0

base = ["Bool", "Int", "String", "Object"]

#Split up annotated ast file into the three different maps
for f in file_contents:
	if f == "implementation_map":
		first_index = count
	elif f == "parent_map":
		second_index = count
		check = True
	elif check == True:
		par_num = int(f)
		check = False
	else:
		count+=1

#Set maps (of type list) to appropriate file contents
class_map = file_contents[:first_index]
imp_map = file_contents[first_index:second_index+1]
parent_map = file_contents[second_index+3:second_index+2*par_num+3]

#Global vars for iterating through the class map and implementation map to create proper dictionaries
formals = []
class_dict = OrderedDict()
imp_dict = OrderedDict()
parent_dict = OrderedDict()
method_name = ""
curr_class = ""
attr_name = ""
ob = ""
method_link = []

#Turn parent map into a dictionary associating parents with children
parent_dict = dict(zip(parent_map[0::2], parent_map[1::2]))

#Takes in the class map and a worker function and applies the worker function to every member in the map
def read_list(lst, worker):
	num = int(lst.pop(0))
	ret = []
	for i in range(num):
		w = worker(lst)
		ret.append(w)
	return ret

#Read a class in from the class map
def read_class(lst):
	name = lst.pop(0)
	global curr_class
	curr_class = name
	#Within the class map dictionary, associate a class with a new empty dictionary
	class_dict[name] = OrderedDict()
	read_list(lst, read_attr)

#To begin reading the class map
def read_class_map(lst):
	lst.pop(0)
	read_list(lst, read_class)

#Read an expression in from the class map
def read_exp(lst):
	global attr_name
	global ob
	line = lst.pop(0)
	exp_type = lst.pop(0)
	name = lst.pop(0)
	#Create an assignment instance with the variable and its assigned expression (rhs)
	if name == "assign":
		another_line = lst.pop(0)
		var = lst.pop(0)
		rhs = read_exp(lst)
		#Associate the current attribute name with an assignment instance
		class_dict[curr_class][attr_name] = Assign(var, rhs)
		return Assign(var, rhs)

	#Create an integer instance with the value
	if name == "integer":
		val = lst.pop(0)
		#Associate the current attribute name with an integer instance
		class_dict[curr_class][attr_name] = Integer(val)
		return Integer(val)

	#Create a string instance with the value
	if name == "string":
		val = lst.pop(0)
		#Associate the current attribute name with a string instance
		class_dict[curr_class][attr_name] = String(val)
		return String(val)

	#Create a bool instance with the value
	if name == "true" or name == "false":
		val = name
		#Associate the current attribute name with a bool instance
		class_dict[curr_class][attr_name] = Bool(val)
		return Bool(val)

	#Create a plus instance with the two expressions being added
	if name == "plus":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a plus instance
		class_dict[curr_class][attr_name] = Plus(e1, e2)
		return Plus(e1, e2)

	#Create a minus instance with the two expressions being subtracted
	if name == "minus":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a minus instance
		class_dict[curr_class][attr_name] = Minus(e1, e2)
		return Minus(e1, e2)

	#Create a times instance with the two expressions being multiplied
	if name == "times":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a times instance
		class_dict[curr_class][attr_name] = Times(e1, e2)
		return Times(e1, e2)

	#Create a divide instance with the two expressions being divided
	if name == "divide":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a divide instance
		class_dict[curr_class][attr_name] = Divide(e1, e2, line)
		return Divide(e1, e2, line)

	#Create a new instance of the specified class
	if name == "new":
		another_line = lst.pop(0)
		cname = lst.pop(0)
		#If the class name is SELF_TYPE, then create a new instance of the current class
		if cname == "SELF_TYPE":
			cname = curr_class
		#Associate the current attribute name with a new instance
		class_dict[curr_class][attr_name] = New(cname, line)
		return New(cname, line)

	#Create an if instance with the predicate expression, then expression, and else expression
	if name == "if":
		pred = read_exp(lst)
		t = read_exp(lst)
		el = read_exp(lst)
		#Associate the current attribute name with an if instance
		class_dict[curr_class][attr_name] = If(pred, t, el)
		return If(pred, t, el)

	#Create a while instance with the predicate expression and loop expression
	if name == "while":
		pred = read_exp(lst)
		loop = read_exp(lst)
		#Associate the current attribute name with a while instance
		class_dict[curr_class][attr_name] = While(pred, loop)
		return While(pred, loop)

	#Create a block instance with a list of all expressions within the block
	if name == "block":
		seq = read_list(lst, read_exp)
		#Associate the current attribute name with a block instance
		class_dict[curr_class][attr_name] = Block(seq)
		return Block(seq)

	#Create an equals instance with the two expressions being compared
	if name == "eq":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with an equals instance
		class_dict[curr_class][attr_name] = Equals(e1, e2)
		return Equals(e1, e2)

	#Create a less than instance with the two expressions being compared
	if name == "lt":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a less than instance
		class_dict[curr_class][attr_name] = LessThan(e1, e2)
		return LessThan(e1, e2)

	#Create a less than equal instance with the two expressions being compared
	if name == "le":
		e1 = read_exp(lst)
		e2 = read_exp(lst)
		#Associate the current attribute name with a less than equal instance
		class_dict[curr_class][attr_name] = LessThanEqual(e1, e2)
		return LessThanEqual(e1, e2)

	#Create a not instance with the expression the not is applied to
	if name == "not":
		e1 = read_exp(lst)
		#Associate the current attribute name with a not instance
		class_dict[curr_class][attr_name] = Not(e1)
		return Not(e1)

	#Create a negate instance with the expression the negate is applied to
	if name == "negate":
		e1 = read_exp(lst)
		#Associate the current attribute name with a negate instance
		class_dict[curr_class][attr_name] = Neg(e1)
		return Neg(e1)

	#Create an isvoid instance with the expression being checked
	if name == "isvoid":
		e1 = read_exp(lst)
		#Associate the current attribute name with an isvoid instance
		class_dict[curr_class][attr_name] = IsVoid(e1)
		return IsVoid(e1)

	#Create a variable instance with the name of the identifier
	if name == "identifier":
		another_num = lst.pop(0)
		vname = lst.pop(0)
		#Associate the current attribute name with a variable instance
		class_dict[curr_class][attr_name] = Variable(vname)
		return Variable(vname)

	#Create a dispatch instance with the method name and a list of attributes
	if name == "self_dispatch":
		another_line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp)
		#Associate the current attribute name with a dispatch instance (the receiver object here is the current class)
		class_dict[curr_class][attr_name] = Dispatch(curr_class, met_name, attrs, line)
		return Dispatch(curr_class, met_name, attrs, line)

	#Create a disptach instance with the method name, receiver object, and a list of attributes
	if name == "dynamic_dispatch":
		ro = read_exp(lst)
		ob = ro
		line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp)
		#Associate the current attribute name with a dispatch instance
		class_dict[curr_class][attr_name] = Dispatch(ro, met_name, attrs, line)
		return Dispatch(ro, met_name, attrs, line)

	#Create a static dispatch instance with the method name, type, receiver object, and a list of attributes
	if name == "static_dispatch":
		ro = read_exp(lst)
		ob = ro
		line = lst.pop(0)
		typ = lst.pop(0)
		another_line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp)
		#Associate the current attribute name with a static dispatch instance
		class_dict[curr_class][attr_name] = StaticDispatch(ro, typ, met_name, attrs, line)
		return StaticDispatch(ro, typ, met_name, attrs, line)

	#Create a case instance with the initial expression and list of case elements
	if name == "case":
		e0 = read_exp(lst)
		elem = read_list(lst, read_case)
		#Associate the current attribute name with a case instance
		class_dict[curr_class][attr_name] = Case(e0, elem, line)
		return Case(e0, elem, line)

	#Create a let instance with the list of bindings and the let body
	if name == "let":
		bind = read_list(lst, read_let)
		body = read_exp(lst)
		#Associate the current attribute name with a let instance
		class_dict[curr_class][attr_name] = Let(bind, body)
		return Let(bind, body)

	#Create a typename instance
	if name == "type_name":
		#Associate the current attribute name with a typename instance
		class_dict[curr_class][attr_name] = TypeName()
		return TypeName()

	#Create an abort instance
	if name == "abort":
		#Associate the current attribute name with an abort instance
		class_dict[curr_class][attr_name] = Abort()
		return Abort()

	#Create a copy instance
	if name == "copy":
		#Associate the current attribute name with a copy instance
		class_dict[curr_class][attr_name] = Copy()
		return Copy()

	#Create an in_int instance
	if name == "in_int":
		#Associate the current attribute name with an in_int instance
		class_dict[curr_class][attr_name] = In_Int()
		return In_Int()

	#Create an in_string instance
	if name == "in_string":
		#Associate the current attribute name with an in_string instance
		class_dict[curr_class][attr_name] = In_String()
		return In_String()

	#Create a length instance
	if name == "length":
		#Associate the current attribute name with a length instance
		class_map[curr_class][attr_name] = Length()
		return Length()

	#Create a concat instance with the expression to be concatenated
	if name == "concat":
		line = lst.pop(0)
		a = read_exp(lst)
		#Associate the current attribute name with a concat instance
		class_map[curr_class][attr_name] = Concat(a)
		return Concat(a)

	#Create a substr instance with the starting index expression and length expression
	if name == "substr":
		line = lst.pop(0)
		i = read_exp(lst)
		another_line = lst.pop(0)
		l = read_exp(lst)
		#Associate the current attribute name with a substr instance
		class_map[curr_class][attr_name] = Substr(i, l)
		return Substr(i, l)

	else:
		print ("NOT DEFINED: %s" % name)

#Read an attribute in from the class map
def read_attr(lst):
	init = lst.pop(0)
	name = lst.pop(0)
	global attr_name
	global ob
	attr_name = name
	ob = ""
	#Within the current class's dictionary, associate the attribute name with the empty string (to be changed later)
	class_dict[curr_class][attr_name] = ""
	attr_type = lst.pop(0)
	#If the attribute has an initialized value, read it
	if init == "initializer":
		read_exp(lst)
	#Else, store default values for classes with no initializers
	else:
		#Default value of Int is 0
		if attr_type == "Int":
			class_dict[curr_class][attr_name] = Integer(0)
			return Integer(0)
		#Default value of String is the empty string
		if attr_type == "String":
			class_dict[curr_class][attr_name] = String("")
			return String("")
		#Default value of Bool is false
		if attr_type == "Bool":
			class_dict[curr_class][attr_name] = Bool("false")
			return Bool("false")
		#Default value of all other Cool Objects is Void
		else:
			class_dict[curr_class][attr_name] = Void()
			return Void()

#Read an expression in from the class map
def read_exp_imp(lst):
	global curr_class
	global method_name
	global ob
	line = lst.pop(0)
	exp_type = lst.pop(0)
	name = lst.pop(0)

	#Create an assignment instance with the variable and its assigned expression (rhs)
	if name == "assign":
		another_line = lst.pop(0)
		var = lst.pop(0)
		rhs = read_exp_imp(lst)
		#Associate the current method body with an assignment instance
		imp_dict[curr_class][method_name][1] = Assign(var, rhs)
		return Assign(var, rhs)

	#Create an integer instance with the value
	if name == "integer":
		val = lst.pop(0)
		#Associate the current method body with an integer instance
		imp_dict[curr_class][method_name][1] = Integer(val)
		return Integer(val)

	#Create a string instance with the value
	if name == "string":
		val = lst.pop(0)
		#Associate the current method body with a string instance
		imp_dict[curr_class][method_name][1] = String(val)
		return String(val)

	#Create a bool instance with the value
	if name == "true" or name == "false":
		val = name
		#Associate the current method body with a bool instance
		imp_dict[curr_class][method_name][1] = Bool(val)
		return Bool(val)

	#Create an if instance with the predicate expression, then expression, and else expression
	if name == "if":
		pred = read_exp_imp(lst)
		t = read_exp_imp(lst)
		el = read_exp_imp(lst)
		#Associate the current method body with an if instance
		imp_dict[curr_class][method_name][1] = If(pred, t, el)
		return If(pred, t, el)

	#Create a while instance with the predicate expression and loop expression
	if name == "while":
		pred = read_exp_imp(lst)
		loop = read_exp_imp(lst)
		#Associate the current method body with a while instance
		imp_dict[curr_class][method_name][1] = While(pred, loop)
		return While(pred, loop)

	#Create a plus instance with the two expressions being added
	if name == "plus":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a plus instance
		imp_dict[curr_class][method_name][1] = Plus(e1, e2)
		return Plus(e1, e2)

	#Create a minus instance with the two expressions being subtracted
	if name == "minus":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a minus instance
		imp_dict[curr_class][method_name][1] = Minus(e1, e2)
		return Minus(e1, e2)

	#Create a times instance with the two expressions being multiplied
	if name == "times":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a times instance
		imp_dict[curr_class][method_name][1] = Times(e1, e2)
		return Times(e1, e2)

	#Create a divide instance with the two expressions being divided
	if name == "divide":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a divide instance
		imp_dict[curr_class][method_name][1] = Divide(e1, e2, line)
		return Divide(e1, e2, line)

	#Create a new instance of the specified class
	if name == "new":
		another_line = lst.pop(0)
		cname = lst.pop(0)
		#If the class name is SELF_TYPE, then create a new instance of the current class
		if cname == "SELF_TYPE":
			cname = curr_class
		#Associate the current method body with a new instance
		imp_dict[curr_class][method_name][1] = New(cname, line)
		return New(cname, line)

	#Create a block instance with a list of all expressions within the block
	if name == "block":
		seq = read_list(lst, read_exp_imp)
		#Associate the current method body with a block instance
		imp_dict[curr_class][method_name][1] = Block(seq)
		return Block(seq)

	#Create an equals instance with the two expressions being compared
	if name == "eq":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with an equals instance
		imp_dict[curr_class][method_name][1] = Equals(e1, e2)
		return Equals(e1, e2)

	#Create a less than instance with the two expressions being compared
	if name == "lt":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a less than instance
		imp_dict[curr_class][method_name][1] = LessThan(e1, e2)
		return LessThan(e1, e2)

	#Create a less than equal instance with the two expressions being compared
	if name == "le":
		e1 = read_exp_imp(lst)
		e2 = read_exp_imp(lst)
		#Associate the current method body with a less than equal instance
		imp_dict[curr_class][method_name][1] = LessThanEqual(e1, e2)
		return LessThanEqual(e1, e2)

	#Create a not instance with the expression the not is applied to
	if name == "not":
		e1 = read_exp_imp(lst)
		#Associate the current method body with a not instance
		imp_dict[curr_class][method_name][1] = Not(e1)
		return Not(e1)

	#Create a negate instance with the expression the negate is applied to
	if name == "negate":
		e1 = read_exp_imp(lst)
		#Associate the current attribute name with a negate instance
		imp_dict[curr_class][method_name][1] = Neg(e1)
		return Neg(e1)

	#Create an isvoid instance with the expression being checked
	if name == "isvoid":
		e1 = read_exp_imp(lst)
		#Associate the current method body with an isvoid instance
		imp_dict[curr_class][method_name][1] = IsVoid(e1)
		return IsVoid(e1)

	#Create a dispatch instance with the method name and a list of attributes
	if name == "self_dispatch":
		another_line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp_imp)
		#Associate the current method body with a dispatch instance (the receiver object here is the current class)
		imp_dict[curr_class][method_name][1] = Dispatch(curr_class, met_name, attrs, line)
		return Dispatch(curr_class, met_name, attrs, line)

	#Create a disptach instance with the method name, receiver object, and a list of attributes
	if name == "dynamic_dispatch":
		ro = read_exp_imp(lst)
		ob = ro
		line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp_imp)
		#Associate the current method body with a dispatch instance
		imp_dict[curr_class][method_name][1] = Dispatch(ro, met_name, attrs, line)
		return Dispatch(ro, met_name, attrs, line)

	#Create a static dispatch instance with the method name, type, receiver object, and a list of attributes
	if name == "static_dispatch":
		ro = read_exp_imp(lst)
		ob = ro
		line = lst.pop(0)
		typ = lst.pop(0)
		another_line = lst.pop(0)
		met_name = lst.pop(0)
		attrs = read_list(lst, read_exp_imp)
		#Associate the current method body with a static dispatch instance
		imp_dict[curr_class][method_name][1] = StaticDispatch(ro, typ, met_name, attrs, line)
		return StaticDispatch(ro, typ, met_name, attrs, line)

	#Create a variable instance with the name of the identifier
	if name == "identifier":
		another_num = lst.pop(0)
		vname = lst.pop(0)
		#Associate the current method body with a variable instance
		imp_dict[curr_class][method_name][1] = Variable(vname)
		return Variable(vname)

	#Create a case instance with the initial expression and list of case elements
	if name == "case":
		e0 = read_exp_imp(lst)
		elem = read_list(lst, read_case_imp)
		#Associate the current method body with a case instance
		imp_dict[curr_class][method_name][1] = Case(e0, elem, line)
		return Case(e0, elem, line)

	#Create a let instance with the list of bindings and the let body
	if name == "let":
		bind = read_list(lst, read_let_imp)
		body = read_exp_imp(lst)
		#Associate the current method body with a let instance
		imp_dict[curr_class][method_name][1] = Let(bind, body)
		return Let(bind, body)

	#Create an abort instance
	if method_name == "abort":
		lst.pop(0)
		#Associate the current method body with an abort instance
		imp_dict[curr_class][method_name][1] = Abort()
		return Abort()

	#Create a typename instance
	if method_name == "type_name":
		lst.pop(0)
		#Associate the current method body with a typename instance
		imp_dict[curr_class][method_name][1] = TypeName()
		return TypeName()

	#Create a copy instance
	if method_name == "copy":
		lst.pop(0)
		#Associate the current method body with a copy instance
		imp_dict[curr_class][method_name][1] = Copy()
		return TypeName()

	#Create an out_string instance
	if method_name == "out_string":
		lst.pop(0)
		#Associate the current method body with an out_string instance
		imp_dict[curr_class][method_name][1] = Out_String("X")
		#Associate the current method formals with the formals for out_string
		imp_dict[curr_class][method_name][0] = ['X']
		return Out_String("X")

	#Create an out_int instance
	if method_name == "out_int":
		lst.pop(0)
		#Associate the current method body with an out_int instance
		imp_dict[curr_class][method_name][1] = Out_Int("X")
		#Associate the current method formals with the formals for out_int
		imp_dict[curr_class][method_name][0] = ['X']
		return Out_Int("X")

	#Create an in_int instance
	if method_name == "in_int":
		lst.pop(0)
		#Associate the current method body with an in_int instance
		imp_dict[curr_class][method_name][1] = In_Int()
		return In_Int()

	#Create an in_string instance
	if method_name == "in_string":
		lst.pop(0)
		#Associate the current method body with an in_string instance
		imp_dict[curr_class][method_name][1] = In_String()
		return In_String()

	#Create a length instance
	if method_name == "length":
		lst.pop(0)
		#Associate the current method body with a length instance
		imp_dict[curr_class][method_name][1] = Length()
		return Length()

	#Create a concat instance with the expression to be concatenated
	if method_name == "concat":
		lst.pop(0)
		#Associate the current method body with a concat instance
		imp_dict[curr_class][method_name][1] = Concat("S")
		#Associate the current method formals with the formals for concat
		imp_dict[curr_class][method_name][0] = ['S']
		return Concat("S")

	#Create a substr instance with the starting index expression and length expression
	if method_name == "substr":
		line = lst.pop(0)
		#Associate the current method body with a substr instance
		imp_dict[curr_class][method_name][1] = Substr("I", "L")
		#Associate the current method formals with the formals for substr
		imp_dict[curr_class][method_name][0] = ['I', 'L']
		return Substr("I", "L")

	else:
		lst.pop(0)
		return None

#Create a tuple for a case element with the variable, case type, and body expression
def read_case(lst):
	line = lst.pop(0)
	var = lst.pop(0)
	another_line = lst.pop(0)
	case_type = lst.pop(0)
	body = read_exp(lst) 
	return (var, case_type, body)

#Create a tuple for a case element with the variable, case type, and body expression
def read_case_imp(lst):
	line = lst.pop(0)
	var = lst.pop(0)
	another_line = lst.pop(0)
	case_type = lst.pop(0)
	body = read_exp_imp(lst)
	return (var, case_type, body)

#Create a tuple for a let element with the variable, let type, and assignment (body) expression
def read_let(lst):
	bind_init = lst.pop(0)
	#If the let element has an assignment (body), read it
	if bind_init == "let_binding_init":
		line = lst.pop(0)
		var = lst.pop(0)
		another_line = lst.pop(0)
		let_type = lst.pop(0)
		body = read_exp(lst)
	#Else set the body to a default value
	else:
		line = lst.pop(0)
		var = lst.pop(0)
		another_line = lst.pop(0)
		let_type = lst.pop(0)
		#Default value for Ints is 0
		if let_type == "Int":
			body = Integer(0)
		#Default value for Strings is the empty string
		elif let_type == "String":
			body = String("")
		#Default value for Bools is false
		elif let_type == "Bool":
			body = Bool("false")
		#Default value for all other Cool Objects is void
		else:
			let_type = Void()
	return (var, let_type, body)

#Create a tuple for a let element with the variable, let type, and assignment (body) expression
def read_let_imp(lst):
	bind_init = lst.pop(0)
	#If the let element has an assignment (body), read it
	if bind_init == "let_binding_init":
		line = lst.pop(0)
		var = lst.pop(0)
		another_line = lst.pop(0)
		let_type = lst.pop(0)
		body = read_exp_imp(lst)
	#Else set the body to a default value
	else:
		line = lst.pop(0)
		var = lst.pop(0)
		another_line = lst.pop(0)
		let_type = lst.pop(0)
		#Default value for Ints is 0
		if let_type == "Int":
			body = Integer(0)
		#Default value for Strings is the empty string
		elif let_type == "String":
			body = String("")
		#Default value for Bools is false
		elif let_type == "Bool":
			body = Bool("false")
		#Default value for all other Cool Objects is void
		else:
			body = Void()
	return (var, let_type, body)

#Read in method formals from the implementation map
def read_formals(lst):
	global formals
	#Within the list associated to the current method, change the first parameter (the empty list) to be the list of formals for the current method
	imp_dict[curr_class][method_name][0].append(lst.pop(0))
	return formals

#Read in a method from the implementation map
def read_methods(lst):
	name = lst.pop(0)
	global method_name, curr_class, formals
	method_name = name
	#Within the objects dictionary, associate a method with a list of an empty list of formals and a body of none (both to be changed later)
	imp_dict[curr_class][method_name] = [[], None]
	read_list(lst, read_formals)
	inherited_class = lst.pop(0)
	read_exp_imp(lst)

#Read in an object from the implementation map
def read_obj(lst):
	name = lst.pop(0)
	global curr_class
	curr_class = name
	#Within the imp map dictionary, associate an object with a new empty dictionary
	imp_dict[name] = OrderedDict()
	read_list(lst, read_methods)

#To begin reading the imp map
def read_imp_map(lst):
	lst.pop(0)
	read_list(lst, read_obj)

#Read all maps and change the naming conventions
read_class_map(class_map)

read_imp_map(imp_map)

class_map = class_dict

imp_map = imp_dict

parent_map = parent_dict


#Counter for activation records
act_rec = 0

#Counter for location
loc_counter = 1000

#Creates a new location by adding one to the location counter
def newloc():
	global loc_counter
	loc_counter+=1
	return loc_counter

#For debugging - changes the indent for nested eval statements
indent_count = 0
def debug_indent():
	x = ' '
	#for i in range(0, indent_count):
	#	print x,

#Method for evaluating an op sem - takes in self object (so), store (s), environment (e), and expression (exp)
def eval(so, s, e, exp):
	global indent_count
	global act_rec
	indent_count += 1
	new_value = None
	new_store = None
	#Indent for new eval statement
	#print
	debug_indent()
	#print "eval: %s" % exp
	debug_indent()
	#print "self: %s" % so
	debug_indent()
	#print "sto = %s" % s
	debug_indent()
	#print "env = %s" % e
	#Add one to the activation record
	act_rec += 1
	#If there are 1000 or more outstanding activation records, throw a stack overflow error
	if act_rec > 999:
		print "ERROR: %s: Exception: stack overflow" % (exp.line)
		exit(1)
	#so, S, E |- i: Int(i), S
	if isinstance(exp, Integer):
		#exp.i is integer constant
		new_value = Cool_Int(int(exp.i))
		new_store = s
	#so, S, E |- s: String(l, s), S
	elif isinstance(exp, String):
		#exp.s is string constant, length automatically calculated once initialized
		new_value = Cool_String(exp.s)
		new_store = s
	#so, S, E |- b: Bool(b), S
	elif isinstance(exp, Bool):
		#exp.b is bool constant
		new_value = Cool_Bool(exp.b)
		new_store = s
	#Void expressions should remain void with no change to the store
	elif isinstance(exp, Void):
		new_value = exp
		new_store = s
	elif isinstance(exp, If):
		#so, S1, E |- e1: Bool(true), S2
		pred = eval(so, s, e, exp.pred)
		if pred[0].b == "true":
			#so, S2, E |- e2: v2, S3
			then = eval(so, pred[1], e, exp.t)
			new_value = then[0]
			new_store = then[1]
		#so, S1, E |- e1: Bool(false), S2
		else:
			#so, S2, E |- e3: v3, S3
			el = eval(so, pred[1], e, exp.el)
			new_value = el[0]
			new_store = el[1]
	elif isinstance(exp, While):
		#so, S1, E |- e1: Bool(true), S2
		pred = eval(so, s, e, exp.pred)
		if pred[0].b == "true":
			#so, S2, E |- e2: v2, S3
			loop = eval(so, pred[1], e, exp.loop)
			#so, S3, E |- while e1 loop e2 pool : void, S4
			(new_value, new_store) = eval(so, loop[1], e, exp)
		#so, S1, E |- e1: Bool(false), S2
		else:
			new_value = Void()
			new_store = pred[1]
	elif isinstance(exp, Plus):
		#so, S1, E |- e1 : Int(i1), S2
		first = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: Int(i2), S3
		second = eval(so, first[1], e, exp.e2)
		#v1 = Int(i1 + i2)
		result_val = first[0].i + second[0].i
		#Ensure 32 bit arithmetic using two's compliment
		b = int(0xFFFFFFFF);
		if result_val > 2147483647:
			flip = result_val
			result_val = -((b ^ flip)+1)
		elif result_val < -2147483647:
			flip = result_val
			result_val = -((b^flip)+1)
		new_value = Cool_Int(int(result_val))
		new_store = second[1]
	elif isinstance(exp, Minus):
		#so, S1, E |- e1 : Int(i1), S2
		first = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: Int(i2), S3
		second = eval(so, first[1], e, exp.e2)
		#v1 = Int(i1 - i2)
		result_val = first[0].i - second[0].i
		#Ensure 32 bit arithmetic using two's compliment
		b = int(0xFFFFFFFF);
		if result_val > 2147483647:
			flip = result_val
			result_val = -((b ^ flip)+1)
		elif result_val < -2147483647:
			flip = result_val
			result_val = -((b^flip)+1)
		new_value = Cool_Int(int(result_val))
		new_store = second[1]
	elif isinstance(exp, Times):
		#so, S1, E |- e1 : Int(i1), S2
		first = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: Int(i2), S3
		second = eval(so, first[1], e, exp.e2)
		#v1 = Int(i1 * i2)
		result_val = first[0].i * second[0].i
		#Ensure 32 bit arithmetic using two's compliment
		b = int(0xFFFFFFFF);
		if result_val > 2147483647:
			flip = result_val
			result_val = -((b ^ flip)+1)
		elif result_val < -2147483647:
			flip = result_val
			result_val = -((b^flip)+1)
		new_value = Cool_Int(int(result_val))
		new_store = second[1]
	elif isinstance(exp, Divide):
		#so, S1, E |- e1 : Int(i1), S2
		first = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: Int(i2), S3
		second = eval(so, first[1], e, exp.e2)
		#If i2 is zero, then division by zero is occuring
		if second[0].i == 0:
			print "ERROR: %s: Exception: division by zero" % exp.line
			exit(1)
		#v1 = Int(i1 / i2)
		result_val = first[0].i / second[0].i
		#Ensure 32 bit arithmetic using two's compliment
		b = int(0xFFFFFFFF);
		if result_val > 2147483647:
			flip = result_val
			result_val = -((b ^ flip)+1)
		elif result_val < -2147483647:
			flip = result_val
			result_val = -((b^flip)+1)
		new_value = Cool_Int(int(result_val))
		new_store = second[1]
	elif isinstance(exp, Not):
		#so, S1, E |- e1: Bool(b), S2
		ret = eval(so, s, e, exp.e1)
		#v1 = Bool(not b)
		if ret[0].b == "true":
			ret[0].b = "false"
		else:
			ret[0].b = "true"
		new_value = Cool_Bool(ret[0].b)
		new_store = ret[1]
	elif isinstance(exp, Neg):
		#so, S1, E |- e1: Int(i1), S2
		ret = eval(so, s, e, exp.e1)
		#v1 = Int(-i1)
		new_value = Cool_Int(0 - (ret[0].i))
		new_store = ret[1]
	elif isinstance(exp, IsVoid):
		#so, S1, E |- e1: void, S2
		e1 = eval(so, s, e, exp.e1)
		if isinstance(e1[0], Void):
			new_value = Cool_Bool("true")
			new_store = s
		#so, S1, E |- e1: X(...), S2
		else:
			new_value = Cool_Bool("false")
			new_store = s
	elif isinstance(exp, Block):
		#Evaluate each expression within the block, threading the store each time
		for se in exp.seq:
			#so, Sn, E |- en: vn, Sn+1
			ret = eval(so, s, e, se)
			s = ret[1]
		new_value = ret[0]
		new_store = s
	elif isinstance(exp, Equals): 
		locs = []
		#so, S1, E |- e1: X(...), S2
		e1 = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: X2(...), S3
		e2 = eval(so, e1[1], e, exp.e2)
		#Determine if there are 2+ objects that share the same location
		for k, v in e1[1].vals.iteritems():
			if v == e1[0]:
				locs.append(k)
		#Compare Ints according to classical convention
		if isinstance (e1[0], Cool_Int):
			if e1[0].i == e2[0].i:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Strings according to classical convention
		elif isinstance(e1[0], Cool_String):
			if e1[0].s == e2[0].s:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Bools according to classical convention
		elif isinstance(e1[0], Cool_Bool):
			if e1[0].b == e2[0].b:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#If two objects addresses are the same, the objects are equal
		elif e1 == e2 and len(locs) == 1:
			new_value = Cool_Bool("true")
			new_store = e2[1]
		#Void is only equal to void
		elif isinstance(e1[0], Void):
			if isinstance(e2[0], Void):
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#The objects are not equal
		else:
			new_value = Cool_Bool("false")
			new_store = e2[1]
	elif isinstance(exp, LessThan): 
		#so, S1, E |- e1: X(...), S2
		e1 = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: X2(...), S3
		e2 = eval(so, e1[1], e, exp.e2)
		#Compare Ints according to classical convention
		if isinstance (e1[0], Cool_Int):
			if e1[0].i < e2[0].i:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Strings according to classical convention
		elif isinstance(e1[0], Cool_String):
			if e1[0].s < e2[0].s:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Bools with false < true
		elif isinstance(e1[0], Cool_Bool):
			if e1[0].b == "false":
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#The first object is not less than the second object
		else:
			new_value = Cool_Bool("false")
			new_store = e2[1]
	elif isinstance(exp, LessThanEqual):
		#so, S1, E |- e1: X(...), S2 
		e1 = eval(so, s, e, exp.e1)
		#so, S2, E |- e2: X2(...), S3
		e2 = eval(so, e1[1], e, exp.e2)
		#Compare Ints according to classical convention
		if isinstance (e1[0], Cool_Int):
			if e1[0].i <= e2[0].i:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Strings according to classical convention
		elif isinstance(e1[0], Cool_String):
			if e1[0].s <= e2[0].s:
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Compare Bools with false < true
		elif isinstance(e1[0], Cool_Bool):
			if e1[0].b == "false" and e2[0].b == "false":
				new_value = Cool_Bool("true")
				new_store = e2[1]
			elif e1[0].b == "true" and e2[0].b == "true":
				new_value = Cool_Bool("true")
				new_store = e2[1]
			elif e1[0].b == "false" and e2[0].b == "true":
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#Void is only equal to void
		elif isinstance(e1[0], Void):
			if isinstance(e2[0], Void):
				new_value = Cool_Bool("true")
				new_store = e2[1]
			else:
				new_value = Cool_Bool("false")
				new_store = e2[1]
		#The first object is not less than or equal to the second object
		else:
			new_value = Cool_Bool("false")
			new_store = e2[1]
	elif isinstance(exp, Assign):
		#so, S1, E |- e1: v1, S2
		right = eval(so, s, e, exp.rhs)
		#E(Id) = l1
		l1 = e[exp.vname]
		#Remove old store reference
		del right[1].vals[l1]
		#S3 = S2[v1/l1]
		right[1].vals[l1] = right[0]
		new_value = right[0]
		new_store = right[1]
	elif isinstance(exp, Variable):
		#so, S, E |- self: so, S
		if exp.vname == "self":
			final_value = so
		else:
			#E(Id) = l
			l = e[exp.vname]
			#S(l) = v
			final_value = s.vals[l]
		new_value = final_value
		new_store = s
	elif isinstance(exp, New):
		#T0 = X if T = SELF_TYPE and so = X(...)
		if exp.cname == "SELF_TYPE":
			exp.cname = so.cname
		attrs_and_locs = OrderedDict()
		new_store = OrderedDict()
		accumulated_store = OrderedDict()
		updated_store = OrderedDict()
		#class(T0) = (a1: T1 <- e1,..., an: Tn <- en)
		attrs_and_inits = class_map[exp.cname]
		#li = newloc(S1), for i = 1...n and each li is distinct
		for a in attrs_and_inits:
			attrs_and_locs[a] = newloc()
		#Build an updated store using the newlocs created in the previous rule
		for a in attrs_and_locs:
			new_store[attrs_and_locs[a]] = class_map[exp.cname][a]
		#v1 = T0(a1 = l1, ..., an = ln)
		v1 = Cool_Object(exp.cname, attrs_and_locs)
		#S2 = S1[DT1/l1, ..., DTn/ln]
		s.vals.update(new_store)
		accumulated_store = s
		for a in attrs_and_inits:
			#v1, S2, [a1: l1, ..., an: ln] |- {a1 <- e1; ...; an <- en;} : v2, S3
			updated_store = eval(v1, accumulated_store, attrs_and_locs, Assign(a, attrs_and_inits[a]))
		new_value = v1
		new_store = accumulated_store
	elif isinstance(exp, Case):
		store_update = OrderedDict()
		e2 = Environment(OrderedDict())
		#so, S1, E |- e0: v0, s2
		e0 = eval(so, s, e, exp.e0)
		val = e0[0]
		s2 = e0[1]
		#If e0 is void, throw a case on void error
		if isinstance(val, Void):
			print "ERROR: %s: Exception: case on void" % (exp.line)
			exit(1)
		#v0 = X(...)
		v0 = val.__class__.__name__
		if v0 == "Cool_Object":
			typ = val.cname
		elif v0[:5] == "Cool_":
			typ = v0[5:]
		else:
			typ = v0
		branch = None
		#Ti = closest ancestor of X in {T1, ..., Tn}
		for el in exp.elem:
			if el[1] == typ:
				branch = el
		if branch == None:
			for el in exp.elem:
				if el[1] == parent_map[typ]:
					branch = el 
		#If no ancestor exists, throw an error
		if branch == None:
			print "ERROR: %s: Exception: case without matching branch: %s" % (exp.line, val)
			exit(1)
		#l0 = newloc(S2)
		loc = newloc()
		store_update[loc] = e0[0]
		#S3 = S2[v0/l0]
		s2.vals.update(store_update)
		#E' = E[l0/Idi]
		e2.attrs.update(e)
		e2.attrs[branch[0]] = loc
		#so, S3, E' |- ei: v1, S4
		(new_value, new_store) = eval(so, s2, e2.attrs, branch[2])
	elif isinstance(exp, Let):
		store_update = OrderedDict()
		e2 = Environment(OrderedDict())
		#so, S1, E |- e1: v1, S2
		val = eval(so, s, e, exp.bind[0][2])
		#l1 = newLoc(S2)
		loc = newloc()
		store_update[loc] = val[0]
		s2 = val[1]
		#S3 = S2[v1/l1]
		s2.vals.update(store_update)
		#E' = E[l1/Id]
		e2.attrs.update(e)
		e2.attrs[exp.bind[0][0]] = loc
		#If there is only one let statement, evaluate body as normal
		if len(exp.bind) == 1:
			#so, S3, E' |- e2: v2, S4
			(new_value, new_store) = eval(so, s2, e2.attrs, exp.body)
		#Else create a new let statement with the body as the rest of the let statements
		else:
			#so, S3, E' |- e2: v2, S4
			(new_value, new_store) = eval(so, s2, e2.attrs, Let(exp.bind[1:], exp.body))
	elif isinstance(exp, StaticDispatch):
		current_store = s
		store_update = OrderedDict()
		body = None
		arg_values = []
		#Evaluate all arguments that the method takes in, threading the store each time
		for a in exp.args:
			#so, Sn, E |- en: vn, Sn+1
			(arg, new_store) = eval(so, current_store, e, a)
			current_store = new_store
			arg_values.append(arg)
		#so, Sn+1, E |- e0: v0, Sn+2
		(v0, s_n1) = eval(so, current_store, e, exp.ro)
		#If the receiver object is Void, throw an error
		if isinstance(v0, Void):
			print ("ERROR: %s: Exception: dispatch on void" % exp.line)
			exit(1)
		#v0 = X(a1 = la1, ..., am = lam)
		if isinstance(v0, Cool_Object):
			#implementation(T, f) = (x1, ..., xn)
			formals = imp_map[exp.typ][exp.fname][0]
			#implementation(T, f) = en+1
			body = imp_map[exp.typ][exp.fname][1]
			counter = 0
			copy_attrs = v0.attrs
			#lxi = newloc(Sn+2), for i = 1...n and each lxi is distinct
			for f in formals:
				loc = newloc()
				store_update[loc] = arg_values[counter]
				copy_attrs[f] = loc
				counter+=1
			#Sn+3 = Sn+2[v1/lx1, ..., vn/lxn]
			s_n1.vals.update(store_update)
			#v0, Sn+3, [a1: la1, ..., am: lam, x1: lx1, ..., xn: lxn] |- en+1: vn+1, Sn+4
			(new_value, new_store) = eval(v0, s_n1, copy_attrs, body)
	elif isinstance(exp, Dispatch):
		current_store = s
		store_update = OrderedDict()
		body = None
		arg_values = []
		#Evaluate all arguments that the method takes in, threading the store each time
		for a in exp.args:
			#so, Sn, E |- en: vn, Sn+1
			(arg, new_store) = eval(so, current_store, e, a)
			current_store = new_store
			arg_values.append(arg)
		#so, Sn+1, E |- e0: v0, Sn+2
		(v0, s_n1) = eval(so, current_store, e, exp.ro)
		#If the receiver object is Void, throw an error
		if isinstance(v0, Void):
			print "ERROR: %s: Exception: dispatch on void" % exp.line
			exit(1)
		#v0 = X(a1 = la1, ..., am = lam)
		if isinstance(v0, Cool_Object):
			#implementation(X, f) = (x1, ..., xn)
			formals = imp_map[v0.cname][exp.fname][0]
			#implementation(X, f) = en+1
			body = imp_map[v0.cname][exp.fname][1]
			counter = 0
			copy_attrs = v0.attrs
			#lxi = newloc(Sn+2), for i = 1...n and each lxi is distinct
			for f in formals:
				loc = newloc()
				store_update[loc] = arg_values[counter]
				copy_attrs[f] = loc
				counter+=1
			#Sn+3 = Sn+2[v1/lx1, ..., vn/lxn]
			s_n1.vals.update(store_update)
			#v0, Sn+3, [a1: la1, ..., am: lam, x1: lx1, ..., xn: lxn] |- en+1: vn+1, Sn+4
			(new_value, new_store) = eval(v0, s_n1, copy_attrs, body)
	#so, S, E |- self: so, S
	elif exp in imp_map.keys():
		new_value = so
		new_store = s

	#BUILT IN METHODS

	#Print error message "abort" and halt program execution
	elif isinstance(exp, Abort):
		print "abort"
		exit(1)
	#Return a string with the name of the dynamic class of the object
	elif isinstance(exp, TypeName):
		new_value = Cool_String(so.cname)
		new_store = s
	#Produce a shallow copy of the object, where the object has a different location, but all attributes share locations
	elif isinstance(exp, Copy):
		new_val = so
		loc = newloc()
		s.vals[loc] = new_val
		new_value = new_val
		new_store = s
	#Print argument, return self parameter
	elif isinstance(exp, Out_String):
		loc = e[exp.val]
		out = s.vals[loc]
		#Replace all \t and \n appropriately
		sys.stdout.write(out.s.replace('\\n', '\n').replace('\\t', '\t')),
		new_value = out
		new_store = s
	#Print argument, return self parameter
	elif isinstance(exp, Out_Int):
		loc = e[exp.val]
		out = s.vals[loc]
		sys.stdout.write(str(out.i))
		new_value = out
		new_store = s
	#Read in a single integer
	elif isinstance(exp, In_Int):
		read_in = int(sys.stdin.readline())
		#If what is read in is not an int, read a 0
		if type(read_in) != int:
			new_value = Cool_Int(0)
		#If what is read in is not 32 bit, read a 0
		elif int(read_in) > 2147483647 or int(read_in) < -2147483648:
			new_value = Cool_Int(0)
		else:
			new_value = Cool_Int(read_in)
		new_store = s
	#Read in a string up to a newline or eof
	elif isinstance(exp, In_String):
		read_in = sys.stdin.readline()
		#If the string contains NUL, read an empty string
		if chr(0) in read_in:
			new_value = Cool_String("")
		#If no string before eof, read an empty string
		elif read_in.isspace():
			new_value = Cool_String("")
		#If the string contains non-ascii characters, read an empty string
		try:
			read_in.decode('ascii')
		except UnicodeDecodeError:
			new_value = Cool_String("")
		else:
			new_value = Cool_String(read_in.strip())
		new_store = s
	#Return the length of self
	elif isinstance(exp, Length):
		new_value = Cool_Int(so.i)
		new_store = s
	#Return the string after conatenating s to self
	elif isinstance(exp, Concat):
		loc = e[exp.s]
		val = s.vals[loc]
		st = so.s + val.s
		new_value = Cool_String(st)
		new_store = s

	#Return the substring of self starting at i with length l
	elif isinstance(exp, Substr):
		locs = e[exp.i]
		vals = s.vals[locs]
		start = vals.i
		loce = e[exp.l]
		vale = s.vals[loce]
		end = vale.i
		#If the substring is out of range, return an error
		if start+end > len(so.s):
			print "ERROR: 0: Exception: substring out of range"
			exit(1)		
		new_value = Cool_String(so.s[start:start+end])
		new_store = s
	#For debugging expressions that aren't present above
	else:
		print "ERROR"
		print "so: %s" % so
		print "s: %s" % s
		print "e: %s" % e
		print "exp: %s" % exp
		exit(1)
	debug_indent()
	#print "ret = %s" % new_value
	debug_indent()
	#print "rets= %s" % new_store
	#Clear indent for next eval statement
	indent_count -= 1
	#Subtract one activation record now that it has been taken care of
	act_rec -= 1
	#Return the new value and new store
	return (new_value, new_store)

#Begin each program with a dispatch of Main.main()
my_exp = Dispatch(New("Main", 0), "main", [], 0)
#print "my_exp = %s" % my_exp
so = None
store = Store(OrderedDict())
environment = Environment(OrderedDict())
#Evaluate Main.main()
eval(so, store, environment, my_exp)
#print "result = %s" % eval(so, store, environment, my_exp)[0]



