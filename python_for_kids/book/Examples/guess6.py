import random, time
Secret = "Компьютер задумался"
Case = random.randint(1,1000)
print(Secret)
print("Число: " + str(Case))
Minimum = 1
Maximum = 1000 
Attempt = 0
Number = 0
while Case != Number :
  Attempt = Attempt + 1
  Number = Number = int((Maximum+Minimum)/2)
  time.sleep(1)
  print(str(Attempt) + ". Попытка: " + str(Number))
  if Number < Case : 
    print("больше")
    Minimum = Number
  if Number > Case :
    print("меньше")
    Maximum  = Number
print("Угадал после " + str(Attempt) + " попыток.")
