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
#enemies.append(Actor("bug")) 
#enemies[-1].x = 10
#enemies[-1].y = -100
score = 0
direction = 1
spaceship.dead = False
spaceship.countdown = 90

for x in range(8):
    for y in range(4):
        enemies.append(Actor("bug")) 
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y
def gameOver():
    screen.draw.text("GAME OVER", (250, 300))

def draw():
    screen.clear()
    screen.fill("blue")
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if spaceship.dead == False:
        spaceship.draw()
    displayScore()
    if len(enemies) == 0:
        gameOver()
    
def displayScore():
    screen.draw.text(str(score), (50, 30))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        bullets[-1].x = spaceship.x
        bullets[-1].y = spaceship.y - 50
        
def update():
    global score
    global direction
    move_down = False
    if spaceship.dead == False:
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

    if len(enemies) == 0:
        gameOver()

    if len(enemies) > 0 and enemies[-1].x > WIDTH - 80 or enemies[0].x < 80:
        move_down = True
        direction = direction *- 1

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