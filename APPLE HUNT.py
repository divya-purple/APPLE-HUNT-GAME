import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
FRUIT_SIZE = 50
BULLET_SIZE = 20
TARGET_SCORE = 30
GUN_SIZE = 50

fruits = []
bullets = []
gun_x = WIDTH / 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

score = 0
font = pygame.font.SysFont('Arial', 36)

pygame.display.set_caption("APPLE HUNT")

fruit_image = pygame.image.load('C:\\Users\\Admin\\New folder\\pygames\\apple.png')
fruit_image = pygame.transform.scale(fruit_image, (FRUIT_SIZE, FRUIT_SIZE))

# CLASS FRUIT
class Fruit:
    def __init__(self):
        self.rect = fruit_image.get_rect()
        self.rect.x = random.randint(0, WIDTH - FRUIT_SIZE)
        self.rect.y =  -FRUIT_SIZE 
    def update(self):
            self.rect.y += 5

# CLASS BULLET
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)

fruits = [Fruit() for _ in range(10)]

# GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(gun_x, HEIGHT - GUN_SIZE))

  # GUN MOVEMENT          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gun_x -= 5
    if keys[pygame.K_RIGHT]:
        gun_x += 5

#FOR FRUIT
    for fruit in fruits:
        fruit.update()
        if fruit.rect.y > HEIGHT:
            fruits.remove(fruit)

#FOR BULLET
    for i, bullet in enumerate(bullets):
        bullet.rect.y -= 10
        if bullet.rect.y < 0:
            bullets.remove(bullet)
  
# COLLISIONS  
    for fruit in fruits:
        for bullet in bullets:
            if fruit.rect.colliderect(bullet.rect):
                fruits.remove(fruit)
                bullets.remove(bullet)
                score += 1
                print("Fruit splashed!")

# FINAL
    if score >= TARGET_SCORE:
            print('Congradulations! you won!')
            pygame.quit()
            quit()

# SPEED 
    if random.random() < 0.03:
        fruits.append(Fruit())

# APPEARENCE
    screen.fill((255, 255, 255))
    for fruit in fruits:
        screen.blit(fruit_image, fruit.rect)
    
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), (bullet.rect.x, bullet.rect.y , BULLET_SIZE, BULLET_SIZE))
    pygame.draw.rect(screen, (0, 0, 0), (gun_x, HEIGHT - GUN_SIZE, GUN_SIZE, GUN_SIZE))
    
    
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()

    pygame.time.Clock().tick(60)