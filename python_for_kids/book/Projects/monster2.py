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

# Основная программа
Frank = Monster("Фрэнки", "необычный")
Frank.show()

