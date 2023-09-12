file = "listOfQuestions.txt"
usedFile = "listOfUsedQuestions.txt"

def getQOTD():
  with open(file,'r+') as questions:
      
      lines = questions.readlines()
      lineIndex = 0
      QOTD = lines[lineIndex]
      questions.seek(0)
      questions.truncate()
      questions.writelines(lines[1:])
      questions.close()
      updateUsedQuestions(QOTD)
      return QOTD
  
def updateUsedQuestions(QOTD):
  with open(usedFile,'w') as usedQuestions:
      usedQuestions.writelines(QOTD)
      usedQuestions.close()


      
 
 
