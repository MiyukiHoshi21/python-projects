print("Title of program: Feel better bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("you can do anything, don't let anything drag you down")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("you can also brighten someone else's day with a joke or smile!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append(" to take a break if you need to but get back on track when you done")
      counter += 1
    if each_word == "depressed":
      feelings_list.append("depressed")
      encouragement_list.append("that there is people who you can trust and talk to")
      counter += 1
    if each_word == "excited":
      feelings_list.append("excited")
      encouragement_list.append("to also help others around you to feel that way")
      counter += 1

  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better! ^_^"

  print()
  print(output)
  print()
