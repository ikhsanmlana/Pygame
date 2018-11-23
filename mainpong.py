import pygame, sys, time
from pygame.locals import *
import random
from random import randint


pygame.init()

WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 600

clock = pygame.time.Clock()

player1_win = False
player2_win = False
bot_win = False

UP1 = False
DOWN1 = False
NO_MOVEMENT1 = True

UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True

UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
surface_rect = main_surface.get_rect()
pygame.display.set_caption('Pong')

basic_font = pygame.font.SysFont("Helvetica", 120)
game_over_font_big = pygame.font.SysFont("Helvetica", 72)
game_over_font_small = pygame.font.SysFont("Helvetica", 50)

bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)
normalfont = pygame.font.Font(None, 69)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, player_number):

        pygame.sprite.Sprite.__init__(self)

        self.player_number = player_number
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 8


        if self.player_number == 1:
            self.rect.centerx = main_surface.get_rect().left
            self.rect.centerx += 50
        elif self.player_number == 2:
            self.rect.centerx = main_surface.get_rect().right
            self.rect.centerx -= 50
        self.rect.centery = main_surface.get_rect().centery

    def move(self):

        if self.player_number == 1:
            if (UP1 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN1 == True) and (self.rect.bottom < WINDOW_HEIGHT - 5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT1 == True):
                pass

        if self.player_number == 2:
            if (UP2 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN2 == True) and (self.rect.bottom < WINDOW_HEIGHT - 5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT2 == True):
                pass


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = surface_rect.centerx
        self.rect.centery = surface_rect.centery
        self.direction = randint(0, 3)
        self.speed = 4

    def move(self):
        if self.direction == UPLEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == UPRIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == DOWNLEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.direction == DOWNRIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed

    def change_direction(self):
        if self.rect.y < 0 and self.direction == UPLEFT:
            self.direction = DOWNLEFT
        if self.rect.y < 0 and self.direction == UPRIGHT:
            self.direction = DOWNRIGHT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNLEFT:
            self.direction = UPLEFT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNRIGHT:
            self.direction = UPRIGHT




def paddle_hit():
    if pygame.sprite.collide_rect(ball, paddle2):
        if (ball.direction == UPRIGHT):
            ball.direction = UPLEFT
        elif (ball.direction == DOWNRIGHT):
            ball.direction = DOWNLEFT
        ball.speed += 1

    elif pygame.sprite.collide_rect(ball, paddle1):
        if (ball.direction == UPLEFT):
            ball.direction = UPRIGHT
        elif (ball.direction == DOWNLEFT):
            ball.direction = DOWNRIGHT
        ball.speed += 1

def solo_hit():
    if ball.rect.x == UPRIGHT or ball.rect.x == DOWNRIGHT or ball.rect.x <= 0:
        if (ball.direction == UPLEFT):
            ball.direction = UPRIGHT
        elif (ball.direction == DOWNLEFT):
            ball.direction = DOWNRIGHT
        ball.speed += 1

def square(x,y,w,h,color):
    pygame.draw.rect(main_surface, color, (x,y,w,h))



paddle1 = Paddle(1)
paddle2 = Paddle(2)

ball = Ball()

all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball)
solo_sprite = pygame.sprite.RenderPlain(paddle2, ball)

player1_score = 0
player2_score = 0
bot_score = 0



