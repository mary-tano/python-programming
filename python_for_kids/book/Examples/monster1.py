# Лаборатория Франкенштейна
class Monster :
  # Атрибут
  Name = "Фрэнки"
  Character = "необычный"
  # Метод
  def show(self) :
    print("Имя: " + self.Name)
    print("Особенность: " + self.Character)

# Основная программа
Frank = Monster()
Frank.show()
