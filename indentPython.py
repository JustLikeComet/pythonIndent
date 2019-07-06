# -*- coding: UTF-8 -*-
import os
import sys
import re


def checkIndent(filepath):
	indentStr = "\t"
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
				indentCount += 1
			if line[1] == '}':
				indentCount-=1

	fp.close()
	return indentCount


def indentCode(filepath):
	indentStr = "\t"
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


if len(sys.argv) != 2:
	print ("give me a file path")
if not os.path.exists(sys.argv[1]):
	print ("give me a exist file ")

indentVal = checkIndent(sys.argv[1])
if indentVal>0 :
	print("#{ too many, not close with #}")
elif indentVal<0 :
	print("#} too many, not pair with #{")
else:
	indentCode(sys.argv[1])

