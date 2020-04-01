# Age
print("Привет, я - твой компьютер и мне 5 лет.")
print("А тебе сколько лет? ")
Age = int(input())
if (Age > 0) and (Age <= 15) :
  print("Ой, какой ты маленький")
if (Age > 15) and (Age <= 25) :
  print("Молоденький и свеженький")
elif (Age > 25) and (Age <= 40) :
  print("В самом расцвете сил")
elif (Age > 40) and (Age <= 65) :
  print("Скоро на пенсию?")
elif (Age > 65) and (Age <= 80) :
  print("Старость, золотая старость")
else :
  print("Ух, ты прожил целых на " + str(Age-80) + " лет дольше, чем я думал!!")


