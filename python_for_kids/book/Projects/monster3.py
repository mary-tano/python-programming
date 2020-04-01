# Лаборатория Франкенштейна
class Monster :
  # Инициализация атрибута
  def __init__(self, name, character) :
    self.Name = name
    self.Character = character
  # Метод
  def show(self) :
    print("Имя: " + self.Name)
    print("Особенность: " + self.Character)

class GMonster (Monster):
  pass

class SMonster (Monster):
  pass

# Основная программа
Frank = Monster("Фрэнки", "необычный")
Frank.show()
Albert = GMonster("Альберт", "задумчивый")
Albert.show()
Sigmund = SMonster("Зигмунд", "веселый")
Sigmund.show()

