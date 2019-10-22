import random

user = str.casefold(input("Rock, Paper, Scissors? "))

if user != "rock" and user != "paper" and user != "scissors":
  print("Please enter only rock, paper, or scissors")
  ## ask how to exit a program without continuing here
 
num = random.randrange(1,3)
if num == 1:
  num = "rock"
  print("Computer chose: Rock")
if num == 2:
  num = "paper"
  print("Computer chose: Paper")
if num == 3:
  num = "scissors"
  print("Computer chose: Scissors")

if (user == "rock" and num == "rock") or (user == "paper" and num == "paper") or (user == "scissors" and num == "scissors"):
  print("You tied the computer!")

if (user == "rock" and num == "scissors") or (user == "paper" and num == "rock") or (user == "scissors" and num == "paper"):
  print("You beat the computer! Great job!")

if (num == "rock" and user == "scissors") or (num == "paper" and user == "rock") or (num == "scissors" and user == "paper"):
  print("The computer beat you! Bummer!")
  


