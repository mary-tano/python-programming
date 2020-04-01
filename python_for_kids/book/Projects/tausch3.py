# Обмен строк

def exchange(x1, x2) :
  Swap = x1
  x1 = x2
  x2 = Swap
  print ("Меняем " + str(x1) + " и " +str(x2))
  return x1, x2

# Основная программа
print("Введи слово: ", end="")
Word1 = input()
print ("И еще одно: ", end="")
Word2 = input()
print ("До обмена: " + Word1 + " и " + Word2)
Word1, Word2 = exchange(Word1, Word2)
print ("После обмена: " + Word1 + " и " + Word2)

