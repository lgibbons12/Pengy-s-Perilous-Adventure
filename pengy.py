import pygame
import pickle
import time
from pygame import mixer
from os import path

screen_width = 500
screen_height = 500

red = (255, 0, 0)
green = (72,61,139)
blue = (0, 0, 255)
brown = (139,69,19)
yellow =(255, 255, 0)

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#define font

font_score = pygame.font.SysFont("Bauhaus 93", 30)
font = pygame.font.SysFont("Bauhaus 93", 70)
small_font = pygame.font.SysFont("Bauhaus 93", 20)


#game variables

tile_size = 25

game_over = 0

# 0 is main menu, 1 is in the game, 2 is gg room
game_state = 0


best_time = "37.437"
max_levels = 7

level = 1

score = 0

high_score = "-6"

your_score = 0

lives = 10

passed_time = 0
timer_startd = False
done = False

super_boost_a = True

super_boost_d = True

level_score = 0

#define colors
black = (0, 0, 0)



clock = pygame.time.Clock()
start = 0
fps = 60





#image loading

bg_img = pygame.image.load("C:/Users/liamw/Documents/Resources/bg.jpg")
bg_img = pygame.transform.scale(bg_img,(1000,500))

restart_img = pygame.image.load("C:/Users/liamw/Documents/Resources/restart.png")
restart_img = pygame.transform.scale(restart_img, (150, 50))

start_img = pygame.image.load("C:/Users/liamw/Documents/Resources/start.png")
start_img = pygame.transform.scale(start_img, (210, 110))

exit_img = pygame.image.load("C:/Users/liamw/Documents/Resources/exit.png")
exit_img = pygame.transform.scale(exit_img, (200, 100))

intro_img = pygame.image.load("C:/Users/liamw/Documents/Resources/intro.png")
intro_img = pygame.transform.scale(intro_img, (400, 200))

endscreen_img = pygame.image.load("C:/Users/liamw/Documents/Resources/endscreen.png")
endscreen_img = pygame.transform.scale(endscreen_img, (400, 200))

fish_img = pygame.image.load("C:/Users/liamw/Documents/Resources/fish.png")
fish_img = pygame.transform.scale(fish_img, (200, 100))

pengy_img = pygame.image.load("C:/Users/liamw/Documents/Resources/happypengy.png")
pengy_img = pygame.transform.scale(pengy_img, (300, 300))

lives_img = pygame.image.load("C:/Users/liamw/Documents/Resources/happypengy.png")
lives_img = pygame.transform.scale(lives_img, (25, 25))

shrimp_img = pygame.image.load("C:/Users/liamw/Documents/Resources/shrimp.png")
shrimp_img = pygame.transform.scale(shrimp_img, (20, 20))

check_img = pygame.image.load("C:/Users/liamw/Documents/Resources/check.png")
check_img = pygame.transform.scale(check_img, (20, 20))

open_img = pygame.image.load("C:/Users/liamw/Documents/Resources/shrimp.png")
open_img = pygame.transform.scale(open_img, (20, 20))



#finishing image loading


#load sounds

crunch_fx = pygame.mixer.Sound("C:/Users/liamw/Documents/Resources/crunch.mp3")
crunch_fx.set_volume(0.5)

jump_fx = pygame.mixer.Sound("C:/Users/liamw/Documents/Resources/img_jump.wav")
jump_fx.set_volume(0.5)

gameover_fx = pygame.mixer.Sound("C:/Users/liamw/Documents/Resources/img_game_over.wav")
gameover_fx.set_volume(0.5)

door_fx = pygame.mixer.Sound("C:/Users/liamw/Documents/Resources/dooropen.mp3")
door_fx.set_volume(0.5)

win_fx = pygame.mixer.Sound("C:/Users/liamw/Documents/Resources/win.wav")
win_fx.set_volume(0.25)

pygame.mixer.music.load("C:/Users/liamw/Documents/Resources/music.wav")
pygame.mixer.music.play()








#grid and world data

def draw_grid():
        for line in range(0, 20):
                pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
                pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))





def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))


        

#function to reset level

def reset_level(level):
        player.reset(50, screen_height - 65)
        yeti_group.empty()
        platform_group.empty()
        shrimp_group.empty()
        icicle_group.empty()
        exit_group.empty()
        if path.exists(f'C:/Users/liamw/Documents/Resources/level{level}_data'):
                pickle_in = open(f'C:/Users/liamw/Documents/Resources/level{level}_data', 'rb')
                world_data = pickle.load(pickle_in)

        world = World(world_data)

        return world
        
        
        

