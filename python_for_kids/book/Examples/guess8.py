import random

# Функция
def initGame() :
  Secret = "Я задумал число от 1 до 1000"
  print(Secret)
def playGame(Attempt, Input) :
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
  return Attempt
def endGame(Attempt) :
  print("Ты попробовал " + str(Attempt) + " раз.")

# Основная программа
initGame()
Game = playGame(0,0)
endGame(Game)

