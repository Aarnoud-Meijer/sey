DATE('now') # returns current date, e.g., 2014-03-06
TIME('now') # returns current time, e.g., 10:10:10
CURRENT_TIMESTAMP # returns current date and time, e.g., 2014-03-06 16:42:30
#  (or alternatively: DATETIME('now'))

https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

class db:
	#default setting / question base
	default={			#default empty question base
		"question":		"String missing",
		"tip":			"String missing",
		"inputfalse":	["nee","n","no"],
		"inputtrue":	["ja","j", "y","yes"],
		# overrwite when change in steps
		"treu":			"next",
		"false":		"next",
		# method of question check / type of input check
		"type":			"bolean",
		# state of every question / only true if currend question is properly awnserd
		"awnser":		False
	}

	#default empty if no question data inserted
	question=[]

	#session data, contains user input (empty on new session)
	data=[]

	# defalt sql file
	db_file = ''

	# --- init / start quiz ---
	def __init__(self, object=False):
		# test if object is json and make quiz
		print self
		pass
