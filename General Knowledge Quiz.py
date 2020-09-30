print("Title of program: General Knowlegde (For adults)")
print()

counter = 0
score = 0
total_num_of_qn = 100


counter +=1
tracker = 0

while tracker !=1:
  print("Geography Questions")
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

  
print("End of quiz!")
  