class Button():
        def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.clicked = False
        def draw(self):

                action = False

                #get mouse position

                pos = pygame.mouse.get_pos()

                #check mouseover and click conditions

                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] and self.clicked == False:
                                self.clicked = True
                                action = True
                                

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False
                
                                
                                
                screen.blit(self.image, self.rect)

                return action

class Player():

    
    def __init__ (self, x, y):
        self.reset(x, y)
        



    def update(self, game_over):

        dx = 0
        dy = 0
        col_thresh = 20
        walk_cooldown = 10

        if game_over == 0:
                
                
        
                #get keypresses
                key = pygame.key.get_pressed()
                super_boost_d = True
                super_boost_a = True


                if key[pygame.K_SPACE] and self.jumped == False:
                    jump_fx.play()
                    self.vel_y = -8
                    self.jumped = True
                    #print("Jump")

                if key[pygame.K_UP] and self.jumped == False:
                    jump_fx.play()
                    self.vel_y = -8
                    self.jumped = True
                    #print("Jump")

                if key[pygame.K_w] and self.jumped == False:
                    jump_fx.play()
                    self.vel_y = -8
                    self.jumped = True
                    #print("Jump")
                    



                if key[pygame.K_d] and key[pygame.K_LSHIFT]:
                    dx += 1.5
                    self.counter += 1
                    self.direction = 1
                    #print("Right Sprint")

                if key[pygame.K_RIGHT] and key[pygame.K_LSHIFT]:
                    dx += 1.5
                    self.counter += 1
                    self.direction = 1
                    #print("Right Sprint")

                if key[pygame.K_d]:
                    dx += 2.5
                    self.counter += 1
                    self.direction = 1
                    #print("Right")

                if key[pygame.K_RIGHT]:
                    dx += 2.5
                    self.counter += 1
                    self.direction = 1
                    #print("Right")

                if key[pygame.K_s] and key[pygame.K_d] and super_boost_d == False:
                    dx += 45
                    super_boost_d = False

                if key[pygame.K_s] and key[pygame.K_a] and super_boost_a == False:
                    dx -= 45
                    super_boost_a = False
                
                    

                if key[pygame.K_a] and key[pygame.K_LSHIFT]:
                    dx -= 1.5
                    self.counter += 1
                    self.direction = -1
                    #print("Left Sprint")

                if key[pygame.K_LEFT] and key[pygame.K_LSHIFT]:
                    dx -= 1.5
                    self.counter += 1
                    self.direction = -1
                    #print("Left Sprint")
                if key[pygame.K_a]:
                    dx -= 2.5
                    self.counter += 1
                    self.direction = -1
                    #print("Left")

                if key[pygame.K_LEFT]:
                    dx -= 2.5
                    self.counter += 1
                    self.direction = -1
                    #print("Left")

                if key[pygame.K_a] == False and key[pygame.K_d] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]

                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]

                    if self.direction == -1:
                        self.image = self.images_left[self.index]
                

                        


                #handle animation

                
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                                         
                    if self.direction == 1:
                        self.image = self.images_right[self.index]

                    if self.direction == -1:
                        self.image = self.images_left[self.index]
                
                    


                #add gravity

                self.vel_y += 0.5
                if self.vel_y > 10:
                    self.vel_y = 10
                dy += self.vel_y
                
                #check for collision

                for tile in world.tile_list:

                    #check for collision in x direction

                    if tile [1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0

                    
                    
                    
                    #check for collision in y direction
                    
                    if tile [1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

                        #check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = +5

                        #checking if above the ground i.e. falling

                        elif self.vel_y > 0:
                            dy = tile[1].top - self.rect.bottom
                            self.jumped = False

                #check for collision with enemies
                if pygame.sprite.spritecollide(self, yeti_group, False):
                    game_over = -1
                    gameover_fx.play()
                

                #check for collision with platforms

                for platform in platform_group:
                    #collision in x direction
                    if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                        dx = 0

                    #collision in y direction
                    if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                        #check if below platform
                        if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                            self.vel_y = 0
                            dy = platform.rect.bottom - self.rect.top
                        #check if above platform
                        elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                            self.vel_y = 0
                            dy = platform.rect.top - self.rect.bottom - 1
                            self.jumped = False
                        #move sideways with platform
                        if platform.move_x != 0:
                            self.rect.x += platform.move_direction


                
                    


                #check for collision with icicle
                if pygame.sprite.spritecollide(self, icicle_group, False):
                    game_over = -1
                    gameover_fx.play()



                #check for collision with exit door

                if pygame.sprite.spritecollide(self, exit_group, False):
                    game_over = 1
                    door_fx.play()
                    

                    



                #update player position

                self.rect.x += dx
                self.rect.y += dy

                
        elif game_over == -1:
                self.image = self.dead_image
                
                draw_text("You Died!", font, blue, 100, 100)
                if self.rect.y > 200:
                        self.rect.y -= 2

        #draw player on screen
        screen.blit(self.image, self.rect)

        return game_over
    def reset(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                    img_right = pygame.image.load(f"C:/Users/liamw/Documents/Resources/pengy{num}.png")
                    img_right = pygame.transform.scale(img_right, (20, 40))
                    img_left = pygame.transform.flip(img_right, True, False)
                    self.images_right.append(img_right)
                    self.images_left.append(img_left)

            self.dead_image = pygame.image.load(f"C:/Users/liamw/Documents/Resources/ghostpengy.png")
            self.dead_image = pygame.transform.scale(self.dead_image, (20, 40))

            self.image = self.images_right[self.index]

                    
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0




        
class World():
    def __init__(self, data):
        self.tile_list = []

        #load image
        grass_img = pygame.image.load("C:/Users/liamw/Documents/Resources/dirt.png")
        dirt_img = pygame.image.load("C:/Users/liamw/Documents/Resources/realdirt.png")
        trophy_img = pygame.image.load("C:/Users/liamw/Documents/Resources/trophy.jpg")

        row_count = 0
        for row in data :
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size)) 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size)) 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3:
                    yeti = Enemy(col_count * tile_size, row_count * tile_size + 12)
                    yeti_group.add(yeti)

                if tile == 4:
                    #horizontal
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                    platform_group.add(platform)

                if tile == 5:
                    #vertical
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                    platform_group.add(platform)

                if tile == 6:
                    icicle = Icicle(col_count * tile_size, row_count * tile_size)
                    icicle_group.add(icicle)

                if tile == 7:
                    shrimp = Shrimp(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                    shrimp_group.add(shrimp)

                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                    
                    
                    
                    
                

                        
                        
                    

                if tile == 29:
                    img = pygame.transform.scale(trophy_img, (tile_size, tile_size)) 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                    
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("C:/Users/liamw/Documents/Resources/yeti1.png")
                meme = 3 / 2
                self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                

        def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if abs(self.move_counter) > 25:
                        self.move_direction *= -1
                        self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
        def __init__(self, x, y, move_x, move_y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("C:/Users/liamw/Documents/Resources/platform.jpg")
                self.image = pygame.transform.scale(self.image, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                self.move_x = move_x
                self.move_y = move_y

        def update(self):
                self.rect.x += self.move_direction * self.move_x
                self.rect.y += self.move_direction * self.move_y 
                self.move_counter += 1
                if abs(self.move_counter) > 25:
                        self.move_direction *= -1
                        self.move_counter *= -1
                

class Icicle(pygame.sprite.Sprite):
        def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("C:/Users/liamw/Documents/Resources/icicle.png")
                self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


class Shrimp(pygame.sprite.Sprite):
        def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("C:/Users/liamw/Documents/Resources/shrimp.png")
                self.image = pygame.transform.scale(self.image, (int(tile_size // 1.5), int(tile_size // 1.5)))
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)
               


class Exit(pygame.sprite.Sprite):
        def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load("C:/Users/liamw/Documents/Resources/door.png")
                self.image = pygame.transform.scale(self.image, (tile_size, int(tile_size * 1.5)))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


                
                




#entity groups

player = Player(50, screen_height - 65)

yeti_group = pygame.sprite.Group()

platform_group = pygame.sprite.Group()

icicle_group = pygame.sprite.Group()

exit_group = pygame.sprite.Group()

shrimp_group = pygame.sprite.Group()




#load in level data and create world

if path.exists(f'C:/Users/liamw/Documents/Resources/level{level}_data'):
        pickle_in = open(f'C:/Users/liamw/Documents/Resources/level{level}_data', 'rb')
world_data = pickle.load(pickle_in)

world = World(world_data)

#create buttons

restart_button = Button(175, 175, restart_img)

start_button = Button(25, 220, start_img)

exit_button = Button(250, 225, exit_img)

exit_endbutton = Button (150, 200, exit_img)

intro_button = Button(50, 10, intro_img)

endscreen_button = Button(50, 10, endscreen_img)

pengy_button = Button(25, 195, pengy_img)

fish_button = Button(250, 300, fish_img)

shrimp_pic = Button(25, 30, shrimp_img)

tenlives_pic = Button(125, 75, lives_img)

ninelives_pic = Button(100, 75, lives_img)

eightlives_pic = Button(75, 75, lives_img)

sevenlives_pic = Button(50, 75, lives_img)

sixlives_pic = Button(25, 75, lives_img)

fivelives_pic = Button(125, 50, lives_img)

fourlives_pic = Button(100, 50, lives_img)

threelives_pic = Button(75, 50, lives_img)

twolives_pic = Button(50, 50, lives_img)

onelife_pic = Button(25, 50, lives_img)

check_button = Button (25, 25, check_img)

open_button = Button(25, 25, open_img)
             

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pengy's Perilous Adventure")

running = True

while running:
        
    
    clock.tick(fps)
    screen.blit(bg_img, (0, 0))
    

    
    

    if game_state == 0:
            
            if exit_button.draw():
                    running = False
            if start_button.draw():
                    game_state = 1
                    
            intro_button.draw()
            draw_text("Best Time: " + best_time, font_score, black, 0, 0)
            draw_text("Lowest Score: " + high_score, font_score, black, 275, 0)
            
            draw_text("Controls:", small_font, black, 0, 315)
            draw_text("WAD, Arrow Keys, or Space", small_font, black, 0, 365)
            draw_text("Shift to Sprint, Click to restart", small_font, black, 0, 415)
            draw_text("You Have 10 Lifes to Make it Through", small_font, black, 0, 465)


    elif game_state == 1:
            
            ticks = pygame.time.get_ticks()
            millis = ticks%1000
            seconds = int(ticks/1000 % 60)
            minutes = int(ticks/60000 % 24)
            draw_text(str(minutes) + ":" + str(seconds) + "." + str(millis), font_score, black, 175, 25)
            
            draw_text("Level " + str(level), font_score, black, 355, 25)
            if lives == 0:
                    game_state = 3
            if lives == 10:
                    tenlives_pic.draw()
                    ninelives_pic.draw()
                    eightlives_pic.draw()
                    sevenlives_pic.draw()
                    sixlives_pic.draw()
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 9:
                    ninelives_pic.draw()
                    eightlives_pic.draw()
                    sevenlives_pic.draw()
                    sixlives_pic.draw()
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 8:
                    eightlives_pic.draw()
                    sevenlives_pic.draw()
                    sixlives_pic.draw()
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 7:
                    sevenlives_pic.draw()
                    sixlives_pic.draw()
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 6:
                    sixlives_pic.draw()
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 5:
                    fivelives_pic.draw()
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 4:
                    fourlives_pic.draw()
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 3:
                    threelives_pic.draw()
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 2:
                    twolives_pic.draw()
                    onelife_pic.draw()
            if lives == 1:
                    onelife_pic.draw()
            

    

            world.draw()
            shrimp_pic.draw()
            draw_text("x " + str(score + level_score), font_score, black, 50, 25)

            if game_over == 0:
                    
            
            

                    yeti_group.update()
                    platform_group.update()
                    
                    #update score
                    if pygame.sprite.spritecollide(player, shrimp_group, True):
                            level_score += 1
                            crunch_fx.play()

                    
                    
                    
                            
                            
            key = pygame.key.get_pressed()       
            if key[pygame.K_r]:
                    
                    
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    level_score = 0      

            yeti_group.draw(screen)

            platform_group.draw(screen)

            icicle_group.draw(screen)

            shrimp_group.draw(screen)

            exit_group.draw(screen)

            game_over = player.update(game_over)

            #if I died

            if game_over == -1:
                    
                    if lives > 0:
                            key = pygame.key.get_pressed()
                            
                            if restart_button.draw():
                                    lives -= 1
                                    world_data = []
                                    world = reset_level(level)
                                    game_over = 0
                                    level_score = 0
                                    

            #if I completed the level
            if game_over == 1:
                    level += 1
                    if level <= max_levels:
                            #reset level
                            world_data = []
                            world = reset_level(level)
                            game_over = 0
                            score += level_score
                            level_score = 0
                            
                    else:
                            game_state = 2
                            score += level_score
                            pygame.mixer.music.stop()
                            win_fx.play()
     
                            
                    
    elif game_state == 2:
            endscreen_button.draw()
            your_score = (minutes * 60 + seconds) - (score) - (lives * 2)
            draw_text("Stats: ", font_score, black, 300, 360)
            draw_text("Time: " + str(minutes) + ":" + str(seconds) + "." + str(millis), font_score, black, 300, 390)
            draw_text("Lives: " + str(lives), font_score, black, 300, 420)
            draw_text("Shrimp: " + str(score), font_score, black, 300, 450)
            draw_text("Score = " + str(your_score), font_score, black, 300, 470)
            print(your_score)
            fish_button.draw()
            pengy_button.draw()
            if exit_button.draw():
                    running = False
    else:
            draw_text("Game Over, Try Again Next Time", font_score, red, 40, 100)
            if exit_endbutton.draw():
                    running = False
                    
            

    

    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False

    

        

    pygame.display.update()


pygame.quit()
