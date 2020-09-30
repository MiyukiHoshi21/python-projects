If any of you want to take the test just use this: (https://create.withcode.uk/python/Bat) because the code is super long. ^_^

print("Title of program: The Impossible Test")
print()

counter = 0
score = 0
total_num_of_qn = 10


counter +=1
tracker = 0

while tracker !=1:
  
  print("---------------------------------------")
  print("~~~~~~~~~~~~~~~GEOGRAPHY~~~~~~~~~~~~~~~")
  print("---------------------------------------")
  print("Q"+str(counter)+") "+ "What is the capital of Chile?")
  print("   a) Islamabad")
  print("   b) Santiago")
  print("   c) Bogota")
  print("   d) Ankara")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is the capital of Pakistan."
    score -=1
  elif answer == "b":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "c":
    output = "Wrong. This is the capital of Colombia."
    score -=1
  elif answer == "d":
    output = "Wrong. This is the capital of Turkey."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the highest mountain in Britain?")
  print("   a) Pikes Peak")
  print("   b) Mount Kinabalu")
  print("   c) Monte Bianco/Mont Blanc")
  print("   d) Ben Nevis")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is the tallest mountain in Colorado."
    score -=1
  elif answer == "b":
    output = "Wrong. This is the tallest mountain in Malaysia."
    score -=1
  elif answer == "c":
    output = "Wrong. This is the tallest mountain in Italy."
    score -=1
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the smallest country in the world?")
  print("   a) Vatican City")
  print("   b) The Maldives")
  print("   c) Seychelles")
  print("   d) El Salvador")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. This is the smallest country in Asia."
    score -=1
  elif answer == "c":
    output = "Wrong. This is the smallest country in Africa."
    score -=1
  elif answer == "d":
    output = "Wrong. This is the smallest country in the Americas."
    tracker =1
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()

  
  
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Alberta is a province of which country?")
  print("   a) Algeria")
  print("   b) Nauru")
  print("   c) Romania")
  print("   d) Canada")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Alberta is not a province of Algeria."
    score -=1
  elif answer == "b":
    output = "Wrong. Alberta is not a province of Nauru."
    score -=1
  elif answer == "c":
    output = "Wrong. Alberta is not a province of Romania."
    score -=1
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
  
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many countries still have the shilling as currency? Which countries are they?")
  print("   a) Six - Italy, Israel, Tanzania, Antigua, Barbuda and Rwanda")
  print("   b) Three - Colombia, The Maldives and Monaco")
  print("   c) Five - Dominican Republic, Holy See, Tunisia, Mongolia and Albania")
  print("   d) Four – Kenya, Uganda, Tanzania and Somalia")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. There are not that many countries."
    score -=1
  elif answer == "b":
    output = "Wrong. There are not that few countries."
    score -=1
  elif answer == "c":
    output = "Wrong. There are not that many countries."
    score -=1
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
 
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which is the only vowel not used as the first letter in a US State?")
  print("   a) U")
  print("   b) I")
  print("   c) E")
  print("   d) A")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. There is a state called Utah."
    score -=1
  elif answer == "b":
    output = "Wrong. There are states called Idaho, Illinois, Indiana and Iowa."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. There are states called Alabama, Alaska, Arizona and Arkansas."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the largest country in the world?")
  print("   a) Canada")
  print("   b) Russia")
  print("   c) United States")
  print("   d) China")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. This is the second largest country in the world."
    score -=1
  elif answer == "b":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "c":
    output = "Wrong. This is the fourth largest country in the world."
    score -=1
  elif answer == "d":
    output = "Wrong. This is the third largest country in the world."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  



counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Where would you find the River Thames?")
  print("   a) London, UK")
  print("   b) New Orleans, USA")
  print("   c) Shanghai, China")
  print("   d) Paris, France")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. River Mississippi is located here."
    score -=1
  elif answer == "c":
    output = "Wrong. River Yangtze is located here."
    score -=1
  elif answer == "d":
    output = "Wrong. River Seine is located here."
    tracker =1
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()

  
  
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the hottest continent on Earth?")
  print("   a) North America")
  print("   b) South America")
  print("   c) Africa")
  print("   d) Asia")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. There is an even hotter continent."
    score -=1
  elif answer == "b":
    output = "Wrong. There is an even hotter continent."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. There is an even hotter continent."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the longest river in the world?")
  print("   a) The Snake River")
  print("   b) The Amazon River")
  print("   c) The River Nile")
  print("   d) The Yellow River")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. That is the 76th longest river in the world."
    score -=1
  elif answer == "b":
    output = "Wrong. That is the 2nd longest river in the world."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. That is the 6th longest river in the world."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  



print("End of quiz!")
