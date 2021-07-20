import pygame

pygame.init()

# 游戏代码

#hero_rect = pygame.Rect(0, 0, 200, 100)
screen = pygame.display.set_mode((480, 700))

# 1、加载图像
bg = pygame.image.load("./images/background.png")
# 2、绘制图像
screen.blit(bg, (0, 0))
# 3、更新图像
pygame.display.update()
while True:
    pass

#pygame.quit()
