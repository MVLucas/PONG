from PPlay.window import *
from PPlay.sprite import *
from PPlay.sound import *


#def reset(wind, pad1, pad2, ball):
#    ball.set_position((wind.width / 2) - ball.width / 2, (wind.height / 4) - ball.height / 2)
#    pad1.set_position(30, (wind.height / 2) - pad1.height / 2)
#    pad2.set_position(wind.width - (30 + pad2.width), (wind.height / 2) - (pad2.height / 2))


# Programa do PONG!. Jogo onde o objetivo e nao deixar a bola passar por vc.

# Window:
janela = Window(800, 600)
janela.set_title("PONG!")

# Background:
fundo = Sprite("Imagens/fundo.jpg")
fundo.x = 0
fundo2 = Sprite("Imagens/fundo.jpg")
fundo2.set_position(800, 0)


# music:
musica = Sound("pong2.ogg")
musica.set_volume(8)
musica.set_repeat(repeat=True)

# Sprites:
# ball:
bola = Sprite("Imagens/bola.png")
bola.set_position((janela.width/2) - bola.width/2, (janela.height/4) - bola.height/2)

# Players:
blue = Sprite("Imagens/BLUE.png")
blue.set_position(30, (janela.height/2) - blue.height/2)

red = Sprite("Imagens/RED.png")
red.set_position(janela.width - (30 + red.width), (janela.height / 2) - (red.height/2))

# WIN:
win = Sprite("Imagens/WIN.png")
win.set_position((janela.width/2) - win.width/2, (janela.height/2) - win.height/2)

# keyboard:
teclado = Window.get_keyboard()

# mouse:
rato = Window.get_mouse()

# speeds:
velocidade_bolax = 450
velocidade_bolay = 500

velocidade_blue = 280
velocidade_red = 280

velocidade_fundo = 100

# score:
blue_score = 0
red_score = 0


while True:

    janela.set_background_color((255, 255, 255))

    # background movement:

    fundo.move_x(-(velocidade_fundo * janela.delta_time()))
    fundo2.move_x(-(velocidade_fundo * janela.delta_time()))

    if fundo.x < -800:
        fundo.x = 0
        fundo2.x = 800

    # pads movement:
    if teclado.key_pressed("W"):
        blue.y -= (velocidade_blue * janela.delta_time())
    if teclado.key_pressed("S"):
        blue.y += (velocidade_blue * janela.delta_time())

    # moving with mouse:
#    rx, ry = rato.get_position()

#    if ry > janela.height/2 + bola.height:
#        red.y += (velocidade_red * janela.delta_time())
#    if ry < janela.height/2:
#        red.y -= (velocidade_red * janela.delta_time())

    # IA of computer(red):
    if bola.x > (janela.width/2):
        red.move_y(velocidade_bolay * janela.delta_time())
        if red.y > 300 > bola.y:
            red.move_y(-velocidade_red * janela.delta_time())
        elif red.y < 300 < bola.y:
            red.move_y(velocidade_red * janela.delta_time())

    # pads collision with ceiling and floor:
    if blue.y < 0:
        blue.y = 0
    if blue.y + blue.height > janela.height:
        blue.y = janela.height - blue.height
    if red.y < 0:
        red.y = 0
    if red.y + red.height > janela.height:
        red.y = janela.height - red.height

    # ball movement:
    bola.move_x(velocidade_bolax * janela.delta_time())
    bola.move_y(velocidade_bolay * janela.delta_time())

    # ball collision:
    if bola.y + bola.height > janela.height:
        bola.y -= 1
        velocidade_bolay *= -1
    if bola.y < 0:
        bola.y += 1
        velocidade_bolay *= -1
    if (bola.x + bola.width) < 0:
        velocidade_bolax *= -1
        bola.set_position((janela.width / 2) - bola.width / 2, (janela.height / 4) - bola.height / 2)
        red_score += 1
    if bola.x > janela.width:
        velocidade_bolax *= -1
        bola.set_position((janela.width / 2) - bola.width / 2, (janela.height / 4) - bola.height / 2)
        blue_score += 1

    # ball collision with pads:

    # CANTOS DA BOLA:
    # bola.x, bola.y = canto SUPERIOR ESQUERDO da bola
    # bola.x, (bola.y + bola.height) = canto INFERIOR ESQUERDO da bola
    # (bola.x + bola.width), bola.y = canto SUPERIOR DIREITO da bola
    # (bola.x + bola.width), (bola.y + bola.height) = canto INFERIOR DIREITO da bola

    # CANTOS DE PADS:
    # pad.x, pad.y = canto SUPERIOR ESQUERDO do pad
    # pad.x, (pad.y + pad.height) = canto INFERIOR ESQUERDO do pad
    # (pad.x + pad.width), pad.y = canto SUPERIOR DIREITO ddo pad
    # (pad.x + pad.width), (pad.y + pad.height) = canto INFERIOR DIREITO do pad

    if bola.x <= (blue.x + blue.width) and (blue.y + blue.height) >= bola.y >= blue.y \
            or bola.x <= (blue.x + blue.width) and (blue.y + blue.height) >= (bola.y + bola.height) >= blue.y:
        bola.x = bola.x + blue.width
        velocidade_bolax *= -1
    if (bola.x + bola.width) >= red.x and (red.y + red.height) >= bola.y >= red.y \
            or (bola.x + bola.width) >= red.x and (red.y + red.height) >= (bola.y + bola.height) >= red.y:
        bola.x = bola.x - red.width
        velocidade_bolax *= -1

    if bola.x <= (blue.x + blue.width) and (blue.y + blue.height) >= bola.y >= blue.y:
        bola.x = bola.x + blue.width
        velocidade_bolax *= -1

    if (bola.x + bola.width) >= red.x and (red.y + red.height) >= bola.y >= red.y:
        bola.x -= red.width
        velocidade_bolax *= -1
        velocidade_bolay *= -1

#    if ponto1 >= 5:
#        reset(janela, blue, red, bola)
#        ponto1 = 0

    # if bug press space bar:
    if teclado.key_pressed("SPACE"):
        velocidade_bolax *= -1

    # press 'ESC' to exit:
    if teclado.key_pressed("ESC"):
        janela.close()

    # draw dos gameobjects:
    fundo.draw()
    fundo2.draw()
    bola.draw()
    blue.draw()
    red.draw()
    # pontuacao:
    janela.draw_text(str(blue_score), 20, 5, size=20, color=[50, 50, 255], font_name="Arial", bold=True)
    janela.draw_text(str(red_score), (janela.width - 32), 5, size=20, color=[255, 50, 50], font_name="Arial", bold=True)

    musica.play()

    # atualizacao da janela e talvez alguma animacao:
    janela.update()
