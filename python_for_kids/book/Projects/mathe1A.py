# Математика
print("Введи число: ", end="")
Number1 = int(input())
print ("Введи еще одно число: ", end="")
Number2 = int(input())
print ("А теперь выбери операцию (+,-,*,/): ", end="")
Operator = input()
print ("Результат = ", end="")
if Operator == "+" :
  print(Number1 + Number2)
if Operator == "-" :
  print(Number1 - Number2)
if Operator == "*" :
  print(Number1 * Number2)
if Operator == "/" :
  print(Number1 / Number2)
