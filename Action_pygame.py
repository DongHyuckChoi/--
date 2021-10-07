import pygame
import sys
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIME = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 192, 0)
RED = (255, 0, 0)
PINK = (255, 128, 255)
VIOLET = (255, 0, 224)

img_bg = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\chip00.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\chip01.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\chip02.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\chip03.png")
]
img_Hiroshi = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi00.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi01.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi02.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi03.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi04.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi05.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi06.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi07.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi08.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi09.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi10.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi11.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Hiroshi_face.png")
]
img_Granny = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny00.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny01.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny02.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny03.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny04.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny05.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny06.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny07.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny08.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny09.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny10.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Granny11.png")
]
img_COVID =  pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\COVID.png")
img_AlDS =  pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\AlDS.png")
img_Bluevirus = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Bluevirus.png")
img_HerpesVirus = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\HerpesVirus.png")
img_Greenherpesvirus = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\Greenherpesvirus.png")

img_title = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\title.png")
img_ending = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Action\\ending.png")

se_Vaccine = None

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]
BLINK = [(255, 255, 255), (255, 255, 192), (255, 255, 128), (255, 224, 64), (255, 255, 128), (255, 255, 192)]

idx = 0
tmr = 0
stage = 1
score = 0
nokori = 7 # 7개 생명
Vaccine = 0

Hiroshi_x = 0
Hiroshi_y = 0
Hiroshi_d = 0 #방향
Hiroshi_a = 0 #캐릭터의 이미지 번호
Hiroshi_sx = 0
Hiroshi_sy = 0

Granny_x = 0
Granny_y = 0
Granny_d = 0
Granny_a = 0
Granny_sx = 0
Granny_sy = 0

COVID_x = 0
COVID_y = 0
COVID_d = 0
COVID_a = 0
COVID_sx = 0
COVID_sy = 0
COVID_sd = 0

AlDS_x = 0
AlDS_y = 0
AlDS_d = 0
AlDS_a = 0
AlDS_sx = 0
AlDS_sy = 0
AlDS_sd = 0

Bluevirus_x = 0
Bluevirus_y = 0
Bluevirus_d = 0
Bluevirus_a = 0
Bluevirus_sx = 0
Bluevirus_sy = 0
Bluevirus_sd = 0

HerpesVirus_x = 0
HerpesVirus_y = 0
HerpesVirus_d = 0
HerpesVirus_a = 0
HerpesVirus_sx = 0
HerpesVirus_sy = 0
HerpesVirus_sd = 0

Greenherpesvirus_x = 0
Greenherpesvirus_y = 0
Greenherpesvirus_d = 0
Greenherpesvirus_a = 0
Greenherpesvirus_sx = 0
Greenherpesvirus_sy = 0
Greenherpesvirus_sd = 0


map_data = []  # 미로 용 리스트


