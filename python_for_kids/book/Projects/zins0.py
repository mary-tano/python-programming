class InterCalc(object) :
  Capital = 1
  Percent = 1
  Fee = 1

  # Функция
  def setCapital(self, Capital) :
    self.Capital = float(input())
  def setPercent(self, Percent) :
    self.Percent = float(input())
  def setFee(self, Fee) :
    self.Fee = float(input())

  def getCapital(self, Capital) :
    self.Capital = self.Fee * 100 / self.Percent
    return self.Capital
  def getPercent(self, Percent) :
    self.Percent = self.Fee * 100 / self.Capital
    return self.Percent
  def getFee(self, Fee) :
    self.Fee = self.Capital * self.Percent / 100
    return self.Fee

# Основная программа

Money = InterCalc()
Money.setCapital(Money)
print(str(Money.getCapital(Money)))


