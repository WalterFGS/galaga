import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

WHITE = "255, 0, 255"
BLUE = "0, 0, 255"

spaceship  = Actor("galaga")
bug = Actor("bug")

spaceship.pos = (WIDTH // 2, HEIGHT  -60)

speed = 5

bullets = []
enemies = []
enemies.append(Actor("bug")) 
enemies[-1].x = 10
enemies[-1].y = -100

def draw():
    screen.clear()
    screen.fill("blue")
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    spaceship.draw()
    displayScore()
    
score = 0
def displayScore():
    screen.draw.text(str(score), (50, 30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x = spaceship.x
        bullets[-1].y = spaceship.y - 50
        
def update():
    global score

    if keyboard.left:
        spaceship.x -= speed
        if spaceship.x <= 0:
            spaceship.x = 0

    if keyboard.right:
        spaceship.x += speed
        if spaceship.x >= WIDTH:
            spaceship.x = WIDTH

    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    for enemy in enemies:
        enemy.y += 5
        
        # Assuming HEIGHT is defined as the bottom of the screen
        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(50, WIDTH - 50)

        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                if bullet in bullets:
                    bullets.remove(bullet) 
                if enemy in enemies:
                    enemies.remove(enemy)
                break

pgzrun.go()