lang ={
	"intro":[
		"\nBeste medewerker van Cosis.\n",
		"Deze vragenlijst gaat over digitale middelen en bronnen die Cosis gebruikt.",
		"Het doel van deze vragenlijst is om te inventariseren hoe medewerkers van Cosis deze middelen gebruiken en op welke manier medewerkers kennis delen. ",
		"Alvast bedankt voor je medewerking.\n"
	],
	# settings
	"default":[
		{"q":		[""]},
		{"tip":		[""]},
		{"inputfalse":	["nee","n"]},
		{"inputtrue":	["ja","j", "y"]},
		# overrwite when change in steps
		{"treu":	["next"]},
		{"false":	["next"]},
		# method of question check
		{"type":	["bolean"]},
	],
	# Questions
	1:[
		("q", "Wat is je leeftijd?"),
		{"tip": "voer a.u.b. een getal in\n"},
		{"type":["age"]},
	],
	"step1":[
		"gender",
		"Wat is je geslacht? man / vrouw ",
		"man/vrouw"
	],
	"questions":[{
		0:[
		"gender",
		"Wat is je geslacht? man / vrouw ",
		"man/vrouw"
		]},
		{1:[
			{"q":		["Wat is je leeftijd?"]},
			{"tip":		["voer a.u.b. een getal in\n"]},
			{"type":	["age"]},
		"test",
		"test Wat is je geslacht? man / vrouw ",
		"test man/vrouw"
		]},
	]
}

menu ={
	"q":	'''1. start quiz\n'''+
			'''2. read database\n'''+
			'''3. export database\n''',
	"option":	range(1,3)
}

question ={
	# id
	1:{
		"name":		"Age",
		# index		# value / string
		"q":		"\nWat is je leeftijd?\n",
		"tip":		"voer a.u.b. een getal in\n",
		# check input for type
		"type":		"age",
		"option":	range(15, 99),
		#			on true or false (goto question)
		"next":		True
	},
	2:{
		"name":		"Gender",
		"q":		"\nWat is je geslacht?\n(man / vrouw)\n",
		"tip":		"man/vrouw",
		"type":		"bolean",
		"option":	(["man", "m", "male"], ["vrouw", "v", "female"]),
		"next":		True
	},
	3:{
		"name":		"Function",
		"q":		"\nWat is je functie?\n",
		"tip":		"zorgverlener , geen , etc",
		"type":		"string",
		"next":		4
	},
	4:{
		"name":		"Digital_source",
		"q":		'''\nWelke digitale bronnen en middelen gebruik je?\n'''+
					'''1. Pynter\n2. Webmail\n3. PCD\n4. Mijn Cosis\n5. Novonet\n6. Geen\n''',
		"tip":		"1, 2, 3 (meerdere opties gescheiden met comma b.v. 3, 5) of 6",
		"option":	(range(1, 5), [6]),
		"type":		"multi",
#		"next":		(5, 5)
	},
	5:{
		"name":		"Use_source",
		"q":		"\nStelling:\nIk werk graag met digitale bronnen en middelen\neens / oneens\n",
		"tip":		"eens / oneens",
		"type":		"bolean",
		"option":	(["eens", "ja","j", "y", "yes", "yhah", "si"], ["oneens", "nee","n", "no", "nope"]),
#		"next":		(6, 6)
	},
	6:{
		"name":		"Pynter_profile",
		"q":		"\nHeb je in Pynter een profiel aangemaakt waarin je kennis en talenten zichtbaar maakt?\n(ja / nee)\n",
		"tip":		"ja of nee\n",
		"type":		"bolean",
#		"next":		(7, 7)
	},
	7:{
		"name":		"Pynter_groups",
		"q":		"\nNeem je deel aan groepen in Pynter?\n(ja / nee)\n",
		"tip":		"ja / nee\n",
		"type":		"bolean",
		"option":	(["ja","j", "y", "yes", "yhah", "si"], ["nee","n", "no", "nope"]),
#		"next":		(8, 8)
	},
	8:{
		"name":		"Closed_group",
		"q":		"\nNeem je deel aan een gesloten groep (alleen van je werkplek) of ook een open groep?\n(gesloten / open)\n",
		"tip":		"gesloten /open\n",
		"type":		"bolean",
		"option":	("gesloten", "open"),
#		"next":		(9, 9)
	},
	9:{
		"name":		"Share_knowlage",
		"q":		'''\nIk deel mijn talenten en kennis (zoals van digitale bronnen en middelen) direct met collega\'s\n'''+
					'''(eens / oneens)\n''',
		"tip":		"eens / oneens",
		"type":		"bolean",
		"option":	(["eens", "ja","j", "y", "yes", "yhah", "si"], ["oneens", "nee","n", "no", "nope"]),
#		"next":		(10, 10)
	},
	10:{
		"name":		"ICT_improve",
		"q":		'''\nOp welke manier zou je graag je ICT vaardigheden willen verbeteren?\n'''+
					'''1. Door te leren in Pynter (E-learning)\n'''+
					'''2. Door het volgen van een reguliere cursus\n'''+
					'''3. Door te leren van mijn collega/'s\n'''+
					'''4. Ik wil mijn ICT-vaardigheden niet verbeteren\n''',
		"tip":		"voor een getal in: 1, 3 of 4",
		"type":		"digit",
		"option":	(range(1, 3), [4]),
		"next":		(False, 11)
	},
	11:{
		"name":		"Why_not",
		"q":		'''\nWaarom niet? Geef de belangrijkste oorzaak aan:\n'''+
					'''1. De technische randvoorwaarden schieten te kort (hoeveelheid computers,snelheid computers, gebruiksvriendelijkheid)\n'''+
					'''2. Ik weet onvoldoende van ICT-vaardigheden\n'''+
					'''3. Het hoort niet bij mijn functie\n''',
		"tip":		"voor een getal in",
		"type":		"digit",
		"option":	range(1, 3),
		"next":		(False, False)
	},
}


intro = {'''\nBeste medewerker van Cosis.\n'''+
		'''Deze vragenlijst gaat over digitale middelen en bronnen die Cosis gebruikt.\n'''+
		'''Het doel van deze vragenlijst is om te inventariseren hoe medewerkers van Cosis deze middelen gebruiken en op welke manier medewerkers kennis delen.\n'''+
		'''Alvast bedankt voor je medewerking.\n\n'''
		}

outro = "\nBedankt voor je medewerking\n"

setting=[
	{"q":		["Geen vraag gevonden/n"]},
	{"tip":		["Geen antwoord optie gevonden/n"]},
	{"inputfalse":	["nee","n"]},
	{"inputtrue":	["ja","j", "y"]},
	# overrwite when change in steps
	{"treu":	["++1"]},
	{"false":	["++1"]},
	# method of question check
	{"type":	["bolean"]},
]
