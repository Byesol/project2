import pygame
import numpy as np
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def Rmat(deg):
    radian = np.deg2rad(deg)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    return R


def Tmat(a, b):
    H = np.eye(3)  # identity, 3x3
    H[0, 2] = a
    H[1, 2] = b
    return H

def star(x,y):
    pygame.draw.circle(screen, WHITE, [x,y], 5)

#이미지 파일 적용
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
sun_img = pygame.image.load(os.path.join(assets_path, 'sun.png'))
venus_img = pygame.image.load(os.path.join(assets_path, 'venus.png'))
earth_img = pygame.image.load(os.path.join(assets_path, 'earth.png'))
moon_img = pygame.image.load(os.path.join(assets_path, 'moon.png'))
saturn_img = pygame.image.load(os.path.join(assets_path, 'saturn.png'))
titan_img = pygame.image.load(os.path.join(assets_path, 'titan.png'))
spaceship_png = pygame.image.load(os.path.join(assets_path, 'spaceship.png'))

#우주선 변수들
keyboard_x = 1000
keyboard_y = 700
keyboard_dx = 0
keyboard_dy = 0
# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("Drawing")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# 게임 종료 전까지 반복
done = False

# 폰트 선택(폰트, 크기, 두껍게, 이탤릭)

degree1 = 10
degree2 = 10
degree3 = 10
degree4 = 10
degree5 = 10

cor = np.array([0, 0, 1])

done = False

#별 위치 랜덤 저장용
splist = []
for i in range(201):
    sp = [np.random.randint(0,WINDOW_WIDTH),np.random.randint(0,WINDOW_HEIGHT)]    
    splist.append(sp)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyboard_dx = -3
            elif event.key == pygame.K_RIGHT:
                keyboard_dx = 3
            elif event.key == pygame.K_UP:
                keyboard_dy = -3
            elif event.key == pygame.K_DOWN:
                keyboard_dy = 3
        # 키가 놓일 경우
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                keyboard_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                keyboard_dy = 0    
    # 우주선 이미지의 위치 변경
    keyboard_x += keyboard_dx
    keyboard_y += keyboard_dy

    screen.fill(BLACK)
    screen.blit(spaceship_png, [keyboard_x, keyboard_y])
    degree1 += 1 #지구
    degree2 += 365.26/27 #지구 공전주기 / 달 공전주기
    degree3 += 365.26/10756.20 #지구 / 토성
    degree4 += 365.26/15.95  #지구 / 토성
    degree5 += 365.26/224.47  #지구 / 금성

    #지구
    H1 = Tmat(600, 800) @ Rmat(degree1) @ Tmat(0, -300) 
    #달
    H2 = Tmat(600, 800) @ Rmat(degree1) @ Tmat(0, - 300) @ Rmat(degree2) @ Tmat(0, -80) 
    #토성
    H3 = Tmat(600, 800) @ Rmat(degree3) @ Tmat(0, -520) 
    #타이탄
    H4 = Tmat(600, 800) @ Rmat(degree3) @ Tmat(0, - 520) @ Rmat(degree4) @ Tmat(0, -100) 
    #금성
    H5 = Tmat(600, 800) @ Rmat(degree5) @ Tmat(0, -160) 
   
    pp1 = H1@cor   
    pp2 = H2@cor
    
    pp3 = H3@cor   
    pp4 = H4@cor

    pp5 = H5@cor

    #타원형 2분의 1
    pp1[1] *= 0.5
    pp2[1] *= 0.5
    pp3[1] *= 0.5
    pp4[1] *= 0.5
    pp5[1] *= 0.5
    
    #별만들기
    for i in range(len(splist)):
        splist[i]
        if np.random.randint(0,2) ==1:
            star = pygame.draw.circle(screen,WHITE,splist[i],2)

    #pygame.draw.circle(screen, (255, 128, 128), [600, 400], 30)
    screen.blit(sun_img, [570, 370])
    #pygame.draw.circle(screen, (255, 128, 128), pp1[:2], 18)
    screen.blit(earth_img, pp1[:2]-[18,18])    
    #pygame.draw.circle(screen, (255, 128, 128), pp2[:2], 10)
    screen.blit(moon_img, pp2[:2]-[10,10])

    #pygame.draw.circle(screen, (255, 128, 128), pp3[:2], 24)
    screen.blit(saturn_img, pp3[:2]-[24,24])
    #pygame.draw.circle(screen, (255, 128, 128), pp4[:2], 12)
    screen.blit(titan_img, pp4[:2]-[12,12])

   #pygame.draw.circle(screen, (255, 128, 128), pp5[:2], 16)
    screen.blit(venus_img, pp5[:2]-[16,16])

    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()

