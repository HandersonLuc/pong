from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *

janela = Window(900, 600)
janela.set_title("Pong do Hand")
cenario = GameImage("imagem.jpg")

bola = Sprite("pngimg.com - football_PNG52789.png")
bola.x = janela.width/2 - bola.width/2
bola.y = janela.height/2 - bola.height/2

barra = Sprite("New Piskel(2).png")
barra2 = Sprite("New Piskel(2).png")
barra.x = 10
barra2.x = janela.width - barra2.width - 10

teclado = Window.get_keyboard()
start = False
velx = 0.8
vely = -0.5
ponto_d = 0
ponto_e = 0
while True:
    if start:
        bola.x += velx
        bola.y += vely

    if bola.x < 0:
        velx = 0.8
        ponto_d += 1
        bola.set_position((janela.width/2) - (bola.width/2), (janela.height/2) - (bola.height/2))
        start = False
    elif bola.x > janela.width:
        velx = 0.8
        ponto_e += 1
        bola.set_position((janela.width/2) - (bola.width/2), (janela.height/2) - (bola.height/2))
        start = False
    if teclado.key_pressed("space"):
        start = True

    if bola.y >= janela.height - bola.height or bola.y <= 0:
        vely *= -1

    if teclado.key_pressed("UP"):
        barra.y -= 0.4
    elif teclado.key_pressed("DOWN"):
        barra.y += 0.4

    if barra.y < 0:
        barra.y = 0
    elif barra.y > janela.height - barra.height:
        barra.y = janela.height - barra.height

    if barra2.y < 0:
        barra2.y = 0
    elif barra2.y > janela.height - barra2.height:
        barra2.y = janela.height - barra2.height

    if bola.collided(barra2) and velx > 0:
        velx *= -1
        velx -= 0.2

    elif bola.collided(barra) and velx < 0:
        velx *= -1
        velx += 0.2
    if (bola.y + bola.height/2) < (barra2.y + barra2.height/2):
        barra2.y -= 0.4
    elif (bola.y + bola.height/2) > (barra2.y + barra2.height/2):
        barra2.y += 0.4
    cenario.draw()
    janela.draw_text(str(ponto_d), 500, 15, size=40, color=(214, 255, 3), font_name="Arial", bold=False, italic=False)
    janela.draw_text(str(ponto_e), 400, 15, size=40, color=(214, 255, 3), font_name="Arial", bold=False, italic=False)

    bola.draw()
    barra.draw()
    barra2.draw()
    janela.update()
