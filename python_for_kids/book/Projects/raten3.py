import random
Secret = "Я задумал число от 1 до 1000"
Case = random.randint(1,1000)
print(Case)
print(Secret)
Attempt = 0
Input = 0
while Input != Case :
  print("Угадай число: ", end="")
  Input = int(input())
  Attempt = Attempt + 1
  if Input < Case :
    print("Слишком маленькое!")
  if Input > Case :
    print("Слишком большое!")
  if Input == Case :
    print("Правильно!")
print("Ты попробовал " + str(Attempt) + " раз.")


