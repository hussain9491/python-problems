
# keep asking the user for input until they enter a valid number between1 to 8
while True:
 user = int(input("Please enter a number between 1 and 8: "))

 if user >=1 and user <= 8:
  print("your number is valid for question")
  break
 else:
  print("Invalid number, please enter a number between 1 and 8")