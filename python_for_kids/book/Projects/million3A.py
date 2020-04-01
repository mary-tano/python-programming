# Время миллионеров
print("Какую сумму ты хочешь инвестировать: ")
Capital = float(input())
print("Процентная ставка: ")
Percent = float(input())
print("На какой срок ты вкладываешь деньги: ")
Clearance = int(input())
while Clearance > 0 :
  Fee   = Capital * Percent / 100
  Capital  = Capital + Fee
  Clearance -= 1
print("Так ты получишь " + str(Capital) + " рублей")
if Capital < 1000000 :
  print("Но так ты не станешь миллионером!")
else :
  print("Добро пожаловать в Клуб Миллионеров!")



