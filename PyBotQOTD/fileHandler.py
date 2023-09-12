file = "listOfQuestions.txt"

def getQOTD():
  with open(file,'r') as questions:
      
      lines = questions.readlines()
      lineIndex = 0
      QOTD = lines[lineIndex]
      questions.close()

      return QOTD


