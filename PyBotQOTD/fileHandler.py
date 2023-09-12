####  Files for question reading and checking usaage  ####
file = "listOfQuestions.txt"
usedFile = "listOfUsedQuestions.txt"

### Gets the Question of the Day (QOTD)
def getQOTD():
  with open(file,'r+') as questions:
      
      lines = questions.readlines()  # reads all lines in file
      lineIndex = 0                  # sets line index to the first
      QOTD = lines[lineIndex]        # sets the QOTD to the first question in file
      questions.seek(0)              # sets file line to the first
      questions.truncate()           # Shortens file
      questions.writelines(lines[1:]) # rewrites file lines, making previously second line the first etc
      questions.close()               
      updateUsedQuestions(QOTD)      # updates used quesiton file
      return QOTD

# stores current question appended to file
def updateUsedQuestions(QOTD):
  with open(usedFile,'a') as usedQuestions:
      usedQuestions.writelines(QOTD)
      usedQuestions.close()



      
 
 
