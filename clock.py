import pygame
import numpy as np
import os
import datetime


# 게임 윈도우 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (126, 71, 22)
OBROWN = (207,201,149)


#시침
poly1 = np.array([[0, 0, 1], [10, -10, 1], [0, -100, 1], [-10, -10, 1]])
poly1= poly1.T
#분침
poly2 = np.array([[0, 0, 1], [5, -20, 1], [0, -150, 1], [-5, -20, 1]])
poly2= poly2.T
#초침
poly3 = np.array([[0, 0, 1], [0, -200, 1]])
poly3= poly3.T
#눈금
cor = np.array([[0, -220, 1],[0,-250,1]])
cor = cor.T
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
font = pygame.font.SysFont('FixedSys', 40, True, False)
degree = 0
degree2 = 0
degree3 =0
degree4=0

done = False

while not done:
    # 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    now =datetime.datetime.now()
    h,m,s = now.hour,now.minute,now.second
    #print(h)
    degree = h* 30  +m*0.5 
    degree2= m * 6      
    degree3 = s*6    
    
    H1 = Tmat(400, 400) @ Rmat(degree)
    H2 = Tmat(400, 400) @ Rmat(degree2)
    H3 = Tmat(400, 400) @ Rmat(degree3)

    pp1 = H1 @ poly1
    pp2 = H2 @ poly2  
    pp3 = H3 @ poly3     

    q1 = pp1[0:2,:].T
    q2 = pp2[0:2,:].T
    q3 = pp3[0:2,:].T          

    pygame.draw.circle(screen,BLACK,[400,400],250,2)
    for i in range(12):
        degree4 = i*30
        H = Tmat(400, 400) @ Rmat(degree4)
        corp = H @ cor
        q4 = corp[0:2,:].T
        pygame.draw.line(screen, BLACK, q4[0],q4[1],2) 

    pygame.draw.polygon(screen, BLUE, q1 )
    pygame.draw.polygon(screen, GREEN, q2 )
    pygame.draw.line(screen, RED, q3[0],q3[1],2) 
 
        


    

    pygame.display.flip()
    

    # 화면에 텍스트 표시

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
