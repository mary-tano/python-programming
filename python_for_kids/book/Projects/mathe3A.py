# Математика
try :
  print("Введи число: ", end="")
  Number1 = float(input())
  print ("Введи еще одно число: ", end="")
  Number2 = float(input())
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
    if Number2 != 0:
      print(Number1 / Number2)
    else:
      print("невозможно вычислить")
except :
  print("Не число!")

