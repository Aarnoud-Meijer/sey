#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Oefeningen STEM1
# Computational thinking
# 
# Vragen over digitale middelen en bronnnen

# python 2.7
# catch 'ctrl+c" from breaking to cli
# catch 'esc' for main menu stuff / and break loop
# convert to Django, gui or cli; detect if cli or http request

import os, os.path, sqlite3, json
from quiz import quiz

# bootsrap

# settings override // REMOVE! must be in class
setting={
	"q":	"String missing",
	"tip":	"String missing",
	"inputfalse":	["nee","n"],
	"inputtrue":	["ja","j", "y"],
	# overrwite when change in steps
	"treu":		"next",
	"false":	"next",
	# method of question check
	"type":		"bolean",
}


def readfile(PATH):
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
		PATH = open(PATH, 'r')
		return PATH.read()
	else:
		print "Either "+PATH+" is missing or is not readable"



# 2 db class
sqlite_file="./db"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

if __name__ == "__main__":
	lang ="./lang.py"
	lang = readfile(lang)
	# print lang

#	string = 'Wat is je leeftijd?'
#	quiz = quiz(lang)
	quiz = quiz()
#	quiz.age(string)
#	quiz.gender("Wat is je geslacht? man / vrouw ")

	#quiz.getquestion()

