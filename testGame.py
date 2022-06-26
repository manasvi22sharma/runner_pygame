
import pygame
from sys import exit

def display_score():
    current_time=int((pygame.time.get_ticks())/1000-start_time)
    score_surf=test_font.render(f'Score:{current_time}',False,(64,64,64))
    score_rect=score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/PixelType.ttf',50)#(type,size)
game_active =False
start_time=0
score=0
#test_surface=pygame.Surface((100,200))
#test_surface.fill('Red')
sky_surface=pygame.image.load('graphics/Sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()
#score_surf=test_font.render('My Game',False,(64,64,64))#(text,AA,color)
#score_rect=score_surf.get_rect(center=(400,50))

snail_surface=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(700,300))
#snail_x_pos=600

obstacle_list=[]
player_surface=pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect=player_surface.get_rect(midbottom=(40,300))# rectange for thr surface used to place accurately and in collisons
player_gravity=0
#intro
player_stand=pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)#surface,rotation,scale
player_stand_rect=player_stand.get_rect(center=(400,200))

game_name=test_font.render('Pixel Runner',False,(119,196,169))
game_name_rect=game_name.get_rect(center=(400,60))

game_message=test_font.render('Press space to Start',False,(119,196,169))
game_message_rect=game_message.get_rect(center=(400,350))

#timmer
obstacle_timmer=pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timmer,900)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit() # this exit will also kill the while loop, this is the most secure way to close pygame
        
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom==300:
                        player_gravity=-20
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:
                    if player_rect.bottom==300:
                        player_gravity=-20 
        else:
              if event.type==pygame.KEYDOWN and event.key== pygame.K_SPACE:
                  game_active=True
                  snail_rect.left=800
                  start_time=int(pygame.time.get_ticks()/1000)
       # if event.type == obstacle_timmer and game_active:
        #    obstacle_list.append(snail_surface.get_rect(midbottom=(700,300)))
    if game_active:
         
        screen.blit(sky_surface,(0,0))#block image transfer, place one surface on another
        screen.blit(ground_surface,(0,300))
        #pygame.draw.rect(screen,'#c0e8ec',score_rect)
        #pygame.draw.rect(screen,'#c0e8ec',score_rect,10)#(surface,color,rect,width)
        #pygame.draw.line(screen,'Gold',(0,0),pygame.mouse.get_pos(),5)
        #screen.blit(score_surf,score_rect)
        score=display_score()
        #snail_x_pos-=3
        #if(snail_x_pos<-100):
        #    snail_x_pos=800
        #screen.blit(snail_surface,(snail_x_pos,250))
        if snail_rect.left < -100:
            snail_rect.left=800
        snail_rect.left-=5
        screen.blit(snail_surface,snail_rect)
        #player_rect.left+=1 move the player

        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom >=300: player_rect.bottom=300
        screen.blit(player_surface,player_rect)

        #keys=pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        #    print('jump')
        #collison
        #if player_rect.collidedict(snail_rect):# 0 no 1 yes
        #   print('collison')

        #mouse_pos=pygame.mouse.get_pos()
        #if player_rect.collidepoint((mouse_pos)) :

        #game end
        if snail_rect.colliderect(player_rect):
            game_active=False
            print('game over')
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message=test_font.render(f'your score:{score}',False,(119,196,169))
        score_message_rect=score_message.get_rect(center=(400,350))
        screen.blit(game_name,game_name_rect)
        if score==0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)
    pygame.display.update()
    clock.tick(60)#max frame rate, while loop should not run faster than 60 times per second
