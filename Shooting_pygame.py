import pygame
import sys
import math
import random
from pygame.locals import *

BLACK = (0, 0, 0)
SILVER = (192, 208, 224)
RED = (255, 0, 0)
CYAN = (0, 224, 255)

# 이미지 로딩
img_galaxy = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\galaxy.png")
img_sship = [
pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\starship.png"),
pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\starship_l.png"),
pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\starship_r.png"),
pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\starship_burner.png")
]
img_weapon = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\bullet.png")
img_shield = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\shield.png")
img_enemy = [ 
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy0.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy1.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy2.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy3.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy4.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy_boss.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\enemy_boss_f.png")
]
img_explode = [ 
    None,
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\explosion1.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\explosion2.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\explosion3.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\explosion4.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\explosion5.png")
]
img_title = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\nebula.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Shooting\\logo.png")
]

# SE 로딩 변수
se_barrage = None #탄막 발사 시 사용할 SE 로딩 변수
se_damage = None #데미지 받을 시 사용할 SE 로딩 변수
se_explosion = None #보스 폭발 시 사용할 SE 로딩 변수
se_shot = None #탄환 발사 시 사용할 SE 로딩

idx = 0 
tmr = 0 
score = 0
hisco = 10000
new_record = False #최고 점수 생신용 플래그 변수.
bg_y = 0

ss_x = 0 #플레이어 기체 x좌표
ss_y = 0 #플레이어 기체 y 좌표
ss_d = 0 #플레이어 기체 기울기 변수
ss_shield = 0 #플레이어 체력
ss_muteki = 0 #플레이어 무적
key_spc = 0 #스페이스바
key_z = 0 #z키

MISSILE_MAX = 200 #플레이어가 발사한 최대 탄환 수 정의
msl_no = 0 #탄환 발사에 사용할 리스트 인덱스 변수
msl_f = [False] * MISSILE_MAX #탄환을 발사 중인지 관리 하는 플래그 
msl_x = [0] * MISSILE_MAX #탄환의 x좌표
msl_y = [0] * MISSILE_MAX #탄환의 y좌표
msl_a = [0] * MISSILE_MAX #탄환이 날아가는 각도 리스트

ENEMY_MAX = 100 #적 최대 수 정의
emy_no = 0 #적 등장 시 사용할 리스트
emy_f = [False] * ENEMY_MAX #적 등장 여부 관리 리스트
emy_x = [0] * ENEMY_MAX #적의 x 좌표
emy_y = [0] * ENEMY_MAX #y좌표
emy_a = [0] * ENEMY_MAX #탄환이 날아가는 각도
emy_type = [0] * ENEMY_MAX #적의 종류 
emy_speed = [0] * ENEMY_MAX #적의 스피드
emy_shield = [0] * ENEMY_MAX #적 체력
emy_count = [0] * ENEMY_MAX #적 움직임 등을 관리할 리스트

EMY_BULLET = 0 #적의 탄환 번호를 관리할 상수
EMY_ZAKO = 1 #적 일반 기체 번호를 관리할 상수
EMY_BOSS = 5 #보스 가체 번호를 관리할 상수
LINE_T = -80 #적이 나타나는 (사라지는) 위쪽 좌표
LINE_B = 800 #적이 나타나는 (사라지는) 아래쪽 좌표
LINE_L = -80 #적이 나타나는 (사라지는) 왼쪽 좌표
LINE_R = 1040 #적이 나타나는 (사라지는) 오른쪽 좌표

EFFECT_MAX = 100 #폭발 연출 최대 수 정의한다.
eff_no = 0 # 폭발 연출시 사용할 리스트 인덱스 
eff_p = [0] * EFFECT_MAX #폭발 연출 이미지 번호 리스트
eff_x = [0] * EFFECT_MAX #폭발 연출 x좌표 리스트
eff_y = [0] * EFFECT_MAX #폭발 연출 y좌표 리스트


