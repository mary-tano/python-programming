# Среднее значение
print("Введи число: ", end="")
Sum = 0
Value = int(input())
for Number in range(1,Value+1) :
  Sum += Number
Mean = Sum / Value
print("Результат: " + str(Mean))
