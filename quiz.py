class quiz:
	#default setting / question base
	default={			#default empty question base
		"q":			"String missing",
		"tip":			"String missing",
#		"inputfalse":	["nee","n","no"],
#		"inputtrue":	["ja","j", "y","yes"],
		# overrwite when change in steps
#		"treu":			"next",
#		"false":		"next",
		# method of question check / type of input check
		"type":			"bolean",
		# state of every question / only true if currend question is properly awnserd
#		"awnser":		False,
		"option":		(['y'],['n']),
		"next":			True,
	}

	intro=""
	outro=""
	current=0 # [int] current question state
	current_question=0
	next=0


	#default empty if no question data inserted
	question=[]

	#session data, contains user input (empty on new session)
	data=[]
	data2=[]

	# defalt sql
	db_file		= 'test321.db'
	db_tabel	= 'awnsers'

	# to lang
	err={
		"noint":	"\npleace input a digit\n",
		"nobolean":	"\npleace input Y or N\n",
		"noage":	"\nyou must be realy old or var to jung\n",
	}

	devmode = False

	def getkeys(self):
		for m in self.default.iterkeys():
			print(m, ''), # no line break
			# print item,				# tail ',' in Python 2.7
			# print(item, end=" ")		# in Python 3

	def getkeys(self):
		for value in self.default.itervalues():
			print(value, ''), # no line break


	# update question with default if key is missing
	def setquestion(self, lang=False):
		for index in self.question.iterkeys():
			for key in self.default.iterkeys():
				if key in self.question[index]:
					pass
				else:
					self.question[index][key] = self.default[key]
					if self.devmode:
						print "updated: ", key, self.question[index][key] 

	# --- init / start quiz ---
	def __init__(self, question=False):									# init
		from lang import question
		self.question = question
		self.setquestion()

		self.next = next(iter(self.question)) # set first question
		self.data = [] # empty data

		# init database
		import os, os.path
		from database import database
		if os.path.isfile(self.db_file) and os.access(self.db_file, os.R_OK):
			self.database = database(self.db_file)
		else:
			self.database = database(self.db_file)
			self.install()


		sql = "INSERT INTO awnsers values (Age , Gender , Function , Use_source , Pynter_profile , Pynter_groups , Closed_group , Share_knowlage , ICT_improve ) , (6 , true , n , false , false , false , true , false , 4 )"
		
		#self.database.write(sql)

		for value in self.question:
			#self.data[value] = 0
			self.data.insert(int(value), '')
			pass
			
#		for m in self.data.iterkeys():#
#			print(m, ''), # no line break

#		self.save_awnsers()
		self.startquiz()
#		self.save_awnsers()

		for key, value in self.data2:
#			print key, value
			pass
			
		self.save_awnsers()


	def save_awnsers(self):
		names =''
		values = ''
		placeholde = '('
		c = 0 #len(self.data2)
		for key, value in self.data2:
			names += key + " "
			values += '"'+value + '"'
			placeholde += "?"
			c += 1
			if c < len(self.data2):
				names += ", "
				values += ", "
				placeholde += ","
		placeholde += ")"

		sql = "INSERT INTO "+self.db_tabel+" ("+ names +  ") values (" + values + ")"
		# werkt # INSERT INTO awnsers  (Age , Gender , Function , Use_source , Pynter_profile , Pynter_groups , Closed_group , Share_knowlage , ICT_improve )  values  ('5' ,' true' ,' n' ,' false' ,' false' ,' false' ,' true' ,' false' , '4' )

#		print sql
		self.database.query(sql)
		
	#	def get(self,table,columns,limit=None):
		data = self.database.get(self.db_tabel,names)
		self.database.toCSV(data)
#		print data
		
#		self.database.summary('awnsers')


	def save_awnser(self, result=False):
		print self.question[self.next]["name"]
		sql = "INSERT INTO "+self.db_tabel+" ("+ self.question[self.next]["name"] +  ") values " + result
		
#		sql = "INSERT INTO "+self.db_tabel+" values("+ self.question[self.next]["name"] +  ") , (" + result + ")"
		
		print sql
	#	sql = "INSERT INTO awnsers Age values (4)"
		# insert into awnsers (Age) values (4)