def get_dis(x1, y1, x2, y2):  # 두 점 사이 거리 계산
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) #제곱한 값을 반환한다.


def draw_text(scrn, txt, x, y, siz, col):  # 입체적인 문자 표시
    fnt = pygame.font.Font(None, siz) #폰트 객체를 생성한다.
    cr = int(col[0] / 2) #빨간색 성분에서 어두운 값 계산
    cg = int(col[1] / 2) #초록색 성분에서 어두운 값 계산
    cb = int(col[2] / 2) #파란색 성분에서 어두운 값 계산
    sur = fnt.render(txt, True, (cr, cg, cb)) #어두운 색 문자열을 그린 Surface 생성
    x = x - sur.get_width() / 2 #중심선 표시 x좌표 계산
    y = y - sur.get_height() / 2 #중심선 표시 y좌표 계산
    scrn.blit(sur, [x + 1, y + 1]) #해당 Surface를 화면에 전송
    cr = col[0] + 128 #빨간색 성분에서 밝은 값 계산
    if cr > 255: cr = 255
    cg = col[1] + 128 #초록색 성분에서 밝은 값 계산
    if cg > 255: cg = 255
    cb = col[2] + 128 #파란색 성분에서 밝은 값 계산
    if cb > 255: cb = 255
    sur = fnt.render(txt, True, (cr, cg, cb)) #밝은 색 문자열을 그린 Surface 생성
    scrn.blit(sur, [x - 1, y - 1]) #해당 Surface를 화면에 전송
    sur = fnt.render(txt, True, col) #인수 색으로 문자열을 그린 Surface 생성
    scrn.blit(sur, [x, y]) #해당 surface를 화면에 전송시킨다.


