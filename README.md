# pythonIndent
A small tool to indent python code, make you write python freedom

Here i add #{ #} to mark the indent place, for example python source file :

Test.py:

a = 0
print ("01")
if a==2:
#{
print("02")
print("03")
#}
else:
#{
	print("04")
#}

run command :
python indentPython.py Test.py

generate indent code:
a = 0
print ("01")
if a==2:
#{
	print("02")
	print("02")
#}
else:
#{
	print("04")
#}

