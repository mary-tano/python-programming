# Лото
import random
Ball = []
# Все шары еще не "вытащены"
for Nr in range(1,50) :
  Ball.append(False)
Case = random.randint(1,49)
# "Вытягивается" шесть шаров
for Nr in range(6) :
  # поиск неиспользованных шаров
  while Ball[Case] :
    Case = random.randint(1,49)
  # Пометка использованного шара "вытащенным"
  Ball[Case] = True
  print("№ " + str(Nr+1) + " => " + str(Case))
  

