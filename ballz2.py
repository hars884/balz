import pygame
import random
def main():
    pygame.init()
    win = pygame.display.set_mode((600, 600))




    #variable  
    cho=0
    run = True
    cx=40
    cy=560
    n=0
    m=0

    class bal():
        def __init__(self,x,y,t):
            self.cx=x
            self.cy=y
            self.speed=5
            self.px=x
            self.py=y
            self.t=t
            self.st=pygame.time.get_ticks()
            self.cho=0
        
        def o(self):
            self.cx=self.px
            self.cy=self.py
            font=pygame.font.Font(None,30)
            keys = pygame.key.get_pressed()
            self.ct=pygame.time.get_ticks()
            if (self.ct-self.st)>=5000:
                self.cho=random.randint(0,2)
                self.st=self.ct
            if self.cho==0:
                text="ASUSUAL"
                text2=""
                if keys[pygame.K_LEFT]:
                    self.cx -= self.speed
                if keys[pygame.K_RIGHT]:
                    self.cx += self.speed
                if keys[pygame.K_UP]:
                    self.cy -= self.speed
                if keys[pygame.K_DOWN]:
                    self.cy += self.speed
            elif self.cho==1:
                text="PRESS->MOVE : RIGHT->LEFT"
                text2="LEFT->RIGHT : UP->DOWN : DOWN->UP"
                if keys[pygame.K_LEFT]:
                    self.cx += self.speed
                if keys[pygame.K_RIGHT]:
                    self.cx -= self.speed
                if keys[pygame.K_UP]:
                    self.cy += self.speed
                if keys[pygame.K_DOWN]:
                    self.cy -= self.speed
            elif self.cho==2:
                text="PRESS->MOVE : RIGHT->UP"
                text2="LEFT->DOWN : UP->RIGHT : DOWN->LEFT "
                if keys[pygame.K_LEFT]:
                    self.cy += self.speed
                if keys[pygame.K_RIGHT]:
                    self.cy -= self.speed
                if keys[pygame.K_UP]:
                    self.cx += self.speed
                if keys[pygame.K_DOWN]:
                    self.cx -= self.speed
            ts=font.render(text,True,(0,0,0))
            win.blit(ts,(30,0))
            ts2=font.render(text2,True,(0,0,0))
            win.blit(ts2,(30,32))
            '''if self.cy<40:
                self.cy=40
            if self.cy>560:
                self.cy=560
            if self.cx<40:
                self.cx=40
            if self.cx>560:
                self.cx=560'''
        def move(self):
            c=False
            for ti in self.t:
                nx=max(ti[0],min(self.cx,ti[0]+30))
                ny=max(ti[1],min(self.cy,ti[1]+30))
                dx=self.cx-nx
                dy=self.cy-ny
                if (((dx**2) +(dy**2))< 10**2):
                    c=True
                    break;
            if not c:
                self.px=self.cx
                self.py=self.cy
            pygame.draw.circle(win, (153,0,76), (self.px,self.py), 10)
            if self.px<30:
                return True
            else:
                return False

    #homepage
    def hp(n):
        hpo=["Start","Details"]
        win.fill((255,153,255))
        font=pygame.font.Font(None,50)
        for i in range(len(hpo)):
            if i==n:
                col=(0,0,0)
            else:
                col=(139,0,139)
            ts2=font.render(hpo[i],True,col)
            tr = ts2.get_rect(center=(600 // 2, 200 + i * 100))
            win.blit(ts2, tr)
        pygame.display.flip()
    #levelpage
    def lp(n):
        win.fill((255,153,255))
        lpo=["LEVEL 1","LEVEL 2"]
        font=pygame.font.Font(None,50)
        for i in range(len(lpo)):
            if i==n:
                col=(0,0,0)
            else:
                col=((139,0,139))
            ts2=font.render(lpo[i],True,col)
            tr = ts2.get_rect(center=(600 // 2, 200 + i * 100))#as we add level center=(600//2~x,iwhichpart*((600~scrnwidth//len(lop)~nooflev)//2~singlepartsenter))
            win.blit(ts2, tr)
        pygame.display.flip()
    #levelpage


    #detailpage
    def dp():
        win.fill((0,0,0))
        details_text = [
            "Game Instructions:",
            "1. Use arrow keys to move.",
            "2. Avoid obstacles.",
            "3. Reach the goal to win.",
            "Press ESC to return to the main menu."
        ]
        font_small = pygame.font.Font(None, 36)
        for i, line in enumerate(details_text):
            text = font_small.render(line, True, (255,255,255))
            text_rect = text.get_rect(center=(600 // 2, 150 + i * 40))
            win.blit(text, text_rect)
        pygame.display.flip()



    #grid
    def grid(p):
        x=0
        y=0
        ti=[]
        for i in range(0,len(p)):
            x=0
            for j in range(len(p)):
                if p[i][j]==1:
                    pygame.draw.rect(win, (153,51,255), (x, y,30, 30))
                    ti.append((x,y))
                if p[i][j]==2:
                    pygame.draw.rect(win, (0,0,0), (x,y,30, 30))
                x+=30
            y+=30
        return ti




    p1=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [2,0,0,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1],
    [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,1],
    [1,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,1],
    [1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    p2 = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1],
        [1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1],
        [1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
        [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
        [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    levels=[p1,p2]

#v=np

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if m!=3:
                if m==0:#menu
                    if event.type== pygame.KEYDOWN:
                        if event.key==pygame.K_DOWN:
                            n=1
                        elif event.key == pygame.K_UP:
                            n=0
                        if n==0 and event.key == pygame.K_RETURN:
                            m=1
                            n=0
                        if n==1 and event.key == pygame.K_RETURN:
                            m=2
                            n=0
                    hp(n)
                elif m==1:#level

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            n=1#can make n+=1 as we increase level but as there is only 2 level it is best(sts1)
                        elif event.key == pygame.K_UP:
                            n=0#can make n-=1 as we increase level but as there is only 2 level it is best(sts1)
                        if event.key == pygame.K_RETURN:
                            t=grid(levels[n])
                            ball=bal(cx,cy,t)
                            g=levels[n]
                            m=3
                        '''if we do sts1 add if n>len(lpo) then n=len(lpo)-1 or 
                        if n<0 then n=0'''
                        '''elif n==1 and event.key == pygame.K_RETURN:
                            t=grid(p2)
                            ball=bal(cx,cy,t)
                            g=p2
                            m=3'''
                    lp(n)
                elif m==2:#detail
                    dp()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            m=0
                            #n=0
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            m=0
                            #n=0
        if m==3:#lev1,2 
            win.fill((255,153,255))
            grid(g)
            ball.o()
            ball.move()
            pygame.time.Clock().tick(60)
            if ball.move() and n==0:
                n=1
                t=grid(levels[n])
                ball=bal(cx,cy,t)
                g=levels[n]
            elif ball.move() and n==1:
                m=0
                #n=0
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        m=1
                        #n=0
        pygame.display.update()
if __name__ == '__main__':
    main()
'''if we need to add level make lpo public and pass it to the lp as argument and creat a function add level
which takes a matrix and as input and make it public and add level to lpo
n=0 upper option
n=1 lower option
m=0 main menu
m=1 level
m=2 detail
m=3 game page'''