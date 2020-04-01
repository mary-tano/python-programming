# Угадывает компьютер
import random
Secret = "Задумай число от 1 до 1000."
print(Secret)
print("Запомни число! Я попытаюсь угадать:")
Minimum = 1
Maximum = 1000 
Attempt = 0
Info = ""
while Info != "правильное" :
  Attempt += 1
  Number = int((Maximum+Minimum)/2)
  print(str(Attempt) + ". Попытка: " + str(Number))
  print("Число правильное/меньше/больше? ", end="")
  Info = input()
  if Info == "меньше" :
    Minimum = Number
  if Info == "больше" :
    Maximum  = Number
  if Info == "правильное" : 
    print("OK - ", end="")
  else :
    print("Жаль - ", end="")
print("Я сделал " + str(Attempt) + " попыток.")