def multiplayer():
    text = normalfont.render('Single Player', 13, BLACK)

    textx = WINDOW_WIDTH / 2 - text.get_width() / 2
    texty = WINDOW_HEIGHT / 1.8 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()

    text1 = bigfont.render('Multiplayer', 13, BLACK)
    textx1 = WINDOW_WIDTH / 2 - text.get_width() / 2
    texty1 = WINDOW_HEIGHT / 2.5 - text.get_height() / 2
    textx_size1 = text.get_width()
    texty_size1 = text.get_height()


    pygame.draw.rect(main_surface, (255, 255, 255), ((textx - 5, texty - 5),
                                               (textx_size + 10, texty_size +
                                                10)))



    pygame.draw.rect(main_surface, (255, 255, 255), ((textx1 - 5, texty1 - 5),
                                                     (textx_size1 + 10, texty_size1 +
                                                      10)))

    main_surface.blit(text, (WINDOW_WIDTH / 2 - text.get_width() / 2,
                             WINDOW_HEIGHT / 2.5 - text.get_height() / 2))

    main_surface.blit(text1, (WINDOW_WIDTH / 2 - text.get_width() / 2,
                             WINDOW_HEIGHT / 1.8 - text.get_height() / 2))



    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
                pygame.display.quit()
                pygame.quit()
                quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x >= textx - 5 and x <= textx + textx_size + 5:
                    if y >= texty - 5 and y <= texty + texty_size + 5:
                        time.sleep(1)
                        game_multi()
                if x >= textx1 - 5 and x <= textx1 + textx_size1 + 5:
                    if y >= texty1 - 5 and y <= texty1 + texty_size1 + 5:
                        time.sleep(1)
                        game_solo()



counter = 0


def game_solo():
    paddle2.speed = 10
    player1_score = 0
    bot_score = 0
    global UP1
    global DOWN1
    global NO_MOVEMENT1
    global UP2
    global DOWN2
    global NO_MOVEMENT2
    global player1_win
    global player2_win
    global bot_win
    global gamestat
    global counter
    global game_over
    global game_over1
    square_y = random.randrange(0, WINDOW_HEIGHT)
    square_x = 0
    square_width = 75
    square_height = 75
    ball.rect.centerx = surface_rect.centerx
    ball.rect.centery = surface_rect.centery
    ball.speed = 6
    while True:
        clock.tick(60)


        if (ball.rect.x > WINDOW_WIDTH):
            ball.rect.centerx = surface_rect.centerx
            ball.rect.centery = surface_rect.centery
            ball.direction = randint(2, 3)
            ball.speed = 6

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


                elif event.key == K_UP:
                    UP2 = True
                    DOWN2 = False
                    NO_MOVEMENT2 = False

                elif event.key == K_DOWN:
                    UP2 = False
                    DOWN2 = True
                    NO_MOVEMENT2 = False
                elif event.key == ord('p'):
                    multiplayer()


            elif event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_UP:
                    NO_MOVEMENT2 = True
                    DOWN2 = False
                    UP2 = False


        score_board = basic_font.render(str(bot_score) + "           " + str(player1_score), True, WHITE, BLACK)
        score_board_rect = score_board.get_rect()
        score_board_rect.centerx = surface_rect.centerx
        score_board_rect.y = 10

        main_surface.fill(BLACK)

        main_surface.blit(score_board, score_board_rect)

        solo_sprite.draw(main_surface)

        paddle2.move()
        ball.move()
        ball.change_direction()

        solo_hit()
        paddle_hit()


        if ball.rect.x > WINDOW_WIDTH:
            bot_score += 1

        elif ball.rect.y < square_y + square_height:
            if ball.rect.x > square_x and ball.rect.x < square_x + square_width or ball.rect.x  > square_x and ball.rect.x < square_x + square_width:
                square_y = random.randrange(0, WINDOW_HEIGHT)
                player1_score += 1
                ball.speed = 6
                ball.rect.centerx = surface_rect.centerx
                ball.rect.centery = surface_rect.centery
                ball.direction = randint(2, 3)
                continue



        if counter == 0:
            time.sleep(1.5)


        elif player1_score == 5:
            player1_win = True
            gamedone()

        elif bot_score == 5:
            bot_win = True
            gamedone()


        counter += 1

        square(0,square_y,square_width,square_height, GREEN)

        pygame.display.update()

