# Лото
import random
Ball = []
# Все числа еще не "вытащены"
for Nr in range(1,50) :
  Ball.append(False)
Case = random.randint(1,49)
# "Вытягивается" шесть чисел
for Nr in range(6) :
  # поиск неиспользованных чисел
  while Ball[Case] :
    Case = random.randint(1,49)
  # Пометка использованного числа "вытащенным"
  Ball[Case] = True
  print("№ " + str(Nr+1) + " => " + str(Case))
  

