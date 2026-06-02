import pygame
import sys
import time 
import random
import asyncio

pygame.init()
screen = pygame.display.set_mode((858,525))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()



async def main():
	running = True
	score1 = 0
	score2 = 0
	paddle2_pos = 202
	paddle1 = pygame.Rect(843,202,10,60)
	paddle2 = pygame.Rect(5,paddle2_pos,10,60)
	ball_x = 420
	ball_y = 230
	ball_speed_x = 0 
	ball_speed_y = 0
	ball_speed = 12
	paddle2_speed = 10
	startSequence = 3
	font1 = pygame.font.SysFont("monaco",112)
	firstTick = pygame.time.get_ticks()
	while running:

		screen.fill("black")

		currentTick = pygame.time.get_ticks()
		if currentTick - firstTick >= 750 and startSequence >= 0:
			startSequence -= 1
			firstTick = currentTick
			if startSequence == 0:
				ball_speed_x = random.choice([-ball_speed, ball_speed])
				ball_speed_y = random.choice([-ball_speed, ball_speed])
		if startSequence > 0:
			countdown_surface = font1.render(str(startSequence),True,"white")
			screen.blit(countdown_surface,[410,200])


		ball_x += ball_speed_x
		ball_y += ball_speed_y
		ball = pygame.Rect(ball_x,ball_y,15,15)

		if ball_x > 858:
			score1+=1
			ball_x = 420
			ball_y = 230
			ball_speed_x = random.choice([-ball_speed, ball_speed])
			ball_speed_y = random.choice([-ball_speed, ball_speed])
		if ball_x < 0:
			score2+=1
			ball_x = 420
			ball_y = 230
			ball_speed_x = random.choice([-ball_speed, ball_speed])
			ball_speed_y = random.choice([-ball_speed, ball_speed])

		if ball_y > 525 or ball_y < 0:
			ball_speed_y*= -1

		if pygame.Rect.colliderect(ball,paddle1):
			if ball[1] > paddle1[1] + 30: #lower portion of paddle
				if ball_speed_y > 0: #balls moving on a downward angle
					ball_speed_y*= 1
				if ball_speed_y < 0: #balls moving on a upward angle
					ball_speed_y*= -1
			if ball[1] < paddle1[1] + 30: #upper portion of paddle
				if ball_speed_y > 0: #balls moving on a downward angle
					ball_speed_y*= -1
				if ball_speed_y < 0: #balls moving on a upward angle
					ball_speed_y*= 1
			ball_speed_x*= -1
		if pygame.Rect.colliderect(ball,paddle2):
			if ball[1] > paddle2[1] + 30: #lower portion of paddle
				if ball_speed_y > 0: #balls moving on a downward angle
					ball_speed_y*= 1
				if ball_speed_y < 0: #balls moving on a upward angle
					ball_speed_y*= -1
			if ball[1] < paddle2[1] + 30: #upper portion of paddle
				if ball_speed_y > 0: #balls moving on a downward angle
					ball_speed_y*= -1
				if ball_speed_y < 0: #balls moving on a upward angle
					ball_speed_y*= 1
			ball_speed_x*= -1


		


		mousePos = pygame.mouse.get_pos()
		if mousePos[1] > 15 and mousePos[1] < 510:
			paddle1.y = mousePos[1]-30

		if startSequence <= 0:
			if ball[1] > paddle2[1] and paddle2[1] < 465-paddle2_speed:
				paddle2_pos+=paddle2_speed
			elif ball[1] < paddle2[1] and paddle2[1] > paddle2_speed:
				paddle2_pos-=paddle2_speed

		paddle2.y = paddle2_pos

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		score1_surface = font1.render(str(score1),True,"white")
		score2_surface = font1.render(str(score2),True,"white")
		screen.blit(score1_surface,[215,5])
		screen.blit(score2_surface,[644,5])

		for i in range(0,525,30):
			pygame.draw.line(screen,"white",(428,i),(428,i+15))

		pygame.draw.rect(screen,"white",paddle1)
		pygame.draw.rect(screen,"white",paddle2)
		pygame.draw.rect(screen,"white",ball)

		pygame.display.flip()
		clock.tick(60)
		await asyncio.sleep(0)

	pygame.quit()

asyncio.run(main())