import pygame
import random
import time
import sys
import os

pygame.init()

# all color
black=(0,0,0)
red=(250,0,0)
green=(0,250,0)
cyan=(0,250,250)
yellow=(250,250,0)
blue=(0,0,250)
#some variable
magenta=(250,0,250)
screen_width=500
snake_size=20
food_size=20
clock=pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS',17)
font_name=pygame.font.SysFont("Script",15)
game_win=pygame.display.set_mode((screen_width,screen_width))
pygame.display.set_caption("Snake")
hi_score=0

def plot_sanke(snk_list,direction):
	for i in range(len(snk_list)):
		x,y=snk_list[i]
		if i==len(snk_list)-1:
			pygame.draw.rect(game_win,magenta,[x,y,snake_size,snake_size])
			if direction=="up" or direction=="down" or direction=="":
				pygame.draw.circle(game_win,black,(x+5,y+10),3)
				pygame.draw.circle(game_win,black,(x+15,y+10),3)
			if direction=="left" or direction=="rigth":	
				pygame.draw.circle(game_win,black,(x+10,y+5),3)
				pygame.draw.circle(game_win,black,(x+10,y+15),3)
		else:
			pygame.draw.rect(game_win,cyan,[x,y,snake_size,snake_size])

def draw_grid():
	a=40
	for i in range(22):
		pygame.draw.aaline(game_win,blue,(20,a),(screen_width-20,a),100)
		pygame.draw.aaline(game_win,blue,(a,20),(a,screen_width-20),100)
		a+=20

# game loop
def game_loop():
	exit_game=False
	game_over=False
	snake_x=240
	snake_y=240
	velocity_x=0
	velocity_y=0
	fps=7
	snk_length=2
	direction=""
	snk_list=[]
	status=True
	score=0
	global hi_score
	



	while True:
		food_x=(random.randint(2,22)*20)
		food_y=(random.randint(2,22)*20)
		if [food_x,food_y]==[snake_x,snake_y]:
			continue
		elif [food_x,food_y]==[snake_x,snake_y-20]:
			continue
		else:
			break

	while not exit_game:
		game_win.fill(black)

		if score>=hi_score:
			hi_score=score

		if game_over:
			game_win.blit(font.render("Game Over!!", True, yellow),[200,200])
			game_win.blit(font.render("Press 'Space-Bar' To Restart", True, yellow),[150,250])
			game_win.blit(font.render("Your Score:"+str(score), True, yellow),[195,300])
			game_win.blit(font_name.render("A_R_N_A_B",True, green),[440,485])

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit(0)

				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_SPACE:
						game_loop()
		else:	
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit(0)

				if event.type==pygame.KEYDOWN:
					if (event.key==pygame.K_RIGHT or event.key==pygame.K_d)  and direction!="left":
						direction="rigth"
						velocity_x=20
						velocity_y=0
						
					elif (event.key==pygame.K_LEFT or event.key==pygame.K_a) and direction!="rigth":
						direction="left"
						velocity_x=-20
						velocity_y=0

					elif (event.key==pygame.K_UP or event.key==pygame.K_w) and direction!="down":
						direction="up"
						velocity_x=0
						velocity_y=-20

					elif (event.key==pygame.K_DOWN or event.key==pygame.K_s) and direction!="up":
						direction="down"
						velocity_x=0
						velocity_y=20
		    
			snake_x+=velocity_x
			snake_y+=velocity_y

			if snake_x<=20 or snake_x+20>460 or snake_y<=20 or snake_y+20>460:
				game_over=True

			if direction=="" and snk_length==2:
				pygame.draw.rect(game_win,cyan,[snake_x,snake_y-20,20,20])




			head=[]	
			head.append(snake_x)
			head.append(snake_y)


			if head in snk_list[:-2]:
				game_over=True


			snk_list.append(head)

			if abs(snake_x - food_x )<5 and abs(snake_y - food_y)<5:
				
				while True:
					food_x=random.randint(2,22)*20
					food_y=random.randint(2,22)*20
					if [food_x,food_y] in snk_list:
						continue
					else:
						break
				score+=5
				snk_length+=1

			if len(snk_list)>snk_length:
				del snk_list[0]

			pygame.draw.aaline(game_win,green,(20,20),(screen_width-20,20))
			pygame.draw.aaline(game_win,green,(20,20),(20,screen_width-20))
			pygame.draw.aaline(game_win,green,(20,screen_width-20),(screen_width-20,screen_width-20))
			pygame.draw.aaline(game_win,green,(screen_width-20,screen_width-20),(screen_width-20,20))
			plot_sanke(snk_list,direction)
			pygame.draw.rect(game_win,red,[food_x,food_y,food_size,food_size])
			draw_grid()
			
			game_win.blit(font.render("SCORE:"+str(score), True, yellow),[20,0])
			game_win.blit(font.render("LENGTH:"+str(snk_length-2),True, yellow),[380,0])
			game_win.blit(font.render("HIGH-SCORE:"+str(hi_score),True, yellow),[180,0])
			game_win.blit(font_name.render("A_R_N_A_B",True, green),[440,485])

		pygame.display.update()	
		if score<100:
			fps=8
		elif score<150 and score>=100:
			fps=9
		elif score<200 and score>=150:
			fps=10
		elif score<300 and score>=200:
			fps=11
		elif score<400 and score>=300:
			fps=12
		else:
			fps=13

		clock.tick(fps)		
__name__
game_loop()
sys.exit(0)