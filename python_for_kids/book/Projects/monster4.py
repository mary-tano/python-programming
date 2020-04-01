# Лаборатория Франкенштейна
class Monster :
  # Инициализация атрибута
  def __init__(self, name, character) :
    self.Name = name
    self.Character = character
  # Метод
  def Type(self) :
    return "Монстр"
  def show(self) :
    print("Имя: " + self.Name)
    print("Особенность: " + self.Character)
    print("Typ:   " + self.Type())

class GMonster (Monster):
  # Метод
  def Type(self) :
    return "Дух монстра"

class SMonster (Monster):
  # Метод
  def Type(self) :
    return "Душа монстра"

# Основная программа
Frank = Monster("Фрэнки", "необычный")
Frank.show()
Albert = GMonster("Альберт", "задумчивый")
Albert.show()
Sigmund = SMonster("Зигмунд", "веселый")
Sigmund.show()

