# Обратное число
try :
  print("Введи число: ")
  Number = float(input())
  if Number != 0 :
    print(1/Number);
  else :
    print("Нет результата");
except :
  print("Нет числа!")

