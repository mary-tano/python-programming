# Импорт Pygame
import pygame

# Определение цветов
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
Cyan = (0,255,255)
Magenta = (255,0,255)
Yellow = (255,255,0)
White = (255,255,255)
Black = (0,0,0)

# Запуск Pygame, создание окна
pygame.init()
Window = pygame.display.set_mode((600, 400))
Window.fill(Green)

# Цикл событий
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False
  # Рисование круга
  Circle = pygame.draw.circle(Window, Red, (300, 200), 100)
  pygame.display.update()

# Завершение Pygame
pygame.quit()