#		self.database.query(sql)


	def install(self):
		sql = "CREATE TABLE "+self.db_tabel+" (id integer primary key autoincrement, "
		for value in self.question:
			name = self.question[value]['name']
			sql += name + ' VARCHAR(50)'
			if value < len(self.question):
					sql += ", "
		sql += ")"
		self.database.query(sql)
		if self.devmode:
			print sql


	def counter(self, result=''):										# counter
		# always check bool first; bolean is an instance of int
		if isinstance(self.question[self.next]["next"], bool):
			self.next += 1
		elif isinstance(self.question[self.next]["next"], int):
			self.next = self.question[self.next]["next"]
		elif isinstance(self.question[self.next]["next"], tuple):
			if result:
				self.next = self.question[self.next]["next"][0] # if result else self.question[self.next]["next"][1]
			else:
				self.next = self.question[self.next]["next"][1]
		else:
			self.next = self.question[self.next]["next"]
		return self.next

	def startquiz(self):												# quiz
		while self.next:
			result = getattr(self, format(self.question[self.next]['type']))(format(self.question[self.next]['q']))
			self.counter(result)


	def getquestion(self):
		if not self.question:
			print "no questions"
		for c, value in enumerate(self.question, 1):
			print(c, value)

	def string(self, question=False):
		awnser = False
		while not (awnser):
			string = raw_input(question)
			if string == "" or string.isdigit(): # check if not empty sting
				print format(self.question[self.next]["tip"])
			else:
				self.data.insert(int(self.next), string)
				self.data2.insert(int(self.next), [self.question[self.next]["name"], string])
				self.save_awnser(string)
				return True


	def age(self, question=False):
		awnser = False
		while not (awnser): #len(self.data[int(self.next)]):
			age = raw_input(question)
			if age.isdigit():
				if not 15 <= int(age) <= 115:
					print format(self.err["noage"])
#				self.data.insert(int(self.next), age)
				
				self.data2.insert(int(self.next), [self.question[self.next]["name"], age]) 
				
#				self.save_awnser(age)
				return age
				awnser = True
			else:
				print format(self.question[self.next]["tip"])
		return age


	def digit(self, question=False):
		awnser = False
		while not (awnser):
			digit = raw_input(question)
			if digit.isdigit():
				#awnser = True
				self.data.insert(int(self.next), digit)
				self.data2.insert(int(self.next), [self.question[self.next]["name"], digit])
				self.save_awnser(digit)
				return digit
			else:
				print format(self.err["noint"])
		return false


	def gender(self, question=False):
		awnser = False
		while not (awnser):
		# while not self.data[self.next]:
			gender = raw_input(question).lower()
			if gender in self.question[self.next]['option'][0]:
				# self.question[self.next]['option'][0]
				gender = "male"
			#	self.data.insert(int(self.next), gender)
				self.data2.insert(int(self.next), [self.question[self.next]["name"], gender])
#				self.save_awnser('string')
				awnser = True
				#return awnser = True
			elif gender in self.question[self.next]['option'][1]:
				gender = "female"
#				self.data.insert(int(self.next), gender)
				self.data2.insert(int(self.next), [self.question[self.next]["name"], gender])
				self.save_awnser(gender)
				awnser = True
			else:
				print self.question[self.next]['tip']

	#default method; override in setting
	def bolean(self, question=False):
		awnser = False
		while not (awnser):
			bolean = raw_input(question).lower()
			if bolean in self.question[self.next]['option'][0]:
				self.data.insert(int(self.next), 'treu')
				self.data2.insert(int(self.next), [self.question[self.next]["name"], "true"])
				self.save_awnser('treu')
				return True
			elif bolean in self.question[self.next]['option'][1]:
				self.data.insert(int(self.next), 'false')
				self.data2.insert(int(self.next), [self.question[self.next]["name"], "false"])
				self.save_awnser('false')
				return False
				bolean = "nee"
				awnser = True
			else:
				print format(self.err["nobolean"])

	def multi(self, question=False):
		# comma seperated awnser
		multi = raw_input("enter multi (separated by a comma):").split(',')
		awnser = False
		while not (awnser):
			string = raw_input(question)
			if string == "": # check if not empty sting
				print format(self.question[self.next]["tip"])
			else:
				self.data.insert(int(self.next), string)
				self.save_awnser('string')
				return True

	def clearscreen():
		# os.system('cls')  # on windows
		os.system('clear')  # on linux / os x




# direct call check
if __name__ == "__main__":
	print "please run main.py"