def game_multi():
    player1_score = 0
    player2_score = 0
    global UP1
    global DOWN1
    global NO_MOVEMENT1
    global UP2
    global DOWN2
    global NO_MOVEMENT2
    global player1_win
    global player2_win
    global gamestat
    global counter
    global game_over
    global game_over1
    ball.rect.centerx = surface_rect.centerx
    ball.rect.centery = surface_rect.centery
    while True:

        clock.tick(60)


        if (ball.rect.x > WINDOW_WIDTH):
            ball.rect.centerx = surface_rect.centerx
            ball.rect.centery = surface_rect.centery
            ball.direction = randint(0, 1)
            ball.speed = 4
        elif (ball.rect.x < 0):
            ball.rect.centerx = surface_rect.centerx
            ball.rect.centery = surface_rect.centery
            ball.direction = randint(2, 3)
            ball.speed = 4

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                elif event.key == ord('a'):
                    UP1 = True
                    DOWN1 = False
                    NO_MOVEMENT1 = False
                elif event.key == ord('z'):
                    UP1 = False
                    DOWN1 = True
                    NO_MOVEMENT1 = False

                elif event.key == K_UP:
                    UP2 = True
                    DOWN2 = False
                    NO_MOVEMENT2 = False
                elif event.key == K_DOWN:
                    UP2 = False
                    DOWN2 = True
                    NO_MOVEMENT2 = False

                elif event.key == ord('p'):
                    multiplayer()


            elif event.type == KEYUP:
                if event.key == ord('a') or event.key == ord('z'):
                    NO_MOVEMENT1 = True
                    DOWN1 = False
                    UP1 = False
                elif event.key == K_DOWN or event.key == K_UP:
                    NO_MOVEMENT2 = True
                    DOWN2 = False
                    UP2 = False


        score_board = basic_font.render(str(player1_score) + "           " + str(player2_score), True, WHITE, BLACK)
        score_board_rect = score_board.get_rect()
        score_board_rect.centerx = surface_rect.centerx
        score_board_rect.y = 10

        main_surface.fill(BLACK)

        main_surface.blit(score_board, score_board_rect)

        all_sprites.draw(main_surface)


        paddle1.move()
        paddle2.move()
        ball.move()
        ball.change_direction()

        paddle_hit()

        if ball.rect.x > WINDOW_WIDTH:
            player1_score += 1
        elif ball.rect.x < 0:
            player2_score += 1



        if counter == 0:
            time.sleep(1.5)


        elif player1_score == 5:
            player1_win = True
            gamedone()




        elif player2_score == 5:
            player2_win = True
            gamedone()


        counter += 1

        pygame.display.update()


def gamedone():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE:
                    main_surface.fill(BLACK)
                    game()

        main_surface.fill(BLACK)

        if player1_win == True:
            game_over = game_over_font_small.render("Press SPACE to go the Menu and ESC to Exit", True, WHITE, BLACK)
            game_over1 = game_over_font_small.render("Player 1 Wins", True, WHITE, BLACK)


        elif player2_win == True:
            game_over = game_over_font_small.render("Press SPACE to go the Menu and ESC to Exit", True, WHITE, BLACK)
            game_over1 = game_over_font_small.render("Player 2 Wins", True, WHITE, BLACK)

        elif bot_win == True:
            game_over = game_over_font_small.render("Press SPACE to go the Menu and ESC to Exit", True, WHITE, BLACK)
            game_over1 = game_over_font_small.render("YOU LOSE", True, WHITE, BLACK)


        game_over_rect = game_over.get_rect()
        game_over_rect.centerx = surface_rect.centerx
        game_over_rect.centery = surface_rect.centery - 50
        game_over1_rect = game_over1.get_rect()
        game_over1_rect.centerx = game_over_rect.centerx
        game_over1_rect.centery = game_over_rect.centery + 75

        main_surface.blit(game_over, game_over_rect)
        main_surface.blit(game_over1, game_over1_rect)

        pygame.display.update()

def game():
    multiplayer()


game()