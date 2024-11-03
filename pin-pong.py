from pygame import *
mixer.init()
font.init()
#класы
#ласс родитель для игроков
class Game_sprite(sprite.Sprite):
#основы
    def __init__(self,image2,x,y,sprint,razmer_x,razmer_y):
        super().__init__()
        self.image = transform.scale(image.load(image2),(razmer_x, razmer_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sprint = sprint
    def show(self):
        windows.blit(self.image,(self.rect.x,self.rect.y))
#для игрока
class Player(Game_sprite):
#передвежение для игрока
    def tuda_sida_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.sprint
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.sprint
    def tuda_sida_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.sprint
        if keys_pressed[K_s] and self.rect.y < 430:
            self.rect.y += self.sprint
#надписи
font3 = font.SysFont('Arial', 70)
Game_over1 = font3.render('Game over Player 1' , True , (255, 0, 0))
Game_over2 = font3.render('Game over Player 2' , True , (255, 0, 0))
#скорость
speed_x = 3
speed_y = 3
#
finish = False
#FPS
clock = time.Clock()
fps = 60
#стандартные размеры спрайтов
razmer_x = 65
razmer_y = 65
#окно
windows = display.set_mode((700, 500))
display.set_caption('pygame window')
#задай фон сцены
background = transform.scale(image.load('fon.png'),(700, 500))
excep = True
#объекты
player_1 = Player('stena.png', 640, 250, 10, 30, 70)
player_2 = Player('stena.png', 60, 250, 10, 30, 70)
ball = Game_sprite('ball.png', 350, 250, 10, 50, 50)
#цикл
while excep != False:
    windows.blit(background,(0, 0))
    for i in event.get():
        if i.type == QUIT:
            excep = False
    if finish != True:
#полёт мяча
        ball.rect.x += speed_x
        ball.rect.y += speed_y
#отбрасывание мяча от хлеба
        if sprite.collide_rect(ball,player_1) or sprite.collide_rect(ball,player_2):
            speed_x *= -1
#отбрасывание мяча от стен
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.y > 450:
            speed_y *= -1
#события
        if ball.rect.x > 650:
            windows.blit(Game_over1 , (50 , 250))
            finish = True
        if ball.rect.x < 0:
            windows.blit(Game_over2 , (50 , 250))
            finish = True
#player_1
        player_1.tuda_sida_l()
        player_1.show()
#player_2
        player_2.tuda_sida_r()
        player_2.show()
#ball
        ball.show()
#FPS
        display.update()
        clock.tick(fps)