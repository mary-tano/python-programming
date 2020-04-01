import random

# Функции
def initGame() :
  global Attempt, Input
  Secret = "Я задумал число от 1 до 1000"
  print(Secret)
  Attempt = 0
  Input = 0
def playGame() :
  global Attempt, Input
  Case = random.randint(1,1000)
  # print(Case)
  while Input != Case :
    print("Угадай число: ", end="")
    Input = int(input())
    Attempt += 1
    if Input < Case :
      print("Слишком маленькое!")
    if Input > Case :
      print("Слишком большое!")
    if Input == Case :
      print("Правильно!")
def endGame() :
  global Attempt
  print("Ты попробовал " + str(Attempt) + " раз.")

# Основная программа
initGame()
playGame()
endGame()
