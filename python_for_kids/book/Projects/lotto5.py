# Лото
import random

Ball = []
Lotto = [0,0,0,0,0,0]
# Все числа еще не "вытащены"
for Nr in range(1,50) :
  Ball.append(False)
Case = random.randint(1,49)
# "Вытягивается" шесть чисел
for Nr in range(6) :
  # поиск неиспользованных чисел
  while Ball[Case] :
    Case = random.randint(1,49)
  # Пометка использованного числа "вытащенным" und merken
  Ball[Case] = True
  Lotto[Nr] = Case
# Сортировка и отображение
Lotto.sort()
print(Lotto)

