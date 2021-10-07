import pygame
import sys
import math
import random
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 224, 0)
GREEN = (0, 255, 0)

idx = 0
tmr = 0
laps = 0 #주행 바퀴 관리 변수
rec = 0 #주행 시간 측정 변수
recbk = 0 #랩 타임 계산용 변수
se_crash = None #충돌 시 사용할 효과음 로딩 변수
mycar = 0 #차종 선택 관리 변수

DATA_LR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 2, 1, 0, 2, 4, 2, 4, 2, 0, 0, 0, -2, -2, -4, -4, -2, -1, 0, 0, 0, 0, 0, 0, 0] #도로 커브 생성 기본 데이터
DATA_UD = [0, 0, 1, 2, 3, 2, 1, 0, -2, -4, -2, 0, 0, 0, 0, 0, -1, -2, -3, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 3, 0, -6, 6, 0] #도로 기복 생성 기본 데이터
CLEN = len(DATA_LR) #위 데이터의 엘리먼트 수를 대입한 상수

BOARD = 120 #도로를 그리 판 수 지정 상수
CMAX = BOARD * CLEN #코스 길이 지정 상수
curve = [0] * CMAX #도로 커브 방향 관리 리스트
updown = [0] * CMAX #도로 기복 관리 리스트
object_left = [0] * CMAX #도로 왼쪽 물체 번호 관리 리스트
object_right = [0] * CMAX #도로 오른쪽 물체 관리 리스트

CAR = 20 #차량수 지정 함수
car_x = [0] * CAR #차량 가로 방향 좌표 관리 리스트
car_y = [0] * CAR #차량 코스 상 위치 관리 리스트
car_lr = [0] * CAR #차량 좌우 방향 관리 리스트
car_spd = [0] * CAR #차량 속도 관리 리스트
PLCAR_Y = 10  # 플레이어 차량 표시 위치, 가장 가까운 도로(화면 아래)가 0

LAPS = 4 #골까지의 바퀴 수
laptime = ["0'00.00"] * LAPS #랩 타임 표시용 리스트 


def make_course():
    for i in range(CLEN):
        lr1 = DATA_LR[i] #커브 데이터 lr1에 대입
        lr2 = DATA_LR[(i + 1) % CLEN] #다음 커브 데이터를 lr2에 대입
        ud1 = DATA_UD[i] #기복 데이터를 ud1에 대입
        ud2 = DATA_UD[(i + 1) % CLEN] #기복 데이터를  ud2에 대입
        for j in range(BOARD): 
            pos = j + BOARD * i #리스트 인덱스 계산, pos에 대입
            curve[pos] = lr1 * (BOARD - j) / BOARD + lr2 * j / BOARD #도로 커브 방향 계산 대입
            updown[pos] = ud1 * (BOARD - j) / BOARD + ud2 * j / BOARD #도로 기복 계산 대입
            if j == 60: #반복 변수 j가 60이면
                object_right[pos] = 1  # 간판설치(도로 오른쪽)
            if i % 8 < 7: # 반복 변수 i%8<7이면
                if j % 12 == 0: #j%12가 0이면
                    object_left[pos] = 2  # 야자 나무(도로 왼쪽)
            else:
                if j % 20 == 0: # j* 12가 6이면
                    object_left[pos] = 3  # 요트(도로 왼쪽)
            if j % 12 == 6: #j % 12가 6이면
                object_left[pos] = 9  # 바다(왼쪽)


def time_str(val): #** ** **시간문자 생성 함수
    sec = int(val)  # 인수를 초 단위 정수로 변환, 인수를 초 단위 정수로 변환, sec에 대입
    ms = int((val - sec) * 100)  # 소수 부분, 소수 이하 값을 ms에 대입
    mi = int(sec / 60)  # 분을 mi에 대입
    return "{}'{:02}.{:02}".format(mi, sec % 60, ms) #** ** **문자열 반환시킴


def draw_obj(bg, img, x, y, sc): #좌표와 스케일을 받아, 물체를 그리는 함수 scale
    img_rz = pygame.transform.rotozoom(img, 0, sc) #확대 축소한 이미지 생성
    w = img_rz.get_width() #w에 이미지 폭 대입
    h = img_rz.get_height() #H에 이미지 높이 대입
    bg.blit(img_rz, [x - w / 2, y - h]) #이미지 그리기


