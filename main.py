import pygame
from pygame.locals import *
import tkinter
from tkinter import *


menu = tkinter.Tk()
menu.title("INSTRUCTIONS")
menu.geometry("470x279")
menu.resizable(0,0)
bg = PhotoImage(file = "wone.png")
bg2 = PhotoImage(file = "2.png")

def wid():
    def delete():
        btnAls.destroy()
        label1.destroy()
        wid2()

    label1 = Label(menu, image=bg)
    label1.place(x=-2, y=1)
    btnAls = Button(menu, text="CONTINUE", height=2, width=13, font=('Helvetica 20 bold'), command = delete)
    btnAls.place(x=120, y=90)
    def on_enter(e):
       btnAls.config(background= "#fdbcb4", foreground= "#170055")
    def on_leave(e):
       btnAls.config(background= 'SystemButtonFace', foreground= 'black')
    btnAls.bind('<Enter>', on_enter)
    btnAls.bind('<Leave>', on_leave)

def wid2():

    lable2 = Label(menu, image=bg2)
    lable2.place(x=-10, y=0)

wid()
menu.mainloop()

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.7)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('"Hackin Ka, SaYo Ako"')


SCREEN2_WIDTH = 800
SCREEN2_HEIGHT = int(SCREEN_WIDTH * 0.7)
screen2 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("monospace", 18)
font2 = pygame.font.SysFont("monospace", 25)

textX= 400
textY=150

def show_text1(x,y):
    textA = font.render("We're talking for a long time na", True, (255, 255, 255))
    screen.blit(textA, (100, 50))
    textB = font.render("At naiinip na ako malaman", True, (255, 255, 255))
    screen.blit(textB, (100, 100))
    textC = font.render("Kung gusto mo rin ako", True, (255, 255, 255))
    screen.blit(textC, (100, 150))
    textD = font.render("That's why naglakas loob na ako ngayon :) ", True, (255, 255, 255))
    screen.blit(textD, (100, 200))
    textE = font.render("LONG PRESS 'L'", True, (255, 255, 255))
    screen.blit(textE, (100, 250))

def show_text2(x,y):
    textA = font.render("Idk if you'll find this weird", True, (255, 255, 255))
    screen.blit(textA, (100, 50))
    textB = font.render("Kasi ang random ng amin ko hahahha", True, (255, 255, 255))
    screen.blit(textB, (100, 100))
    textC = font.render("GUSTO KITA, MR. CHINITO!!", True, (255, 255, 255))
    screen.blit(textC, (100,150))
    textD = font.render("Sana gusto mo rin ako", True, (255, 255, 255))
    screen.blit(textD, (100, 200))
    textE = font.render("If hindi, please pilitin mo :(( HHAHAH jk", True, (255, 255, 255))
    screen.blit(textE, (100, 250))
    textF = font.render("LONG PRESS 'Y'", True, (255, 255, 255))
    screen.blit(textF, (100, 300))

def show_text3(x,y):
    textG = font.render("Now, move closer to the girl", True, (255, 255, 255))
    screen.blit(textG, (100, 50))
    textH = font.render("Do you accept my love for you?", True, (255, 255, 255))
    screen.blit(textH, (100, 100))
    textI = font.render("Press 'space bar' if Yes", True, (255, 255, 255))
    screen.blit(textI, (100,150))
    textJ = font.render("Press 'F1' key if No", True, (255, 255, 255))
    screen.blit(textJ, (100, 200))

def show_text4(x,y):
    textK = font2.render("INDEED, HAPPY VALENTINES!! ", True, (255, 255, 255))
    screen.blit(textK, (50, 100))

def show_text5(x,y):
    textK = font2.render("IT'S OKAY :)!! ", True, (255, 255, 255))
    screen.blit(textK, (50, 100))



def show_text(x,y):
    text = font.render("Hi, Mr. Chinito :))", True, (255,255,255))
    screen.blit(text,(100, 50 ))
    text2 = font.render("I know you have no idea about this", True, (255, 255, 255))
    screen.blit(text2, (100, 100))
    text3 = font.render("But I just want you to know that I admire you", True, (255, 255, 255))
    screen.blit(text3, (100, 150))
    text3 = font.render("HAHHAHAHHAHAHA shems ", True, (255, 255, 255))
    screen.blit(text3, (100, 200))
    text4 = font.render("LONG PRESS 'i'", True, (255, 255, 255))
    screen.blit(text4, (100, 250))


#define fps
clock = pygame.time.Clock()
fps = 60

background_image = pygame.image.load("paris.jpg").convert()

#load button images
start_img = pygame.image.load('start_btn.png')



#load image
bg = ("black")

def draw_bg():
    screen.fill(bg)

#create spaceship class
class You(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('p1.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_shot = pygame.time.get_ticks()


    def update(self):
        #set movement speed
        speed = 8
        #set a cooldown variable
        cooldown = 500 #milliseconds


        #get key press
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= speed
        if key[pygame.K_RIGHT]:
            self.rect.x += speed
        if key[pygame.K_DOWN]:
            self.rect.y += speed
        if key[pygame.K_UP]:
            self.rect.y -= speed
        if key[pygame.K_m]:
            #self.rect.y -= speed
            show_text(textX, textY)
        if key[pygame.K_i]:
            #self.rect.y -= speed
            show_text1(textX, textY)
        if key[pygame.K_l]:
            #self.rect.y -= speed
            show_text2(textX, textY)
        if key[pygame.K_l]:
            #self.rect.y -= speed
            show_text2(textX, textY)
        if key[pygame.K_y]:
            #self.rect.y -= speed
            show_text3(textX, textY)
        if key[pygame.K_h]:
            #self.rect.y -= speed
            show_text4(textX, textY)
        if key[pygame.K_j]:
            #self.rect.y -= speed
            show_text5(textX, textY)




        #record current time
        time_now = pygame.time.get_ticks()
        #shoot
        if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.last_shot = time_now



        if key[pygame.K_F1] and time_now - self.last_shot > cooldown:
            broken = Broken(self.rect.centerx, self.rect.top)
            broken_group.add(broken)
            self.last_shot = time_now


class Me(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('p2.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



#create Bullets class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("bh.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


    def update(self):
        self.rect.x += 5
       # if self.rect.bottom < 0:
         #   self.kill()

class Broken(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("broken.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


    def update(self):
        self.rect.x += 5
       # if self.rect.bottom < 0:
         #   self.kill()


#create sprite groups
you_group = pygame.sprite.Group()
me_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
broken_group = pygame.sprite.Group()


#create player
you = You(100,360, .4)
you_group.add(you)
me = Me(600,330,.15)
me_group.add(me)



run = True
while run:

    clock.tick(fps)
    #draw background
    draw_bg()
    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background_image, [0, 0])
    #update you
    you.update()
    me.update()

    #update sprite groups
    bullet_group.update()
    broken_group.update()

    #draw sprite groups
    you_group.draw(screen)
    me_group.draw(screen)
    bullet_group.draw(screen)
    broken_group.draw(screen)


    pygame.display.update()


pygame.quit()
