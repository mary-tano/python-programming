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
Window.fill(White)

# Цикл событий
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False
  # Рисование
  pygame.draw.rect(Window, Blue, (100, 50, 400, 100))
  pygame.draw.ellipse(Window, Yellow, (100, 250, 400, 100))
  pygame.draw.line(Window, Black, (50,50), (550,350), 5)
  pygame.draw.line(Window, Black, (550,50), (50,350), 5) 
  pygame.display.update()

# Завершение Pygame
pygame.quit()