def move_starship(scrn, key):  # 플레이어 기체 이동
    global idx, tmr, ss_x, ss_y, ss_d, ss_shield, ss_muteki, key_spc, key_z
    ss_d = 0
    if key[K_UP] == 1:
        ss_y = ss_y - 20
        if ss_y < 80:
            ss_y = 80
    if key[K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > 640:
            ss_y = 640
    if key[K_LEFT] == 1:
        ss_d = 1
        ss_x = ss_x - 20
        if ss_x < 40:
            ss_x = 40
    if key[K_RIGHT] == 1:
        ss_d = 2
        ss_x = ss_x + 20
        if ss_x > 920:
            ss_x = 920
    key_spc = (key_spc + 1) * key[K_SPACE] #스페이스 키를 누르는 동안 변수 값을 증가시킴
    if key_spc % 5 == 1: #스페이스 키를 처음 누른후 5프레임마다
        set_missile(0) #탄환 발사
        se_shot.play() #발사음 출력
    key_z = (key_z + 1) * key[K_z] #z키를 누르는 동안 변수 값 증가
    if key_z == 1 and ss_shield > 10: #1번 눌렀을때 체력이 10보다 크다면 
        set_missile(10) #탄만을 친다
        ss_shield = ss_shield - 7 #체력 감소
        se_barrage.play() #발사음 출력함.

    if ss_muteki % 2 == 0: #무적 상태에서 깜빡이기 위한 if구문
        scrn.blit(img_sship[3], [ss_x - 6, ss_y + 30 + (tmr % 3) * 2]) #엔진의 불꽃을 그린다
        scrn.blit(img_sship[ss_d], [ss_x - 37, ss_y - 48]) #플레이어 기체 그림

    if ss_muteki > 0: #무적 상태라면
        ss_muteki = ss_muteki - 1 #체력 감소
        return
    elif idx == 1: #무적 상태가 아니라면
        for i in range(ENEMY_MAX):  # 적 기체와 히트 체크
            if emy_f[i] == True: #적 기체 존재
                w = img_enemy[emy_type[i]].get_width()
                h = img_enemy[emy_type[i]].get_height()
                r = int((w + h) / 4 + (74 + 96) / 4) #히트 체크 거리 계산
                if get_dis(emy_x[i], emy_y[i], ss_x, ss_y) < r * r: #적 기체와 플레이어 기체 사이의 거리가 히트 체크 거리보다 작으면 
                    set_effect(ss_x, ss_y) #폭발 연출 설정
                    ss_shield = ss_shield - 10 #체력은 10감소
                    if ss_shield <= 0: #체력이 0보다 작거나 같다면
                        ss_shield = 0 #체력에 0 대입
                        idx = 2 #게임 오버로 떠남
                        tmr = 0
                    if ss_muteki == 0: #무적 상태가 아니라면
                        ss_muteki = 60 #무적 상태로 바꿈
                        se_damage.play() #대미지 효과음 출력
                    if emy_type[i] < EMY_BOSS: #접촉한 기체가 보스가 아니면
                        emy_f[i] = False #삭제 시킨다.


def set_missile(typ):  # 플레이어 기체 발사 탄환 설정
    global msl_no # 전역 변수 선언
    if typ == 0:  # 단발
        msl_f[msl_no] = True
        msl_x[msl_no] = ss_x #x좌표 대입(플레이어 기체 앞끝)
        msl_y[msl_no] = ss_y - 50 
        msl_a[msl_no] = 270
        msl_no = (msl_no + 1) % MISSILE_MAX #다음 설정을 위한 번호 계산
    if typ == 10:  # 탄막
        for a in range(160, 390, 10):
            msl_f[msl_no] = True
            msl_x[msl_no] = ss_x
            msl_y[msl_no] = ss_y - 50
            msl_a[msl_no] = a
            msl_no = (msl_no + 1) % MISSILE_MAX #다음 설정을 위한 번호 계산


def move_missile(scrn):  # 탄환 이동
    for i in range(MISSILE_MAX): #반복해서
        if msl_f[i] == True: #탄환이 발사된 상태라면
            msl_x[i] = msl_x[i] + 36 * math.cos(math.radians(msl_a[i]))
            msl_y[i] = msl_y[i] + 36 * math.sin(math.radians(msl_a[i]))
            img_rz = pygame.transform.rotozoom(img_weapon, -90 - msl_a[i], 1.0)
            scrn.blit(img_rz, [msl_x[i] - img_rz.get_width() / 2, msl_y[i] - img_rz.get_height() / 2])#탄환이미지 그리기
            if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i] > 960: #탄환이 화면 밖으로 나가면
                msl_f[i] = False #삭제


def bring_enemy():  # 적 기체 등장
    sec = tmr / 30 #게임 진행 시간(초 단위)을 sec에 대입
    if 0 < sec and sec < 25:  # 시작 후 25초 간
        if tmr % 15 == 0:
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)  # 적 1 , 8= 스피드 1= 방어력
    if 30 < sec and sec < 55:  # 30~55초
        if tmr % 10 == 0:
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO + 1, 20, 1)  # 적 2 
    if 60 < sec and sec < 85:  # 60~85초
        if tmr % 15 == 0:
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)  # 적 3
    if 90 < sec and sec < 115:  # 90~115초
        if tmr % 20 == 0:
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)  # 적 4
    if 120 < sec and sec < 145:  # 120~145초, 2종류
        if tmr % 20 == 0:
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)  # 적 1
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)  # 적 3
    if 150 < sec and sec < 175:  # 150~175초, 2종류
        if tmr % 20 == 0:
            set_enemy(random.randint(20, 940), LINE_B, 270, EMY_ZAKO, 8, 1)  # 적 1 아래에서 위로
            set_enemy(random.randint(20, 940), LINE_T, random.randint(70, 110), EMY_ZAKO + 1, 12, 1)  # 적 2
    if 180 < sec and sec < 205:  # 180~205초, 2종류
        if tmr % 20 == 0:
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)  # 적 3
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)  # 적 4
    if 210 < sec and sec < 235:  # 210~235초, 2종류
        if tmr % 20 == 0:
            set_enemy(LINE_L, random.randint(40, 680), 0, EMY_ZAKO, 12, 1)  # 적 1
            set_enemy(LINE_R, random.randint(40, 680), 180, EMY_ZAKO + 1, 18, 1)  # 적 2
    if 240 < sec and sec < 265:  # 240~265초, 총공격
        if tmr % 30 == 0:
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO, 8, 1)  # 적 1
            set_enemy(random.randint(20, 940), LINE_T, 90, EMY_ZAKO + 1, 12, 1)  # 적 2
            set_enemy(random.randint(100, 860), LINE_T, random.randint(60, 120), EMY_ZAKO + 2, 6, 3)  # 적 3
            set_enemy(random.randint(100, 860), LINE_T, 90, EMY_ZAKO + 3, 12, 2)  # 적 4

    if tmr == 30 * 270:  # 보스 출현
        set_enemy(480, -210, 90, EMY_BOSS, 4, 200)


