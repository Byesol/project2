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
BROWN = (126, 71, 22)
OBROWN = (207,201,149)

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

# 배경 이미지 로드
background_image = pygame.image.load(os.path.join(assets_path, 'windmill.png'))

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
degree = 10
degree2 = 110
degree3 =200
degree4 = 290

# radian = np.deg2rad(degree)
# c = np.cos(radian)
# s = np.sin(radian)
# R = np.array([[c, -s], [s, c]])
# R, R.shape


#날개
poly1 = np.array([[0, 0, 1], [-50, -200, 1],  [50, -200, 1]])
poly1 = poly1.T  # 3*3 matrix
#몸통
poly2 = np.array([[400,700], [600,700],  [520,400], [480,400]])


done = False
begin = True
mode = 0
while not done:
    # 이벤트 반복 구간
 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    screen.blit(background_image,background_image.get_rect())

    degree+=1
    degree2+=1
    degree3+=1
    degree4+=1
    
    #날개들
    H1 = Tmat(500, 400) @ Rmat(degree)
    H2 = Tmat(500, 400) @ Rmat(degree2)
    H3 = Tmat(500, 400) @ Rmat(degree3)
    H4 = Tmat(500, 400) @ Rmat(degree4)


    pp1 = H1 @ poly1
    pp2 = H2 @ poly1  
    pp3 = H3 @ poly1  
    pp4 = H4 @ poly1      

    q1 = pp1[0:2,:].T
    q2 = pp2[0:2,:].T
    q3 = pp3[0:2,:].T
    q4 = pp4[0:2,:].T
    #windmill 몸통
    pygame.draw.polygon(screen, BROWN, poly2)
    #윈드밀 날개
    pygame.draw.polygon(screen, OBROWN, q1 )
    pygame.draw.polygon(screen, OBROWN, q2 )
    pygame.draw.polygon(screen, OBROWN, q3 )
    pygame.draw.polygon(screen, OBROWN, q4 )
    

    # 화면에 텍스트 표시

    # 화면 업데이트
    pygame.display.flip()

    # 초당 60 프레임으로 업데이트
    clock.tick(60)

# 게임 종료
pygame.quit()
