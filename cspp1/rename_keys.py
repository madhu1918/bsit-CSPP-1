import fileinput, os, string, sys
def replacestrs(filename):
	"replace a certain type of string occurances in all files in a directory"
	for line in fileinput.input(filename,inplace=1):

		lineno = 0
  		lineno = string.find(line, "optText")
  		if lineno >0:
  			line =line.replace("optText", "option")
		lineno = string.find(line, "questionText")
  		if lineno >0:
  			line =line.replace("questionText", "question")
		lineno = string.find(line, "opt-Text")
  		if lineno >0:
  			line =line.replace("opt-Text", "option")
		lineno = string.find(line, "question-Text")
  		if lineno >0:
  			line =line.replace("question-Text", "question")
  		sys.stdout.write(line)

def replacestrs1(filename):
	"replace a certain type of string occurances in all files in a directory"
	for line in fileinput.input(filename,inplace=1):

		lineno = 0
  		lineno = string.find(line, '"questionType":"quiz"')
  		if lineno >0:
  			line =line.replace('"questionType":"quiz"', '"questionType":"mcq"')
		lineno = string.find(line, '"questionType": "quiz"')
  		if lineno >0:
  			line =line.replace('"questionType": "quiz"', '"questionType":"mcq"')

		sys.stdout.write(line)

import fnmatch
matches = []
for root, dirnames, filenames in os.walk(os.getcwd()):
    for filename in fnmatch.filter(filenames, '*.json'):
        matches.append(os.path.join(root, filename))

for file in matches:
	replacestrs1(file)
	#print(file)
