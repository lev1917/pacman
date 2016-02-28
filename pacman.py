from decimal import Decimal, getcontext
import math
import sys
import pygame
from pygame.locals import *
from math import floor
import random
getcontext().prec=1

class Map():
    def __init__(self, x):
                self.map = [[0]*x for i in range(x)]
                for i in range(x):
                    for y in range(x):
                        self.map[i][y]=[]




    def get(self, x, y):
                return self.map[x][y]
    def moveTo(self, obj, new_x, new_y,):
            point = self.map[int(obj.Mx)][int(obj.My)]
            if obj in point:
              point.remove(obj)
              self.map[new_x][new_y].append(obj)

    def put(self, x,y,obi):

        self.map[x][y].append(obi)
    def remuwal(self,obj):
        self.map[obj.Mx][obj.My].remove(obj)





def init_window():
    pygame.init()
    pygame.display.set_mode((512, 512))
    pygame.display.set_caption('Packman')


def draw_background(scr, img=None):
    """
    :rtype : object
    """
    if img:
        scr.blit(img, (0, 0))
    else:
        bg = pygame.Surface(scr.get_size())
        bg.fill((0, 0, 0))
        scr.blit(bg, (0, 0))


class GameObject(pygame.sprite.Sprite):
    def __init__(self, img, x, y, tile_size, map_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.screen_rect = None
        self.x = 0
        self.y = 0
        self.tick = 0
        self.tile_size = tile_size
        self.map_size = map_size
        self.set_coord(x, y)

    def set_coord(self, x, y):
        self.x = x
        self.y = y
        self.screen_rect = Rect(floor(x) * self.tile_size, floor(y) * self.tile_size, self.tile_size, self.tile_size )

    def game_tick(self):
        self.tick += 1

    def draw(self, scr):
        scr.blit(self.image, (self.screen_rect.x, self.screen_rect.y))

class Point(GameObject):
    def __init__(self,x,y,title_size,map_size):
        GameObject.__init__(self,'C:/Users/Home/PycharmProjects/pacman/point.ico',x,y,tile_size,map_size)
        self.live=1
        self.Mx=int(x)
        self.My=int(y)
class Ghost(GameObject):
    def __init__(self, x, y, tile_size, map_size):
        GameObject.__init__(self, 'C:/Users/Home/PycharmProjects/pacman/ghost.png', x, y, tile_size, map_size)
        self.direction = 0
        self.velocity = 0.4
        self.pu=2
        self.Mx=int(self.x)
        self.My=int(self.y)

    def g(self):
        self.Mx=int(self.x)
        self.My=int(self.y)
    def game_tick(self):
        t=1
        super(Ghost, self).game_tick()
        if int(self.x)==int(pacman.x):
            t=0
            if (int(self.y)-int(pacman.y))>0:
                self.direction=4
            else:
                self.direction=2
        if int(self.y)==int(pacman.y):
            t=0
            if (int(self.x)-int(pacman.x))>0:
                self.direction=3
            else:
                self.direction=1


        if t:
            if self.tick % 5 == 0 or self.direction == 0:
               self.direction=random.randint(1,4)



        if self.direction == 1:
            u=1

            xk=self.x+self.velocity
            if self.Mx<map_size-1:

                ma=Map0.get(self.Mx+1,self.My)
                if ma:
                    for el in ma:
                        if isinstance(el,Pacman):

                            el.life-=1
                            self.x=xk
                            self.g()
                if u:

                   Map0.moveTo(self,int(xk),self.My)
                   self.x=xk

                   self.g()




            else:
                self.x=map_size-1
                self.g()

        elif self.direction == 2:

            u=1
            yk=self.y+self.velocity


            if int(self.y)<15:
                ma=Map0.get(self.Mx,self.My+1)
                if ma:
                    for el in ma:
                        if isinstance(el,Pacman):

                            el.life=-1
                            self.y=yk
                            self.g()
                            u=1
                if u:
                   Map0.moveTo(self,self.Mx,int(yk))
                   self.y=yk
                   self.g()
            else:
                self.y=map_size-1

                self.g()

        elif self.direction == 3:
            u=1
            xk=self.x-self.velocity
            if int(self.Mx)>0:
                ma=Map0.get(self.Mx-1,self.My)
                if ma:
                    for el in ma:
                        if isinstance(el,Pacman):

                            el.life-=1
                            self.x=xk

                            self.g()

                if u:
                    Map0.moveTo(self,int(xk),self.My)
                    self.x=xk
                    self.g()



            else:
                self.x=0

                self.g()

        elif self.direction == 4:


            yk=self.y-self.velocity


            if int(self.y)>0:
                u=1
                ma=Map0.get(self.Mx,self.My-1)
                if ma:
                    for el in ma:
                        if isinstance(el,Pacman):

                            el.life-=1
                            self.y=yk
                            self.g()

                if u:


                     Map0.moveTo(self,self.Mx,int(yk))
                     self.y=yk

                     self.g()






            else:
                self.y=0

                self.g()

        self.set_coord(self.x, self.y)
class Pacman(GameObject):
    def __init__(self, x, y, tile_size, map_size):
        GameObject.__init__(self, 'C:/Users/Home/PycharmProjects/pacman/pacman.png', x, y, tile_size, map_size)
        self.direction = 0
        self.velocity = 0.4
        self.life=2
        self.point=0

        self.Mx=int(self.x)
        self.My=int(self.y)


    def g(self):
        self.Mx=int(self.x)
        self.My=int(self.y)
    def game_tick(self):
        super(Pacman, self).game_tick()
        if self.direction==1:
            self.image=pygame.image.load('C:/Users/Home/PycharmProjects/pacman/pacman.png')
            u=1
            xk=self.x+self.velocity
            if self.Mx<map_size-1:
                ma=Map0.get(self.Mx+1,self.My)

                if ma:
                    for el in ma:
                        if isinstance(el,Ghost):
                            el.direction=0
                            pacman.life-=1
                            self.x=xk
                            self.g()
                        if isinstance(el, Wall):


                                self.direction=0

                                self.g()
                                u=0
                        if isinstance(el,Point):
                            self.point+=1
                            el.live-=1
                            Map0.remuwal(el)

                if u:
                    Map0.moveTo(pacman,int(xk),self.My)

                    self.x=xk

                    self.g()



            else:
                self.x=15

                self.g()
        elif self.direction == 2:
            self.image=pygame.image.load('C:/Users/Home/PycharmProjects/pacman/pacman_2.png')
            yk=self.y+self.velocity


            if self.My<map_size-1:
                u=1
                ma=Map0.get(self.Mx,self.My+1)
                print(ma)
                if ma:
                    for el in ma:
                        if isinstance(el,Ghost):
                            el.direction=0
                            pacman.life-=1
                            self.y=yk
                            u=0
                        if isinstance(el, Wall):

                           self.direction=0
                           u=0
                        if isinstance(el,Point):
                            self.point+=1
                            el.live-=1
                            Map0.remuwal(el)

                if u:

                    Map0.moveTo(pacman,self.Mx,int(yk))
                    self.y=yk

                    self.g()


            else:
                self.y=15
        elif self.direction == 3:
            self.image=pygame.image.load('C:/Users/Home/PycharmProjects/pacman/pacman_3.png')
            xk=self.x-self.velocity
            if self.Mx>0:
                u=1
                ma=Map0.get(self.Mx-1,self.My)
                print(ma)
                if ma:
                    for el in ma:
                        if isinstance(el,Ghost):
                            el.direction=0
                            pacman.life=0
                            self.x=xk
                            u=0
                        if isinstance(el, Wall):

                                self.direction=0
                                u=0
                                self.g()
                        if isinstance(el,Point):
                            self.point+=1
                            el.live-=1
                            Map0.remuwal(el)
                if u:
                    Map0.moveTo(pacman,int(xk),self.My)
                    self.x=xk

                    self.g()


            elif xk>0:
                 self.x=xk

                 self.g()
            else:
                self.x=0

                self.g()

        elif self.direction == 4:
            self.image=pygame.image.load('C:/Users/Home/PycharmProjects/pacman/pacman_4.png')
            yk=self.y-self.velocity
            u=1

            if self.My>0:
                u=1
                ma=Map0.get(self.Mx,self.My-1)
                if ma:
                    for el in ma:
                        if isinstance(el,Ghost):
                            el.direction=0
                            pacman.life=0
                            self.y=yk
                            u=0
                        if isinstance(el, Wall):

                                self.direction=0
                                u=0
                                self.g()
                        if isinstance(el,Point):
                            self.point+=1
                            el.live-=1
                            Map0.remuwal(el)
                if u:
                    Map0.moveTo(pacman,self.Mx,int(yk))

                    self.y=yk

                    self.g()



            else:
                self.y=0


        self.set_coord(self.x, self.y)






class Wall(GameObject):
    def __init__(self,x,y, tile_size, map_size):
        GameObject.__init__(self, 'C:/Users/Home/PycharmProjects/pacman/wall.png', x, y, tile_size, map_size)


def process_events(events, packman):
    for event in events:
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                packman.direction = 3
            elif event.key == K_RIGHT:
                packman.direction = 1
            elif event.key == K_UP:
                packman.direction = 4
            elif event.key == K_DOWN:
                packman.direction = 2
            elif event.key == K_SPACE:
                packman.direction = 0
if __name__ == '__main__':

    MAp = open('C:/Users/Home/PycharmProjects/pacman/MAP.txt', 'r')
    MAP=[]
    p=1
    GHs=[]
    while p:
      p= MAp.readline()
      if p:
       for i in range(16):
           t=p[i]
           print(t)
           MAP.append(t)
    init_window()
    tile_size = 32
    map_size = 16
    Map0=Map(map_size)
    background = pygame.image.load("C:/Users/Home/PycharmProjects/pacman/background.png")
    screen = pygame.display.get_surface()
    Walls=[]
    POint=[]
    print(MAP)
    g=1
    for i in range(len(MAP)):

       if MAP[i] == '@':
          h=0
          if i/16==16 :
            h=-1
          x=i-16*(i//16)
          y=i//16+h
          pacman=Pacman(x,y,32,16)
          print(pacman)
          Map0.put(x,y,pacman)
          Pa=(i-16*(i//16),i//16+h,)
          print(i)
          h=0
       if MAP[i] == '&':
         h=0
         if i/16==16:
             h=-1
         x=i-16*(i//16)
         y=i//16+h

         ghost=Ghost(x,y,tile_size,map_size)
         Map0.put(x,y,ghost)
         GHs.append(ghost)



       if MAP[i] == '^':
          h=0
          if i/16==16:
                h=-1
          x=i-16*(i//16)
          y=i//16+h
          wall=Wall(x,y,32,16)
          Walls.append(wall)
          Map0.put(x,y,wall)
       if MAP[i]=='.':
          h=0
          if i/16==16:
                h=-1
          x=i-16*(i//16)
          y=i//16+h
          poi=Point(x,y,tile_size,map_size)
          POint.append(poi)
          Map0.put(x,y,poi)
    print(Map0.map)
    print(Walls)
    p=len(POint)
    while pacman.life>0 and pacman.point!=p:
            process_events(pygame.event.get(), pacman)
            pygame.time.delay(100)



            draw_background(screen, background)





            pacman.game_tick()
            pacman.draw(screen)

            for wall in Walls:

                wall.draw(screen)
            for gh in GHs:
                gh.game_tick()
                gh.draw(screen)
            for poi in POint:
                if poi.live>0:
                    poi.draw(screen)


            pygame.display.update()

    if pacman.life>0:
        print('ПОБЕДА')

    else:
        print('ЛУЗЕР')
    print(pacman.point,pacman.life)
