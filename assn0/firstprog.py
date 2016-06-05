# "HASH' IS A COMMENTS IN THE PYTHON PROGRAMMING  :)

# NOW HELLO WORLD , LET'S ENTER THE WORLD OF PYTHON PROGRAMMING

# HOW YOU RUN THE PROGRAM , I SAVED THIS IN A DESKTOP UNDER THE FOLDER assn0 and saved this file as firstprog.py

# in the terminal , >>> python firstprog.py 

# that's it. you are good to go. Mac and Linux supports natively and windows needs a installation. :)

print "welcome to python programming"
print "great!"

# expressions.
print 123

# THIS IS A FLOATING POINT
print 98.6

# ASSIGNING TO A VARIABLE.
x = 23

y = x + 1

print y

# DIVISION IN PYTHON ROUNDS OFF THE VALUE , IF 9/2 PRODUCES 4 AND NOT 4.5
div = 4/2

print div

# THIS GIVES US THE REMAINDER , THIS PRODUCES OUTPUT OF 0.
rem = 4%2

print rem

# THIS IS HOW YOU REFER 4 TO THE POWER OF 2, WHICH PRODUCES OUTPUT OF 16.
pow = 4**2

print pow

mul = 2 * 3

print mul 

# order of execution 
# paranthesis -> power -> multiplication -> addition -> left to right.

order = 1 + 2 **3/4 * 5

print order

# prints 4 and not 4.5 similar to 99/100 produces 0 (rounds off )
print 9/2 

# 1 + 6/4.0 - 5 -> 1 + 1.5 - 5 - > 2.5 - 5 - > -2.5
# ( once the program touches floating point , remainder of calculation is done is floating point.)
print "hello floating point -> " , 1 + 2*3 / 4.0 - 5


# INTRODUCING TYPES 

eee = "string" + "append"

print eee

print type("hello")

# type conversion , different than 99/100 which produces 0 rather than 0.99
print float(99)/100

# nsv = "hello" and niv = int(nsv) , throws an traceback error. invalid literal for int()

# LETS SEE HOW WE ACCEPT INPUTS TO THE PROGRAM 

name = raw_input("who are you ?")

print "welcome",name

inp = raw_input("which floor ?")

usf = int(inp) + 1

print "us floor ",usf


# conditional execution. 

x = 5
if x < 10:
 print "smaller"

if x > 20:
 print "bigger"

print "finish"

print "starting conditional statement"

inputif = int(raw_input("enter your age"))

if inputif < 18:
	print " you are a minor"
elif inputif > 18:
	print "you are a major"
else:
	print "yeah else part can't be reached !!"
	

print "for loop "
words = ['ram', 'window','late']

for w in words:
	print 'words -> ',w







