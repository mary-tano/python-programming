# Математика
import random
Number1 = random.randint(0,50)
Number2 = random.randint(1,20)
Operation = random.randint(1,4)
if Operation == 1 :
  Result = Number1 + Number2
  Op = " + "
if Operation == 2 :
  Result = Number1 - Number2
  Op = " - "
if Operation == 3 :
  Result = Number1 * Number2
  Op = " * "
if Operation == 4 :
  Result = Number1 / Number2
  Op = " / "
print("Задача:")
print(str(Number1) + Op + str(Number2) + " =")
print("Твой результат: ", end="")
Input = int(input())
if Input == Result :
  print("Правильно")
else :
  print("Результат = " + str(Result))
