# Отметка
print("Введи число: ", end="")
Score = int(input())
print("Это ", end = "")
if (Score >= 0) and (Score < 1) :
  print("ужасно (6)")
if (Score >= 1) and (Score < 3) :
  print("плохо (5)")
if (Score >= 3) and (Score < 5) :
  print("сойдет (4)")
if (Score >= 5) and (Score < 7) :
  print("средне (3)")
if (Score >= 7) and (Score < 9) :
  print("хорошо (2)")
if (Score >= 9) and (Score <= 10) :
  print("очень хорошо (1)")
if (Score > 10) or (Score < 0) :
  print("неправильно (0)")
