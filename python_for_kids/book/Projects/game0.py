# Импорт Pygame
import pygame

# Запуск Pygame, создание окна
pygame.init()
pygame.display.set_mode((600, 400))

# Цикл событий
running = True
while running :
  for event in pygame.event.get() :
    if event.type == pygame.QUIT :
      running = False

# Завершение Pygame
pygame.quit()
