import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
white=(255,255,255)
screen.fill(white)

pygame.display.update()

spider_man = pygame.image.load("spiderman.png")
spider_man=pygame.transform.scale(spider_man, (70,100))
bat_man = pygame.image.load("batman.png")
bat_man=pygame.transform.scale(bat_man, (70,100))
super_man= pygame.image.load("superman.png")
super_man=pygame.transform.scale(super_man, (70,100))
hulk = pygame.image.load("hulk.png")
hulk=pygame.transform.scale(hulk, (70,100))

screen.blit(spider_man, (150,100))
screen.blit(bat_man, (150,200))
screen.blit(super_man, (150,300))
screen.blit(hulk, (150,400))

font = pygame.font.SysFont("Georgia", 20)

text1 = font.render("Spider man", True, (0,0,0))
text2 = font.render("Hulk", True, (0,0,0))
text3 = font.render("Bat man", True, (0,0,0))
text4 = font.render("Super man", True, (0,0,0))

screen.blit(text1, (350,100))
screen.blit(text2, (350,200))
screen.blit(text3, (350,300))
screen.blit(text4, (350,400))

pygame.display.update()
while True:
    event = pygame.event.poll()
    
    if event.type==pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (255,0,0),(pos), 20, 0)
        pygame.display.update()
    
    elif event.type==pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, (0,0,0), (pos), (pos2), 6)
        pygame.draw.circle(screen, (255,0,0), (pos2), 20, 0)
        pygame.display.update()