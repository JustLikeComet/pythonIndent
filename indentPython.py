# -*- coding: UTF-8 -*-
import os
import sys
import re
import getopt


indentStr = "\t"

def checkIndent(filepath):
	indentCount = 0;

	fp = open(filepath, "r")

	while True:
		line = fp.readline()
		if not line:
			break
		line = re.sub(r'^\s*', "", line)
		if len(line)==0:
			continue
		if line[0] == '#':
			if line[1] == '{':
				indentCount += 1
			if line[1] == '}':
				indentCount-=1

	fp.close()
	return indentCount


def indentCode(filepath):
	codeContent = ""
	indentCount = 0;

	fp = open(filepath, "r")

	while True:
		line = fp.readline()
		if not line:
			break
		line = re.sub(r'^\s*', "", line)
		if len(line)==0:
			continue
		if line[0] == '#':
			if line[1] == '{':
				codeContent += indentStr*indentCount + line
				indentCount += 1
			if line[1] == '}':
				indentCount-=1
				codeContent += indentStr*indentCount + line
		else:
			codeContent += indentStr*indentCount + line

	fp.close()


	fo = open(filepath, "w")
	fo.write(codeContent)
	fo.close()


opts,args = getopt.getopt(sys.argv[1:],'-h-i:',['help','indent='])

for opt_name,opt_value in opts:
	if opt_name in ('-h','--help'):
		print("indentPython.py [-h|--help] [-i t|sNUM] file [...]")
		print("-h  --help show help info")
		print("-i  --indent set indent , \n\t\t-i t use one tab ,\n\t\t -i sNUM is use NUM space NUM in (1,9)")
		sys.exit()
	if opt_name in ('-i','--indent'):
		if opt_value[0] == 's':
			if opt_value[1]=='0':
				print('Error with s0 setting')
				sys.exit()
			indentStr = ' '*int(opt_value[1])
		elif opt_value[0] == 't':
			# do nothing
			indentStr = "\t"
		else:
			print('Error with '+opt_value+' setting')
			sys.exit()


if len(args) == 0:
	print ("give me file path")

for filepath in args:
	if not os.path.exists(filepath):
		print ("give me a exist file ",filepath)
	else:
		indentVal = checkIndent(filepath)
		if indentVal>0 :
			print("#{ too many, not close with #}")
		elif indentVal<0 :
			print("#} too many, not pair with #{")
		else:
			indentCode(filepath)

