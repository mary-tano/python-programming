class InterCalc(object) :

  # Инициализация атрибута
  def __init__(self) :
    self.Capital = 1
    self.Percent = 1
    self.Fee = 1
   
  # Метод
  def setCapital(self) :
    self.Capital = float(input())
  def setPercent(self) :
    self.Percent = float(input())
  def setFee(self) :
    self.Fee = float(input())

  def getCapital(self) :
    self.Capital = self.Fee * 100 / self.Percent
    return self.Capital
  def getPercent(self) :
    self.Percent = self.Fee * 100 / self.Capital
    return self.Percent
  def getFee(self) :
    self.Fee = self.Capital * self.Percent / 100
    return self.Fee

# Основная программа
Money = InterCalc()
print("Капитал: ", end="")
Money.setCapital()
print("Процентная ставка: ", end="")
Money.setPercent()
print("Доход = " + str(Money.getFee()))