def set_stage():  # 스테이지 데이터 설정
    global map_data, Vaccine
    global Granny_sx, Granny_sy
    global Hiroshi_sx, Hiroshi_sy
    global COVID_sx, COVID_sy, COVID_sd
    global AlDS_sx, AlDS_sy, AlDS_sd
    global Bluevirus_sx, Bluevirus_sy, Bluevirus_sd
    global HerpesVirus_sx, HerpesVirus_sy, HerpesVirus_sd
    global Greenherpesvirus_sx, Greenherpesvirus_sy, Greenherpesvirus_sd
    

    if stage == 1:
        map_data = [
            [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
            [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
            [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
            [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
            [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
            [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
            [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        Vaccine = 32 #32
        Granny_sx = 630
        Granny_sy = 450
        COVID_sd = -1 #코로나가 출현하지 않음
        AlDS_sd = -1
        Bluevirus_sd = -1
        HerpesVirus_sd = -1
        Greenherpesvirus_sd = -1
       

    if stage == 2:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 3, 3, 0, 2, 1, 1, 2, 0, 3, 3, 0],
            [0, 3, 3, 1, 3, 3, 3, 3, 1, 3, 3, 0],
            [0, 2, 1, 3, 3, 3, 3, 3, 3, 1, 2, 0],
            [0, 3, 3, 0, 3, 3, 3, 3, 0, 3, 3, 0],
            [0, 3, 3, 1, 2, 1, 1, 2, 1, 3, 3, 0],
            [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        Vaccine = 38#38
        Granny_sx = 630
        Granny_sy = 90
        COVID_sx = 330
        COVID_sy = 270
        COVID_sd = DIR_LEFT
        AlDS_sd = -1
        Bluevirus_sd = -1
        HerpesVirus_sd = -1
        Greenherpesvirus_sd = -1
      


    if stage == 3:
        map_data = [
            [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 1, 3, 1, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0],
            [0, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0],
            [0, 1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0],
            [0, 3, 3, 3, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        Vaccine = 23 #23
        Granny_sx = 630
        Granny_sy = 450
        COVID_sx = 330
        COVID_sy = 270
        COVID_sd = DIR_RIGHT
        AlDS_sd = -1
        Bluevirus_sd = -1
        HerpesVirus_sd = -1
        Greenherpesvirus_sd = -1
    

    if stage == 4:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 3, 0, 3, 3, 1, 3, 0, 3, 0, 3, 0],
            [0, 3, 1, 0, 3, 3, 3, 0, 3, 1, 3, 0],
            [0, 3, 3, 0, 1, 1, 1, 0, 3, 3, 3, 0],
            [0, 3, 0, 1, 3, 3, 3, 1, 3, 1, 1, 0],
            [0, 3, 1, 3, 3, 1, 3, 3, 3, 3, 3, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        Vaccine = 50 #50
        Granny_sx = 150
        Granny_sy = 270
        COVID_sx = 510
        COVID_sy = 270
        COVID_sd = DIR_UP
        AlDS_sd = -1
        Bluevirus_sd = -1
        HerpesVirus_sd = -1
        Greenherpesvirus_sd = -1
    
       

    if stage == 5:
        map_data = [
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 0, 3, 0, 1, 3, 3, 1, 0, 3, 0],
            [0, 2, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0],
            [0, 2, 1, 3, 1, 1, 3, 3, 1, 1, 3, 0],
            [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0],
            [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        Vaccine = 40 #40
        Granny_sx = 630
        Granny_sy = 450
        COVID_sx = 390
        COVID_sy = 210
        COVID_sd = DIR_RIGHT
        AlDS_sd = -1
        Bluevirus_sd = -1
        HerpesVirus_sd = -1
        Greenherpesvirus_sd = -1
        
    
    if stage == 6:
        map_data = [
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 2, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0],
        ]
        Vaccine = 32
        Granny_sx = 630
        Granny_sy = 390
        COVID_sx = 150
        COVID_sy = 90
        COVID_sd = DIR_DOWN
        AlDS_sx = 270
        AlDS_sy = 450
        AlDS_sd = DIR_UP
        Bluevirus_sx = 390
        Bluevirus_sy = 90
        Bluevirus_sd = DIR_DOWN
        HerpesVirus_sx = 510
        HerpesVirus_sy = 450
        HerpesVirus_sd = DIR_UP
        Greenherpesvirus_sx = 630
        Greenherpesvirus_sy = 90
        Greenherpesvirus_sd = DIR_DOWN


def set_chara_pos():  # 캐릭터 시작 위치
    global Hiroshi_x, Hiroshi_y, Hiroshi_d, Hiroshi_a
    global Granny_x, Granny_y, Granny_d, Granny_a
    global COVID_x, COVID_y, COVID_d, COVID_a
    global AlDS_x, AlDS_y, AlDS_d, AlDS_a
    global Bluevirus_x, Bluevirus_y, Bluevirus_d, Bluevirus_a
    global HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, HerpesVirus_a
    global Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, Greenherpesvirus_a
    Hiroshi_x = 90
    Hiroshi_y = 90
    Hiroshi_d = DIR_DOWN #히로시 방향 아래로
    Hiroshi_a = 3 #히로시 그림 번호 대입
    Granny_x = Granny_sx
    Granny_y = Granny_sy
    Granny_d = DIR_DOWN
    Granny_a = 3
    COVID_x = COVID_sx
    COVID_y = COVID_sy
    COVID_d = COVID_sd
    COVID_a = 0
    
    AlDS_x = AlDS_sx
    AlDS_y = AlDS_sy
    AlDS_d = AlDS_sd
    AlDS_a = 0

    Bluevirus_x = Bluevirus_sx
    Bluevirus_y = Bluevirus_sy
    Bluevirus_d = Bluevirus_sd
    Bluevirus_a = 0

    HerpesVirus_x = HerpesVirus_sx
    HerpesVirus_y = HerpesVirus_sy
    HerpesVirus_d = HerpesVirus_sd
    HerpesVirus_a = 0

    Greenherpesvirus_x = Greenherpesvirus_sx
    Greenherpesvirus_y = Greenherpesvirus_sy
    Greenherpesvirus_d = Greenherpesvirus_sd
    Greenherpesvirus_a = 0


def draw_txt(scrn, txt, x, y, siz, col):  # 그림자 포함 문자
    fnt = pygame.font.Font(None, siz * 2) 
    sur = fnt.render(txt, True, BLACK)
    x = x - sur.get_width() / 2
    y = y - sur.get_height() / 2
    scrn.blit(sur, [x + 2, y + 2])
    sur = fnt.render(txt, True, col) 
    scrn.blit(sur, [x, y])


def draw_screen(scrn):  # 게임 화면 그리기
    for y in range(9):
        for x in range(12):
            scrn.blit(img_bg[map_data[y][x]], [x * 60, y * 60]) #맵 칩으로 미로를 그린다.
    scrn.blit(img_Hiroshi[Hiroshi_a], [Hiroshi_x - 30, Hiroshi_y - 30]) #히로시 표시
    scrn.blit(img_Granny[Granny_a], [Granny_x - 30, Granny_y - 30]) #그래니 표시
    if COVID_sd != -1:
        scrn.blit(img_COVID, [COVID_x - 30, COVID_y - 30])
    draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE)
    draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori): #히로시의 남은 수만큼 반복
        scrn.blit(img_Hiroshi[12], [60 + i * 50, 500])  #히로시의 남은 수  표시

    if AlDS_sd != -1:
        scrn.blit(img_AlDS, [AlDS_x - 30, AlDS_y - 30])
    draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE) #스테이지 수 표시
    draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori): #히로시의 남은 수만큼 반복
        scrn.blit(img_Hiroshi[12], [60 + i * 50, 500])  #히로시의 남은 수  표시

    if Bluevirus_sd != -1:
        scrn.blit(img_Bluevirus, [Bluevirus_x - 30, Bluevirus_y - 30])
    draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE) #스테이지 수 표시
    draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori): #히로시의 남은 수만큼 반복
        scrn.blit(img_Hiroshi[12], [60 + i * 50, 500])  #히로시의 남은 수  표시

    if HerpesVirus_sd != -1:
        scrn.blit(img_HerpesVirus, [HerpesVirus_x - 30, HerpesVirus_y - 30])
    draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE) #스테이지 수 표시
    draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori): #히로시의 남은 수만큼 반복
        scrn.blit(img_Hiroshi[12], [60 + i * 50, 500])  #히로시의 남은 수  표시

    if Greenherpesvirus_sd != -1:
        scrn.blit(img_Greenherpesvirus, [Greenherpesvirus_x - 30, Greenherpesvirus_y - 30])
    draw_txt(scrn, "SCORE " + str(score), 200, 30, 30, WHITE) #스테이지 수 표시
    draw_txt(scrn, "STAGE " + str(stage), 520, 30, 30, LIME)
    for i in range(nokori): #히로시의 남은 수만큼 반복
        scrn.blit(img_Hiroshi[12], [60 + i * 50, 500])  #히로시의 남은 수  표시


def check_wall(cx, cy, di, dot):  # 각 방향에 벽 존재 여부 확인
    chk = False
    if di == DIR_UP:
        mx = int((cx - 30) / 60) #mx와 my에 리스트의 좌상 방향
        my = int((cy - 30 - dot) / 60) #확인용 값 대입
        if map_data[my][mx] <= 1:  # 좌상, 벽이라면
            chk = True #chk에 True를 대입한다.
        mx = int((cx + 29) / 60)  #리스트의 우상 방향 확인용 값 대입
        if map_data[my][mx] <= 1:  # 우상, 벽이라면
            chk = True #chk에 Ture를 대입한다
    if di == DIR_DOWN: #아래쪽인 경우
        mx = int((cx - 30) / 60) #mx와 my에 리스트의 좌하 방향
        my = int((cy + 29 + dot) / 60) #확인용 값 대우
        if map_data[my][mx] <= 1:  # 좌하, 벽이라면
            chk = True #chk에 Ture를 대입한다
        mx = int((cx + 29) / 60) #리스트의 우하 방향 확인용 값 대입
        if map_data[my][mx] <= 1:  # 우하, 벽이라면
            chk = True #chk에 Ture를 대입한다
    if di == DIR_LEFT: #왼쪽인 경우
        mx = int((cx - 30 - dot) / 60)  #mx와 my에 리스트의 좌상 방향
        my = int((cy - 30) / 60) #확인용 값을 대입한다
        if map_data[my][mx] <= 1:  # 좌상, 벽이라면
            chk = True #chk에 Ture를 대입한다
        my = int((cy + 29) / 60)  #mx와 my에 리스트의 좌상 방향 
        if map_data[my][mx] <= 1:  # 좌하, 벽이라면
            chk = True #chk에 Ture를 대입한다
    if di == DIR_RIGHT: #오른쪽인경우
        mx = int((cx + 29 + dot) / 60) #mx와 my에 리스트의 우상 방향
        my = int((cy - 30) / 60) #리스트 방향에확인용 값을 대입
        if map_data[my][mx] <= 1:  # 우상, 벽이라면
            chk = True #chk에 Ture를 대입한다
        my = int((cy + 29) / 60) #리스트 방향에 확인용값 대입
        if map_data[my][mx] <= 1:  # 우하, 벽이라면
            chk = True #chk에 Ture를 대입한다
    return chk


def move_penpen(key):  # 히로시 움직이기
    global score, Vaccine, Hiroshi_x, Hiroshi_y, Hiroshi_d, Hiroshi_a
    if key[K_UP] == 1:
        Hiroshi_d = DIR_UP
        if check_wall(Hiroshi_x, Hiroshi_y, Hiroshi_d, 20) == False:
            Hiroshi_y = Hiroshi_y - 20
    elif key[K_DOWN] == 1:
        Hiroshi_d = DIR_DOWN
        if check_wall(Hiroshi_x, Hiroshi_y, Hiroshi_d, 20) == False:
            Hiroshi_y = Hiroshi_y + 20
    elif key[K_LEFT] == 1:
        Hiroshi_d = DIR_LEFT
        if check_wall(Hiroshi_x, Hiroshi_y, Hiroshi_d, 20) == False:
            Hiroshi_x = Hiroshi_x - 20
    elif key[K_RIGHT] == 1:
        Hiroshi_d = DIR_RIGHT
        if check_wall(Hiroshi_x, Hiroshi_y, Hiroshi_d, 20) == False:
            Hiroshi_x = Hiroshi_x + 20
    Hiroshi_a = Hiroshi_d * 3 + ANIMATION[tmr % 4] #히로시 이미지 번호 계산
    mx = int(Hiroshi_x / 60)
    my = int(Hiroshi_y / 60)
    if map_data[my][mx] == 3:  # 백신에 닿았는가?
        score = score + 100
        map_data[my][mx] = 2 #백신 삭제
        Vaccine = Vaccine - 1 #백신 뺴기
        se_Vaccine.play()


def move_enemy():  # 그래니 움직이기
    global idx, tmr, Granny_x, Granny_y, Granny_d, Granny_a
    speed = 10
    if Granny_x % 60 == 30 and Granny_y % 60 == 30: #칸이 정확한 위치에 있는경우
        Granny_d = random.randint(0, 6) #무작위로 방향변경
        if Granny_d >= 4: #난수가 4이상이면
            if Hiroshi_y < Granny_y: #히로시가 위쪽에 있다면
                Granny_d = DIR_UP #그래니를 위쪽으로 이동
            if Hiroshi_y > Granny_y: #히로시가 아래쪽에 있다면
                Granny_d = DIR_DOWN #그래니를 아래쪽으로 이동
            if Hiroshi_x < Granny_x: #히로시가 왼쪽에 있다면
                Granny_d = DIR_LEFT #그래니를 왼쪽으로
            if Hiroshi_x > Granny_x: #히로시가 오른쪽에 있다면
                Granny_d = DIR_RIGHT #그래니를 오론쯕으로 이동
    if Granny_d == DIR_UP: #그래니가 위쪽으로 향한 경우
        if check_wall(Granny_x, Granny_y, Granny_d, speed) == False: #해당 뱡향이 벽이 아니라면
            Granny_y = Granny_y - speed #y좌표 감소 위쪽으로 이동
    if Granny_d == DIR_DOWN: #그래니가 아래쪽을 향한 경우
        if check_wall(Granny_x, Granny_y, Granny_d, speed) == False: #해당 방향이 벽이 아니라면
            Granny_y = Granny_y + speed #y좌표 증가 아래쪽으로 이동
    if Granny_d == DIR_LEFT: #그래니가 왼쪽을 향한경우
        if check_wall(Granny_x, Granny_y, Granny_d, speed) == False: #해당 뱡향이 벽이 아니라면
            Granny_x = Granny_x - speed #x좌표 감소 왼쪽으로 이동
    if Granny_d == DIR_RIGHT: # 그래니가 오른쪽으로 이동한 경우
        if check_wall(Granny_x, Granny_y, Granny_d, speed) == False: #해당 뱡향이 벽이 아니라면
            Granny_x = Granny_x + speed #x좌표 증가 오른쪽으로 이동
    Granny_a = Granny_d * 3 + ANIMATION[tmr % 4] #그래니 이미지 번호 계산
    if abs(Granny_x - Hiroshi_x) <= 40 and abs(Granny_y - Hiroshi_y) <= 40: #히로시와 접촉했는지를 판단
        idx = 2
        tmr = 0 #tmr을 0으로 변경, 당했다 처리로 감.
 

def move_enemy2():  # COVID 움직이기
    global idx, tmr, COVID_x, COVID_y, COVID_d, COVID_a
    speed = 5
    if COVID_sd == -1:
        return
    if COVID_d == DIR_UP:
        if check_wall(COVID_x, COVID_y, COVID_d, speed) == False:
            COVID_y = COVID_y - speed
        else:
            COVID_d = DIR_DOWN
    elif COVID_d == DIR_DOWN:
        if check_wall(COVID_x, COVID_y, COVID_d, speed) == False:
            COVID_y = COVID_y + speed
        else:
            COVID_d = DIR_UP
    elif COVID_d == DIR_LEFT:
        if check_wall(COVID_x, COVID_y, COVID_d, speed) == False:
            COVID_x = COVID_x - speed
        else:
            COVID_d = DIR_RIGHT
    elif COVID_d == DIR_RIGHT:
        if check_wall(COVID_x, COVID_y, COVID_d, speed) == False:
            COVID_x = COVID_x + speed
        else:
            COVID_d = DIR_LEFT
    if abs(COVID_x - Hiroshi_x) <= 40 and abs(COVID_y - Hiroshi_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy3():  # AlDS 움직이기
    global idx, tmr, AlDS_x, AlDS_y, AlDS_d, AlDS_a
    speed = 5
    if AlDS_sd == -1:
        return
    if AlDS_d == DIR_UP:
        if check_wall(AlDS_x, AlDS_y, AlDS_d, speed) == False:
            AlDS_y = AlDS_y - speed
        else:
            AlDS_d = DIR_DOWN
    elif AlDS_d == DIR_DOWN:
        if check_wall(AlDS_x, AlDS_y, AlDS_d, speed) == False:
            AlDS_y = AlDS_y + speed
        else:
            AlDS_d = DIR_UP
    elif AlDS_d == DIR_LEFT:
        if check_wall(AlDS_x, AlDS_y, AlDS_d, speed) == False:
            AlDS_x = AlDS_x - speed
        else:
            AlDS_d = DIR_RIGHT
    elif AlDS_d == DIR_RIGHT:
        if check_wall(AlDS_x, AlDS_y, AlDS_d, speed) == False:
            AlDS_x = AlDS_x + speed
        else:
            AlDS_d = DIR_LEFT
    if abs(AlDS_x - Hiroshi_x) <= 40 and abs(AlDS_y - Hiroshi_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy4():  # Bluevirus 움직이기
    global idx, tmr, Bluevirus_x, Bluevirus_y, Bluevirus_d, Bluevirus_a
    speed = 5
    if Bluevirus_sd == -1:
        return
    if Bluevirus_d == DIR_UP:
        if check_wall(Bluevirus_x, Bluevirus_y, Bluevirus_d, speed) == False:
            Bluevirus_y = Bluevirus_y - speed
        else:
            Bluevirus_d = DIR_DOWN
    elif Bluevirus_d == DIR_DOWN:
        if check_wall(Bluevirus_x, Bluevirus_y, Bluevirus_d, speed) == False:
            Bluevirus_y = Bluevirus_y + speed
        else:
            Bluevirus_d = DIR_UP
    elif Bluevirus_d == DIR_LEFT:
        if check_wall(Bluevirus_x, Bluevirus_y, Bluevirus_d, speed) == False:
            Bluevirus_x = Bluevirus_x - speed
        else:
            Bluevirus_d = DIR_RIGHT
    elif Bluevirus_d == DIR_RIGHT:
        if check_wall(Bluevirus_x, Bluevirus_y, Bluevirus_d, speed) == False:
            Bluevirus_x = Bluevirus_x + speed
        else:
            Bluevirus_d = DIR_LEFT
    if abs(Bluevirus_x - Hiroshi_x) <= 40 and abs(Bluevirus_y - Hiroshi_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy5():  # HerpesVirus 움직이기
    global idx, tmr, HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, HerpesVirus_a
    speed = 5
    if HerpesVirus_sd == -1:
        return
    if HerpesVirus_d == DIR_UP:
        if check_wall(HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, speed) == False:
            HerpesVirus_y = HerpesVirus_y - speed
        else:
            HerpesVirus_d = DIR_DOWN
    elif HerpesVirus_d == DIR_DOWN:
        if check_wall(HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, speed) == False:
            HerpesVirus_y = HerpesVirus_y + speed
        else:
            HerpesVirus_d = DIR_UP
    elif HerpesVirus_d == DIR_LEFT:
        if check_wall(HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, speed) == False:
            HerpesVirus_x = HerpesVirus_x - speed
        else:
            HerpesVirus_d = DIR_RIGHT
    elif HerpesVirus_d == DIR_RIGHT:
        if check_wall(HerpesVirus_x, HerpesVirus_y, HerpesVirus_d, speed) == False:
            HerpesVirus_x = HerpesVirus_x + speed
        else:
            HerpesVirus_d = DIR_LEFT
    if abs(HerpesVirus_x - Hiroshi_x) <= 40 and abs(HerpesVirus_y - Hiroshi_y) <= 40:
        idx = 2
        tmr = 0

def move_enemy6():  # Greenherpesvirus 움직이기4
    global idx, tmr, Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, Greenherpesvirus_a
    speed = 5
    if Greenherpesvirus_sd == -1:
        return
    if Greenherpesvirus_d == DIR_UP:
        if check_wall(Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, speed) == False:
            Greenherpesvirus_y = Greenherpesvirus_y - speed
        else:
            Greenherpesvirus_d = DIR_DOWN
    elif Greenherpesvirus_d == DIR_DOWN:
        if check_wall(Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, speed) == False:
            Greenherpesvirus_y = Greenherpesvirus_y + speed
        else:
            Greenherpesvirus_d = DIR_UP
    elif Greenherpesvirus_d == DIR_LEFT:
        if check_wall(Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, speed) == False:
            Greenherpesvirus_x = Greenherpesvirus_x - speed
        else:
            Greenherpesvirus_d = DIR_RIGHT
    elif Greenherpesvirus_d == DIR_RIGHT:
        if check_wall(Greenherpesvirus_x, Greenherpesvirus_y, Greenherpesvirus_d, speed) == False:
            Greenherpesvirus_x = Greenherpesvirus_x + speed
        else:
            Greenherpesvirus_d = DIR_LEFT
    if abs(Greenherpesvirus_x - Hiroshi_x) <= 40 and abs(Greenherpesvirus_y - Hiroshi_y) <= 40:
        idx = 2
        tmr = 0

def main():  # 메인 루프
    global idx, tmr, stage, score, nokori, se_Vaccine
    pygame.init()
    pygame.display.set_caption("백신찾기 겜")
    screen = pygame.display.set_mode((720, 540))
    clock = pygame.time.Clock()
    se_Vaccine = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Action\\Appendix1_sound_penpen_Vaccine.ogg")

    set_stage()
    set_chara_pos()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((720, 540), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((720, 540))

        key = pygame.key.get_pressed()
        tmr = tmr + 1
        draw_screen(screen)

        if idx == 0:  # 타이틀 화면
            screen.blit(img_title, [230, 80])
            if tmr % 10 < 5:
                draw_txt(screen, "Press SPACE !", 360, 380, 30, YELLOW)
            if key[K_SPACE] == 1:
                stage = 1
                score = 0
                nokori = 7 
                set_stage()
                set_chara_pos()
                idx = 1
                tmr = 0

        if idx == 1:  # 게임 플레이
            move_penpen(key)
            move_enemy()
            move_enemy2()
            move_enemy3()
            move_enemy4()
            move_enemy5()
            move_enemy6()
            if Vaccine == 0:
                idx = 4
                tmr = 0
            if tmr == 1:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Action\\Appendix1_sound_penpen_bgm.ogg")
                pygame.mixer.music.play(-1)

        if idx == 2:  # 적에게 당했다
            draw_txt(screen, "MISS", 360, 270, 40, ORANGE)
            if tmr == 1: #tmr 값이 1이면
                pygame.mixer.music.stop()
                nokori = nokori - 1 #잔여 수 1 감소
            if tmr == 5:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Action\\Appendix1_sound_penpen_miss.ogg")
                pygame.mixer.music.play(0)
            if tmr == 50: #tmr 값이 50이면 
                if nokori == 0: #잔여수가 0이면
                    idx = 3
                    tmr = 0
                else:
                    set_chara_pos()
                    idx = 1
                    tmr = 0

        if idx == 3:  # 게임 오버
            draw_txt(screen, "GAME OVER", 360, 270, 40, RED)
            if tmr == 50:
                idx = 0

        if idx == 4:  # 스테이지 클리어
            if stage < 6:
                draw_txt(screen, "STAGE CLEAR", 360, 270, 40, PINK)
            else:
                draw_txt(screen, "ALL STAGE CLEAR!", 360, 270, 40, VIOLET)
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr == 5:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Action\\Appendix1_sound_penpen_clear.ogg")
                pygame.mixer.music.play(0)
            if tmr == 50:
                if stage < 6:
                    stage = stage + 1
                    set_stage()
                    set_chara_pos()
                    idx = 1
                    tmr = 0
                else:
                    idx = 5
                    tmr = 0

        if idx == 5:  # 엔딩
            if tmr < 60: #tmr 값이 60보다 작으면
                xr = 8 * tmr #타원 반지름 계산
                yr = 6 * tmr
                pygame.draw.ellipse(screen, BLACK, [360 - xr, 270 - yr, xr * 2, yr * 2]) #검은색 타원그림
            else:
                pygame.draw.rect(screen, BLACK, [0, 0, 720, 540]) #화면을 검은 색으로 칠함
                screen.blit(img_ending, [360 - 120, 300 - 80]) #엔딩 화면 표시
                draw_txt(screen, "Congratulations!", 360, 160, 40, BLINK[tmr % 6])
            if tmr == 300: 
                idx = 0

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()