def set_enemy(x, y, a, ty, sp, sh):  # 적 기체 설정
    global emy_no #전역 변수 선언
    while True: #무한 반복
        if emy_f[emy_no] == False: #리스트가 비어있다면
            emy_f[emy_no] = True #플래그 설정
            emy_x[emy_no] = x #x좌표 대입
            emy_y[emy_no] = y#y좌표 대입
            emy_a[emy_no] = a#각도 대입
            emy_type[emy_no] = ty#적 종류 대입
            emy_speed[emy_no] = sp #적 속도 대입
            emy_shield[emy_no] = sh # 적 체력 대입
            emy_count[emy_no] = 0 #움직임 등을 관리하는 리스트에 0대입
            break #반복 이탈
        emy_no = (emy_no + 1) % ENEMY_MAX #다음 설정을 위한 번호 계산 


def move_enemy(scrn):  # 적 기체 이동
    global idx, tmr, score, hisco, new_record, ss_shield
    for i in range(ENEMY_MAX):
        if emy_f[i] == True: #적 기체가 존재한다면
            ang = -90 - emy_a[i] #ang에 이미지 회전 각도 대입
            png = emy_type[i] #png에 이미지 번호 대입 
            if emy_type[i] < EMY_BOSS:  # 적 일반 기체 이동
                emy_x[i] = emy_x[i] + emy_speed[i] * math.cos(math.radians(emy_a[i])) #x좌표 변화
                emy_y[i] = emy_y[i] + emy_speed[i] * math.sin(math.radians(emy_a[i])) #y좌표 변화
                if emy_type[i] == 4:  # 진행 방향을 변경하는 적
                    emy_count[i] = emy_count[i] + 1 #emy_count 증가
                    ang = emy_count[i] * 10 #이미지 회전 각도 계산
                    if emy_y[i] > 240 and emy_a[i] == 90: #y좌표가 240 보다 크다면 
                        emy_a[i] = random.choice([50, 70, 110, 130]) #무작위로 방향 변경
                        set_enemy(emy_x[i], emy_y[i], 90, EMY_BULLET, 6, 0) #탄환 발사
                if emy_x[i] < LINE_L or LINE_R < emy_x[i] or emy_y[i] < LINE_T or LINE_B < emy_y[i]:#화면 상하좌우 벗어났다면
                    emy_f[i] = False#적기체 소멸
            else:  # 보스 기체
                if emy_count[i] == 0: #emy_count 값이 0이면
                    emy_y[i] = emy_y[i] + 2 #아래 쪽으로 내려 보냄
                    if emy_y[i] >= 200: #아래쪽까지 왔다면
                        emy_count[i] = 1 #왼쪽 방향으로 이동
                elif emy_count[i] == 1: #emy_count 값이 1이면
                    emy_x[i] = emy_x[i] - emy_speed[i] #왼쪽으로 이동
                    if emy_x[i] < 200: #왼쪽까지 왔다면 
                        for j in range(0, 10): #반복한다
                            set_enemy(emy_x[i], emy_y[i] + 80, j * 20, EMY_BULLET, 6, 0) #탄환발사
                        emy_count[i] = 2 #오른쪽으로 이동한다.
                else: #emy_count가 0, 1이 아니라면
                    emy_x[i] = emy_x[i] + emy_speed[i] #오른쪽으로 이동
                    if emy_x[i] > 760: #오른쪽으로 왔다가
                        for j in range(0, 10): #반복
                            set_enemy(emy_x[i], emy_y[i] + 80, j * 20, EMY_BULLET, 6, 0)#빵야
                        emy_count[i] = 1 #왼쪽으로 이동
                if emy_shield[i] < 100 and tmr % 30 == 0: #실드 값 <100일 시 해당 타이밍에
                    set_enemy(emy_x[i], emy_y[i] + 80, random.randint(60, 120), EMY_BULLET, 6, 0)#빵야빵야

            if emy_type[i] != EMY_BULLET:  # 플레이어 기체 발사 탄환과 히트 체크
                w = img_enemy[emy_type[i]].get_width()
                h = img_enemy[emy_type[i]].get_height()
                r = int((w + h) / 4) + 12 #히트 체크에 사용할 거리 계산
                er = int((w + h) / 4) #폭발 연출 표시 값
                for n in range(MISSILE_MAX):
                    if msl_f[n] == True and get_dis(emy_x[i], emy_y[i], msl_x[n], msl_y[n]) < r * r: #플레이어 기체 탄환과 접촉 여부판단
                        msl_f[n] = False#탄환 삭제
                        set_effect(emy_x[i] + random.randint(-er, er), emy_y[i] + random.randint(-er, er)) #폭발 임펙트
                        if emy_type[i] == EMY_BOSS:  # 보스 기체 깜빡임 처리
                            png = emy_type[i] + 1 #플래시용 이미지 번호 
                        emy_shield[i] = emy_shield[i] - 1 #적 체력 감소
                        score = score + 100 #점수 증가~
                        if score > hisco: #최고 점수를 뛰어넘으면
                            hisco = score #최고 점수는 그냥 점수로 바뀐다 갱신
                            new_record = True #최고 점수 플래그
                        if emy_shield[i] == 0: #적 게체를 격추했다면
                            emy_f[i] = False #적 기체 삭제
                            if ss_shield < 100: #플레이어 실드량 <100
                                ss_shield = ss_shield + 1 #실드량 증가
                            if emy_type[i] == EMY_BOSS and idx == 1:  # 보스를 격추시키면 클리어
                                idx = 3
                                tmr = 0
                                for j in range(10):
                                    set_effect(emy_x[i] + random.randint(-er, er), emy_y[i] + random.randint(-er, er)) #보스 폭발 연출
                                se_explosion.play() #폭발 브금 

            img_rz = pygame.transform.rotozoom(img_enemy[png], ang, 1.0) #적 기체를 회전시킨 이미지 생성
            scrn.blit(img_rz, [emy_x[i] - img_rz.get_width() / 2, emy_y[i] - img_rz.get_height() / 2])


