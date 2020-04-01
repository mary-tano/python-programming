import pygame as pg

class Game :

  # Запуск и создание текстового поля
  def __init__(self, Color) :
    self.Start = 0
    self.Score = 0
    self.Text = pg.Surface((300,50))
    self.Text.fill(Color)

  # Вывод информации
  def showMessage(self, text, Color) :
    self.Font = pg.font.SysFont("arial", 48)
    self.Text = self.Font.render(text, True, Color)

  # Подсчет и вывод очков
  def setScore(self, num, Color) :
    self.Score += num
    self.showMessage("Счет: " + str(self.Score), Color)

  # Таймер
  def getTime(self, Reset) :
    if Reset :
      self.Start = pg.time.get_ticks()
    self.Diff = pg.time.get_ticks() - self.Start
    return self.Diff

  # Счет и время
  def showAll(self, num, Color) :
    self.Score += num
    ptext = "  |  Счет: " + str(self.Score)
    ztext = "Время: " + str(int(self.Diff/1000))
    self.showMessage(ztext+ptext, Color)
