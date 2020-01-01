import pygame as pg

pg.init()

win = pg.display.set_mode((500, 500))

pg.display.set_caption("First Game")

x = 50
y = 40
width = 30
height = 80
vel = 5
delay_time = 20


run = True
while run:
    pg.time.delay(delay_time)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x -= vel
    if keys[pg.K_RIGHT]:
        x += vel
    if keys[pg.K_UP]:
        y -= vel
    if keys[pg.K_DOWN]:
        y += vel

    win.fill((0, 0, 0))
    pg.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()