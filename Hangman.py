#Hangman Game
import random as r
Words = input("Enter a list of words seperated by space : ")
Word_List = Words.split(" ")
Word = r.choice(Word_List)
Check = ""
Life = 0
Check_Word = []
Word = Word.upper()
for i in Word:
  if i == " ":
    Check+=i + " "
    Check_Word.append("  ")
  else:
    Check+=i + " "
    Check_Word.append("_ ")
Display_Word = ""
while True:
  Display_Word = ""
  for i in Check_Word:
    Display_Word+=i
  if Check == Display_Word:
    print(Check)
    print("Game Won")
    break
  print(Display_Word)
  Guess = input("Guess a letter : ")
  Guess = Guess.upper()
  if Guess in Word:
    print("Letter present in word.")
    for i in range(0,len(Word)):
      if Word[i] == Guess:
        Check_Word[i] = Guess + " "
  else:
    print("Letter not present in Word.")
    Life+=1
    print(f"Remaining Lives : {6 - Life}")
  if Life == 6:
    print("Game Lost.")
    break