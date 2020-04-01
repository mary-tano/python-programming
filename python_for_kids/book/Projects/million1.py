# Миллионер
import random
Capital = random.randint(2,10)*10000
print("Ты выиграл в лотерею " + str(Capital) + " рублей!")
print("Ты можешь не забирать выигрыш сразу, ", end="")
print("а вложить деньги и заработать на этом!")
print("Процентная ставка: ", end="")
Percent = float(input())
Clearance = 0
while Capital < 1000000 :
  Fee   = Capital * Percent / 100
  Capital  = Capital + Fee
  Clearance += 1
print("Чтобы стать миллионером, тебе понадобится ", end="")
print(str(Clearance) + " лет.")
