import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
화면_너비 = 480
화면_높이 = 640
화면 = pygame.display.set_mode((화면_너비, 화면_높이))

# 게임 타이틀 설정
pygame.display.set_caption("움직이는 사각형 게임")

# FPS 설정
FPS = 60
시계 = pygame.time.Clock()

# 게임 색상
흰색 = (255, 255, 255)
파랑 = (0, 0, 255)
빨강 = (255, 0, 0)

# 플레이어 설정
플레이어_너비 = 50
플레이어_높이 = 50
플레이어_위치_x = 화면_너비 // 2 - 플레이어_너비 // 2
플레이어_위치_y = 화면_높이 // 2 - 플레이어_높이 // 2
플레이어_속도 = 5

# 공 설정
공_너비 = 30
공_높이 = 30
공_속도 = 5
공_리스트 = []
공_생성_시간 = pygame.time.get_ticks()

# 점수 설정
점수 = 0
폰트 = pygame.font.Font(None, 40)

# 공 생성 함수
def 공_생성():
    공_위치_x = random.randint(0, 화면_너비 - 공_너비)
    공_위치_y = -공_높이
    공_속도_x = random.randint(-3, 3)
    공_속도_y = random.randint(3, 8)
    공_리스트.append([공_위치_x, 공_위치_y, 공_속도_x, 공_속도_y])

# 게임 시작 시간
게임_시작_시간 = pygame.time.get_ticks()

# 게임 루프
게임_진행중 = True
while 게임_진행중:
    for 이벤트 in pygame.event.get():
        if 이벤트.type == pygame.QUIT:
            게임_진행중 = False

    # 플레이어 이동 처리
    키_입력 = pygame.key.get_pressed()
    if 키_입력[pygame.K_LEFT]:
        플레이어_위치_x -= 플레이어_속도
    if 키_입력[pygame.K_RIGHT]:
        플레이어_위치_x += 플레이어_속도
    if 키_입력[pygame.K_UP]:
        플레이어_위치_y -= 플레이어_속도
    if 키_입력[pygame.K_DOWN]:
        플레이어_위치_y += 플레이어_속도

    # 화면 경계 처리
    if 플레이어_위치_x < 0:
        플레이어_위치_x = 0
    if 플레이어_위치_x > 화면_너비 - 플레이어_너비:
        플레이어_위치_x = 화면_너비 - 플레이어_너비
    if 플레이어_위치_y < 0:
        플레이어_위치_y = 0
    if 플레이어_위치_y > 화면_높이 - 플레이어_높이:
        플레이어_위치_y = 화면_높이 - 플레이어_높이

    # 게임 시간 계산
    현재_시간 = pygame.time.get_ticks()
    경과_시간 = (현재_시간 - 게임_시작_시간) / 1000  # 밀리초를 초 단위로 변환

    # 1초마다 점수 추가
    if 경과_시간 >= 1:
        점수 += 100
        게임_시작_시간 = 현재_시간

    # 공 생성 및 이동 처리
    if 현재_시간 - 공_생성_시간 > 200:
        공_생성()
        공_생성_시간 = 현재_시간
    for 공 in 공_리스트:
        공[1] += 공[3]  # 공의 y 좌표에 속도 더하기
        if 공[1] > 화면_높이:
            공_리스트.remove(공)

    # 충돌 처리
    플레이어_사각형 = pygame.Rect(플레이어_위치_x, 플레이어_위치_y, 플레이어_너비, 플레이어_높이)
    for 공 in 공_리스트:
        공_사각형 = pygame.Rect(공[0], 공[1], 공_너비, 공_높이)
        if 플레이어_사각형.colliderect(공_사각형):
            게임_진행중 = False

    # 화면 그리기
    화면.fill(흰색)
    pygame.draw.rect(화면, 파랑, (플레이어_위치_x, 플레이어_위치_y, 플레이어_너비, 플레이어_높이))
    for 공 in 공_리스트:
        pygame.draw.rect(화면, 빨강, (공[0], 공[1], 공_너비, 공_높이))

    # 게임 오버 처리
    if not 게임_진행중:
        화면.blit(폰트.render("게임 오버", True, (0, 0, 0)), (200, 300))

    # 점수 표시
    점수_표시 = 폰트.render("점수: " + str(점수), True, (0, 0, 0))
    화면.blit(점수_표시, (10, 10))

    pygame.display.update()

    # FPS 설정
    시계.tick(FPS)

# 게임 종료
pygame.quit()