def draw_shadow(bg, x, y, siz): #그림자 표시 함수
    shadow = pygame.Surface([siz, siz / 4]) #그릴 화면(surface) 준비
    shadow.fill(RED) #해당 화면을 빨간색으로 채움
    shadow.set_colorkey(RED)  # Surface 투과색 설정
    shadow.set_alpha(128)  # Surface 투명도 설정
    pygame.draw.ellipse(shadow, BLACK, [0, 0, siz, siz / 4]) #surface에 검은색 타원 그림 vertical
    bg.blit(shadow, [x - siz / 2, y - siz / 4]) #타원을 그린,surface를 게임 화면에 전송


def init_car(): #차량 관리 리스트 초기값 대입 함수
    for i in range(1, CAR): #반복 com 차량의
        car_x[i] = random.randint(50, 750) #가로 방향 좌표 무작위로 설정
        car_y[i] = random.randint(200, CMAX - 200) #코스 상 위치 무작위 결정
        car_lr[i] = 0 #좌우 움직임 0대입(정면을 향한다)
        car_spd[i] = random.randint(100, 200) #속도 무작위 결정
    car_x[0] = 400 #플레이어 차량 거로 방향 화면 중앙
    car_y[0] = 0 #플레이어 차량 코스 상 위치 초가화
    car_lr[0] = 0 #플레이어 차량 방향 0대입
    car_spd[0] = 0 #플레이어 차량 속도 0대입


def drive_car(key):  # 플레이어 차량 조작 및 제어
    global idx, tmr, laps, recbk
    if key[K_LEFT] == 1: #왼쪽 방향 키를 눌렀다면
        if car_lr[0] > -3: #방향이 -3보다 크다면
            car_lr[0] -= 1 #방향 -1(왼쪽으로 회전)
        car_x[0] = car_x[0] + (car_lr[0] - 3) * car_spd[0] / 100 - 5 #차량 가로 방향 좌표 
    elif key[K_RIGHT] == 1: #오론쪽 방향 키를 눌렀다면
        if car_lr[0] < 3: #방향이 3보다 작다면
            car_lr[0] += 1 #방향 +1
        car_x[0] = car_x[0] + (car_lr[0] + 3) * car_spd[0] / 100 + 5 #차량 가로 방향 좌표 계산
    else:
        car_lr[0] = int(car_lr[0] * 0.9) #정면 방향으로 가까이 이동

    if key[K_a] == 1:  # 악셀레이터
        car_spd[0] += 3 
    elif key[K_z] == 1:  # 브레이크
        car_spd[0] -= 10
    else:
        car_spd[0] -= 0.25

    if car_spd[0] < 0: #속도가 0 미만이라면
        car_spd[0] = 0 #속도에 0 대입
    if car_spd[0] > 320: #속도가 320을 넘으면
        car_spd[0] = 320 #속도가 320 대입

    car_x[0] -= car_spd[0] * curve[int(car_y[0] + PLCAR_Y) % CMAX] / 50 #차량 속도와 도로 커브에서 가로 방향 좌표 계산
    if car_x[0] < 0: #왼쪽 도로 끝에 닿았다면
        car_x[0] = 0 #가로 방향 좌표에 0대입
        car_spd[0] *= 0.9 #차량 감속
    if car_x[0] > 800: #오른쪽 도로 끝에 닿았다면
        car_x[0] = 800 #가로 방향 좌표에 800대입
        car_spd[0] *= 0.9 #차량 감속

    car_y[0] = car_y[0] + car_spd[0] / 100 #차량 속도에서 코스 상 위치 계산
    if car_y[0] > CMAX - 1: #코스 종점을 넘었다면
        car_y[0] -= CMAX #코스를 시작으로 되돌림.
        laptime[laps] = time_str(rec - recbk) #랩 타임 계산 후 대입
        recbk = rec #현재 타임 증가
        laps += 1 #완주 횟수 1증가
        if laps == LAPS: #완주 횟수가 LAPS와 같다면
            idx = 3
            tmr = 0


