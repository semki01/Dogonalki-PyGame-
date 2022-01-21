from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Dog Nalki')
background = transform.scale(image.load('background.jpg'), (700, 500))

#данные о спрайте картинки
x1 = 500
y1 = 300

x2 = 100
y2 = 283

sprite_1 = transform.scale(image.load('Cat Nalki.png'), (100, 100))
sprite_2 = transform.scale(image.load('Dog Nalki.png'), (130, 130))
speed = 10

#игровой цикл

run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(background,(0,0))
    window.blit(sprite_1,(x1,y1))
    window.blit(sprite_2,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            run = False
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    
    if keys_pressed[K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed
    if keys_pressed[K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    display.update()
    clock.tick(FPS)
