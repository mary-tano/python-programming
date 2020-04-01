# Сумма целых чисел
print("Суммируем: ", end="")
Sum = 0
Value = int(input())
for Number in range(1,Value+1) :
  Sum += Number
print("Результат: " + str(Sum))