def move_car(cs):  # COM 차량 제어
    for i in range(cs, CAR): #반복해서 모든 차량 처리
        if car_spd[i] < 100: #속도가 100보가 작으면
            car_spd[i] += 3 #속도 증가
        if i == tmr % 120: #일정 시간 별로
            car_lr[i] += random.choice([-1, 0, 1]) #방향을 무작위로 변경
            if car_lr[i] < -3: car_lr[i] = -3 #방향이 -3미만이면 -3대입
            if car_lr[i] > 3: car_lr[i] = 3 #방향이 3초과면 3대입
        car_x[i] = car_x[i] + car_lr[i] * car_spd[i] / 100 #차량 방향, 속도에서 가로 좌표 계산
        if car_x[i] < 50: #왼쪽 길 끝에 가깝다면
            car_x[i] = 50 #그 이상 움직이지 않도록
            car_lr[i] = int(car_lr[i] * 0.9) #정면쪽으로 이동
        if car_x[i] > 750: #오른쪽 길 끝에 가깝다면
            car_x[i] = 750 #그이상 움직이지 않도록
            car_lr[i] = int(car_lr[i] * 0.9) #정면으로 이동
        car_y[i] += car_spd[i] / 100 #코스 중점을 넘었다면
        if car_y[i] > CMAX - 1: #코스 중점을 넘었다면
            car_y[i] -= CMAX #코스 시작으로 되돌림
        if idx == 2:  # 레이스 중 히트 체크
            cx = car_x[i] - car_x[0] #플레이어 차량과 가로 방향 거리
            cy = car_y[i] - (car_y[0] + PLCAR_Y) % CMAX #플레이어 차량과 크스 상 거리
            if -100 <= cx and cx <= 100 and -10 <= cy and cy <= 10: #이들이 범위 이내라면
                # 충돌 시 좌표 변화, 속도 변화 및 감속
                car_x[0] -= cx / 4 #플레이어 차량 가로로 이동
                car_x[i] += cx / 4 #com 차량 가로로 이동
                car_spd[0], car_spd[i] = car_spd[i] * 0.3, car_spd[0] * 0.3 #2개 차량 속도를 서로 바꿔 감속
                se_crash.play() #충돌음 출력


def draw_text(scrn, txt, x, y, col, fnt): #그림자 포함 문자열 표시 함수
    sur = fnt.render(txt, True, BLACK) #검은 문자열을 그릴 surface 생성
    x -= sur.get_width() / 2 #센터링 x좌표 계산
    y -= sur.get_height() / 2 #센터링 y좌표 계산
    scrn.blit(sur, [x + 2, y + 2]) #surface를 화면으로 전성
    sur = fnt.render(txt, True, col) #지정색으로 문자열 그린 surface 생성
    scrn.blit(sur, [x, y]) #surface를 화면으로 전송 vertical


