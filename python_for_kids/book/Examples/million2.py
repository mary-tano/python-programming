# Миллионер
print("Какую сумму ты хочешь инвестировать: ", end="")
Capital = float(input())
print("Процентная ставка: ", end="")
Percent = float(input())
Term = 0
while Capital < 1000000 :
  Fee   = Capital * Percent / 100
  Capital  = Capital + Fee
  Term += 1
if Term > 0 :
  print("Чтобы тебе превратиться в миллионера, твои деньги в течение ", end="")
  print(str(Term) + " лет должны быть в банке.")
else :
  print("Добро пожаловать в Клуб Миллионеров!")