def set_effect(x, y):  # 폭발 설정
    global eff_no 
    eff_p[eff_no] = 1 #폭발 연출 이미지 번호 대입
    eff_x[eff_no] = x
    eff_y[eff_no] = y
    eff_no = (eff_no + 1) % EFFECT_MAX


def draw_effect(scrn):  # 폭발 연출
    for i in range(EFFECT_MAX):
        if eff_p[i] > 0: #폭발 연출 중이면
            scrn.blit(img_explode[eff_p[i]], [eff_x[i] - 48, eff_y[i] - 48]) #폭발 연출 표시
            eff_p[i] = eff_p[i] + 1 #eff_p 값 1증가
            if eff_p[i] == 6: #eff_p가 6이 되었다면
                eff_p[i] = 0 #eff_p에 0 대입 후 연출 종류


def main():  # 메인 루프
    global idx, tmr, score, new_record, bg_y, ss_x, ss_y, ss_d, ss_shield, ss_muteki
    global se_barrage, se_damage, se_explosion, se_shot

    pygame.init()
    pygame.display.set_caption("Galaxy Lancer")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    se_barrage = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_barrage.ogg")
    se_damage = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_damage.ogg")
    se_explosion = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_explosion.ogg")
    se_shot = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_shot.ogg")

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((960, 720), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        # 배경 스크롤
        bg_y = (bg_y + 16) % 720
        screen.blit(img_galaxy, [0, bg_y - 720]) #배경그리기 위쪽
        screen.blit(img_galaxy, [0, bg_y]) #아래쪽

        key = pygame.key.get_pressed() #키에 모든 키상태를 대입한다.

        if idx == 0:  # 타이틀
            img_rz = pygame.transform.rotozoom(img_title[0], -tmr % 360, 1.0) #로고 뒤 회전하는 소용돌이 이미지
            screen.blit(img_rz, [480 - img_rz.get_width() / 2, 280 - img_rz.get_height() / 2]) #이미지 화면 그리기
            screen.blit(img_title[1], [345, 150]) #갤럭시 로그 그리기
            draw_text(screen, "Press [SPACE] to start!", 480, 600, 50, SILVER)
            if key[K_SPACE] == 1:
                idx = 1
                tmr = 0
                score = 0
                new_record = False
                ss_x = 480
                ss_y = 600
                ss_d = 0
                ss_shield = 100
                ss_muteki = 0
                for i in range(ENEMY_MAX):
                    emy_f[i] = False
                for i in range(MISSILE_MAX):
                    msl_f[i] = False
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_bgm.ogg")
                pygame.mixer.music.play(-1)

        if idx == 1:  # 게임 플레이 중
            move_starship(screen, key)
            move_missile(screen)
            bring_enemy()
            move_enemy(screen)

        if idx == 2:  # 게임 오버
            move_missile(screen)
            move_enemy(screen)
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr <= 90:
                if tmr % 5 == 0:
                    set_effect(ss_x + random.randint(-60, 60), ss_y + random.randint(-60, 60))
                if tmr % 10 == 0:
                    se_damage.play()
            if tmr == 120:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_gameover.ogg")
                pygame.mixer.music.play(0)
            if tmr > 120:
                draw_text(screen, "GAME OVER", 480, 300, 80, RED)
                if new_record == True:
                    draw_text(screen, "NEW RECORD " + str(hisco), 480, 400, 60, CYAN)
            if tmr == 400:
                idx = 0
                tmr = 0

        if idx == 3:  # 게임 클리어
            move_starship(screen, key)
            move_missile(screen)
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr < 30 and tmr % 2 == 0:
                pygame.draw.rect(screen, (192, 0, 0), [0, 0, 960, 720])
            if tmr == 120:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Shooting\\Chapter8_sound_gl_gameclear.ogg")
                pygame.mixer.music.play(0)
            if tmr > 120:
                draw_text(screen, "GAME CLEAR", 480, 300, 80, SILVER)
                if new_record == True:
                    draw_text(screen, "NEW RECORD " + str(hisco), 480, 400, 60, CYAN)
            if tmr == 400:
                idx = 0
                tmr = 0

        draw_effect(screen)  # 폭발 연출
        draw_text(screen, "SCORE " + str(score), 200, 30, 50, SILVER)
        draw_text(screen, "HISCORE " + str(hisco), 760, 30, 50, CYAN)
        if idx != 0:  # 실드 표시
            screen.blit(img_shield, [40, 680])
            pygame.draw.rect(screen, (64, 32, 32), [40 + ss_shield * 4, 680, (100 - ss_shield) * 4, 12])

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