def main():  # 메인 처리
    global idx, tmr, laps, rec, recbk, se_crash, mycar
    pygame.init()
    pygame.display.set_caption("Python Racer")
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    fnt_s = pygame.font.Font(None, 40)
    fnt_m = pygame.font.Font(None, 50)
    fnt_l = pygame.font.Font(None, 120)

    img_title = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\title.png").convert_alpha()
    img_bg = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\bg.png").convert()
    img_sea = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\sea.png").convert_alpha()
    img_obj = [
        None,
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\board.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\yashi.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\yacht.png").convert_alpha()
    ]
    img_car = [
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car00.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car01.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car02.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car03.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car04.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car05.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car06.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car10.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car11.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car12.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car13.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car14.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car15.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car16.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car20.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car21.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car22.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car23.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car24.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car25.png").convert_alpha(),
        pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_Racing\\car26.png").convert_alpha()
    ]

    se_crash = pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Racing\\Chapter11_sound_pr_crash.ogg")  # SE 로딩

    # 도로 판의 기본 형태 계산
    BOARD_W = [0] * BOARD #판의 폭을 대입하는 리스트
    BOARD_H = [0] * BOARD #판의 높이를 대입하는 리스트
    BOARD_UD = [0] * BOARD #판의 기복 값을 대입하는 리스트
    for i in range(BOARD):
        BOARD_W[i] = 10 + (BOARD - i) * (BOARD - i) / 12 #폭 계산
        BOARD_H[i] = 3.4 * (BOARD - i) / BOARD #높이 계산
        BOARD_UD[i] = 2 * math.sin(math.radians(i * 1.5)) #기복을 삼각함수로 계산

    make_course()
    init_car()

    vertical = 0 #배경 가로 방향 위치 관리 변수

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((800, 600), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((800, 600))
        tmr += 1

        # 화면에 그릴 도로의 X 좌표와 높낮이 계산
        di = 0 #도로커브 방향 계산 변수
        ud = 0 #도로 기복 계산 변수
        board_x = [0] * BOARD #판의 x좌표를 계산하는 리스트
        board_ud = [0] * BOARD #판의 높낮이를 계산하는 리스트
        for i in range(BOARD):
            di += curve[int(car_y[0] + i) % CMAX] #커브 데이터에서 도로 굽기 계산
            ud += updown[int(car_y[0] + i) % CMAX] #기복 데이터에서 도로 기복 계산
            board_x[i] = 400 - BOARD_W[i] * car_x[0] / 800 + di / 2 #판의 x좌표를 계산해서 대입
            board_ud[i] = ud / 30 #판의 높낮이 계산해서 대입

        horizon = 400 + int(ud / 3)  # 지평선 좌표 계산
        sy = horizon  # 도로를 그리기 시작할 위치

        vertical = vertical - int(car_spd[0] * di / 8000)  # 베경 수직 위치
        if vertical < 0: #0미만이면
            vertical += 800 #+800
        if vertical >= 800: #800이상이면
            vertical -= 800 #-800

        # 필드 그리기
        screen.fill((0, 0, 0))  # 겅은색 색상
        screen.blit(img_bg, [vertical - 800, horizon - 400])
        screen.blit(img_bg, [vertical, horizon - 400])
        screen.blit(img_sea, [board_x[BOARD - 1] - 780, sy])  # 가장 먼 오로라

        # 그리기 데이터를 기초로 도로 그리기
        for i in range(BOARD - 1, 0, -1): #반복해서 도로의 판 그리기
            ux = board_x[i] #사다리꼴 윗변 x좌표 대입
            uy = sy - BOARD_UD[i] * board_ud[i] #윗변 y좌표 대입
            uw = BOARD_W[i] #윗변의 폭 대입
            sy = sy + BOARD_H[i] * (600 - horizon) / 200 #사다리꼴을 그릴 y좌표 대입
            bx = board_x[i - 1] #아랫변 x좌표 계산
            by = sy - BOARD_UD[i - 1] * board_ud[i - 1] #아랫변 폭 대입
            bw = BOARD_W[i - 1] #아랫변 폭 대입
            col = (160, 160, 160)
            if int(car_y[0] + i) % CMAX == PLCAR_Y + 10:  # 빨강색 선 위치
                col = (192, 0, 0)
            pygame.draw.polygon(screen, col, [[ux, uy], [ux + uw, uy], [bx + bw, by], [bx, by]]) #도로판 그림

            if int(car_y[0] + i) % 10 <= 4:  # 좌우 노랑색 선
                pygame.draw.polygon(screen, YELLOW, [[ux, uy], [ux + uw * 0.02, uy], [bx + bw * 0.02, by], [bx, by]])
                pygame.draw.polygon(screen, YELLOW, [[ux + uw * 0.98, uy], [ux + uw, uy], [bx + bw, by], [bx + bw * 0.98, by]])
            if int(car_y[0] + i) % 20 <= 10:  # 흰색 선
                pygame.draw.polygon(screen, WHITE, [[ux + uw * 0.24, uy], [ux + uw * 0.26, uy], [bx + bw * 0.26, by], [bx + bw * 0.24, by]])
                pygame.draw.polygon(screen, WHITE, [[ux + uw * 0.49, uy], [ux + uw * 0.51, uy], [bx + bw * 0.51, by], [bx + bw * 0.49, by]])
                pygame.draw.polygon(screen, WHITE, [[ux + uw * 0.74, uy], [ux + uw * 0.76, uy], [bx + bw * 0.76, by], [bx + bw * 0.74, by]])

            scale = 1.5 * BOARD_W[i] / BOARD_W[0]
            obj_l = object_left[int(car_y[0] + i) % CMAX]  # 도로 왼쪽 물체
            if obj_l == 2:  # 야자 나무
                draw_obj(screen, img_obj[obj_l], ux - uw * 0.05, uy, scale)
            if obj_l == 3:  # 요트
                draw_obj(screen, img_obj[obj_l], ux - uw * 0.5, uy, scale)
            if obj_l == 9:  # 바다
                screen.blit(img_sea, [ux - uw * 0.5 - 780, uy])
            obj_r = object_right[int(car_y[0] + i) % CMAX]  # 도로 오른쪽 물체
            if obj_r == 1:  # 간판
                draw_obj(screen, img_obj[obj_r], ux + uw * 1.3, uy, scale)

            for c in range(1, CAR):  # COM 차량
                if int(car_y[c]) % CMAX == int(car_y[0] + i) % CMAX:
                    lr = int(4 * (car_x[0] - car_x[c]) / 800)  # 플레이어가 보는 COM 차량의 방향
                    if lr < -3: lr = -3
                    if lr > 3: lr = 3
                    draw_obj(screen, img_car[(c % 3) * 7 + 3 + lr], ux + car_x[c] * BOARD_W[i] / 800, uy, 0.05 + BOARD_W[i] / BOARD_W[0])

            if i == PLCAR_Y:  # 플레이어 차량
                draw_shadow(screen, ux + car_x[0] * BOARD_W[i] / 800, uy, 200 * BOARD_W[i] / BOARD_W[0])
                draw_obj(screen, img_car[3 + car_lr[0] + mycar * 7], ux + car_x[0] * BOARD_W[i] / 800, uy, 0.05 + BOARD_W[i] / BOARD_W[0])

        draw_text(screen, str(int(car_spd[0])) + "km/h", 680, 30, RED, fnt_m)
        draw_text(screen, "lap {}/{}".format(laps, LAPS), 100, 30, WHITE, fnt_m)
        draw_text(screen, "time " + time_str(rec), 100, 80, GREEN, fnt_s)
        for i in range(LAPS):
            draw_text(screen, laptime[i], 80, 130 + 40 * i, YELLOW, fnt_s)

        key = pygame.key.get_pressed()

        if idx == 0:
            screen.blit(img_title, [120, 120])
            draw_text(screen, "[A] Start game", 400, 320, WHITE, fnt_m)
            draw_text(screen, "[S] Select your car", 400, 400, WHITE, fnt_m)
            move_car(0)
            if key[K_a] != 0:
                init_car()
                idx = 1
                tmr = 0
                laps = 0
                rec = 0
                recbk = 0
                for i in range(LAPS):
                    laptime[i] = "0'00.00"
            if key[K_s] != 0:
                idx = 4

        if idx == 1:
            n = 3 - int(tmr / 60)
            draw_text(screen, str(n), 400, 240, YELLOW, fnt_l)
            if tmr == 179:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Racing\\Chapter11_sound_pr_bgm.ogg")
                pygame.mixer.music.play(-1)
                idx = 2
                tmr = 0

        if idx == 2:
            if tmr < 60:
                draw_text(screen, "Go!", 400, 240, RED, fnt_l)
            rec = rec + 1 / 60
            drive_car(key)
            move_car(1)

        if idx == 3:
            if tmr == 1:
                pygame.mixer.music.stop()
            if tmr == 30:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_Racing\\Chapter11_sound_pr_goal.ogg")
                pygame.mixer.music.play(0)
            draw_text(screen, "GOAL!", 400, 240, GREEN, fnt_l)
            car_spd[0] = car_spd[0] * 0.96
            car_y[0] = car_y[0] + car_spd[0] / 100
            move_car(1)
            if tmr > 60 * 8:
                idx = 0

        if idx == 4:
            move_car(0)
            draw_text(screen, "Select your car", 400, 160, WHITE, fnt_m)
            for i in range(3):
                x = 160 + 240 * i
                y = 300
                col = BLACK
                if i == mycar:
                    col = (0, 128, 255)
                pygame.draw.rect(screen, col, [x - 100, y - 80, 200, 160])
                draw_text(screen, "[" + str(i + 1) + "]", x, y - 50, WHITE, fnt_m)
                screen.blit(img_car[3 + i * 7], [x - 100, y - 20])
            draw_text(screen, "[Enter] OK!", 400, 440, GREEN, fnt_m)
            if key[K_1] == 1:
                mycar = 0
            if key[K_2] == 1:
                mycar = 1
            if key[K_3] == 1:
                mycar = 2
            if key[K_RETURN] == 1:
                idx = 0

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()