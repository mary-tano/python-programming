# Игральные кубики
import random, time
print("Давай бросим кубики!")
Attempt = 0
YourNumber = 0
MyNumber = 0
while Attempt < 5 :
  Attempt = Attempt + 1
  print(str(Attempt) + ". Раунд")
  print("Твоя очередь: ", end="")
  Shoot1 = random.randint(1,6)  # Твой бросок
  time.sleep(0.5)  # Ожидание в полсекунды
  print(Shoot1)
  print("Моя очередь: ", end="")
  Shoot2 = random.randint(1,6)  # Мой бросок
  time.sleep(0.5)  # Ожидание в полсекунды
  print(Shoot2)
  if Shoot1 > Shoot2 :
    YourNumber = YourNumber + 1
  if Shoot1 < Shoot2 :
    MyNumber = MyNumber + 1
  print(str(YourNumber) + " и " + str(MyNumber))
  time.sleep(1)  # Ожидание в секунду
  print()
if YourNumber > MyNumber :
  print("Ты выиграл")
elif YourNumber < MyNumber :
  print("Я выиграл")
else :
  print("Ничья")

