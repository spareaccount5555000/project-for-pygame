import pygame
import random

pygame.init()
pygame.font.init()

screen_x = 800
screen_y = 600
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Catch the falling blocks")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

player_width = 50
player_height = 20
player_x = screen_x // 2 - player_width // 2
player_y = screen_y - player_height - 10
player_vel = 5

block_size = 30
block_vel = 3
block_x = random.randint(0, screen_x - block_size)
block_y = 0

score = 0

while True:
    clock.tick(60)
    screen.fill("white")   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < screen_x - player_width:
        player_x += player_vel

    block_y += block_vel

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_size, block_size)

    if player_rect.colliderect(block_rect):
        score += 1
        block_x = random.randint(0, screen_x - block_size)
        block_y = 0
        block_vel += 0.3  

    if block_y > screen_y:
        block_x = random.randint(0, screen_x - block_size)
        block_y = 0

    if score >= 10:
        wintext = font.render("You Won!", True, "black")
        screen.blit(wintext, (screen_x//2, screen_y//2))

    
    pygame.draw.rect(screen, "blue", player_rect)
    pygame.draw.rect(screen, "red", block_rect)

    score_text = font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.update()



