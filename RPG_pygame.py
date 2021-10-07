import pygame
import sys
import random
from pygame.locals import *


# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
BLINK = [(224, 255, 255), (192, 240, 255), (128, 224, 255), (64, 192, 255), (128, 224, 255), (192, 240, 255)] #반짝이는 연출

# 이미지 로딩
imgTitle = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\title.png")
imgWall = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\wall.png")
imgWall2 = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\wall2.png")
imgDark = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\dark.png")
imgPara = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\parameter.png")
imgBtlBG = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\btlbg.png")
imgEnemy = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\enemy0.png")
imgItem = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\potion.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\Black_Diamond.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\spoiled.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\fish.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\meat.png")
]
imgFloor = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\floor.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\tbox.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\cocoon.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\stairs.png")
]
imgPlayer = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr0.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr1.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr2.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr3.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr4.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr5.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr6.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr7.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\mychr8.png")
]
imgEffect = [
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_a.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_b.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_c.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_d.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_e.png"),
    pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\effect_f.png")
]

# 변수 선언
speed = 2
idx = 0
tmr = 0
floor = 0
fl_max = 1 #도달 층수 값 
welcome = 0

pl_x = 0
pl_y = 0
pl_d = 0 #플레이어의 방향
pl_a = 0 #플레이어의 애니메이션 패턴
pl_lifemax = 0
pl_life = 0
pl_str = 0#플레이어의 공격력
food = 0
potion = 0
BlackDiamond = 0
treasure = 0

emy_name = ""
emy_lifemax = 0
emy_life = 0
emy_str = 0
emy_x = 0
emy_y = 0
emy_step = 0
emy_blink = 0


dmg_eff = 0
btl_cmd = 0

COMMAND = ["[A] Attack", "[P]otion", "[B]lack_Diamond", "[R]un"] 
TRE_NAME = ["Potion", "Black_Diamond", "Food spoiled.", "Food +20", "Food +100"]
EMY_NAME = [ 
   "Spiders", "Skeleton", "Zombies", "Creepers", "Phantom", "Aooni", "Hirobin", "Born Dragon", "Phoenix!!",
    "\"The devil!\""
]

MAZE_W = 11 #가로 방향 길이 
MAZE_H = 9  #세로 방향 길이
maze = []   #미로 데이터 관리 리스트
for y in range(MAZE_H): #y 미로 세로에 관한 반복
    maze.append([0] * MAZE_W) #가로의 값은 초기화 처리한다.

DUNGEON_W = MAZE_W * 3
DUNGEON_H = MAZE_H * 3 
dungeon = [] #던전 리스트 함수
for y in range(DUNGEON_H): #던전 값에 대한 반복
    dungeon.append([0] * DUNGEON_W) #가로의 값은 초기화 한다.

def make_dungeon():  # 던전 자동 생성
    XP = [0, 1, 0, -1] #벽그리기 위한 값정의
    YP = [-1, 0, 1, 0] 
    # 테두리 벽
    for x in range(MAZE_W): # x의 값에대한 미로 가로의 값 정리
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1
    # 가운데를 아무것도 없는 상태로 만듦
    for y in range(1, MAZE_H - 1): 
        for x in range(1, MAZE_W - 1): 
            maze[y][x] = 0 # 0=길
    # 기둥&벽
    for y in range(2, MAZE_H - 2, 2): 
        for x in range(2, MAZE_W - 2, 2): 
            maze[y][x] = 1 #미로 데이터 yx합친 기둥 데이터 값은 1이다. 1=벽
    # 기둥에서 상하좌우로 벽 생성
    for y in range(2, MAZE_H - 2, 2):
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0, 3) #랜덤을 0~3까지 기둥이랑 블록x이건데 쉽게 말해 기둥& 바닥 랜덤.
            if x > 2:  # 2열부터 왼쪽에는 벽을 생성하지 않음
                d = random.randint(0, 2)
            maze[y + YP[d]][x + XP[d]] = 1 #기둥의 위치를 말한다. 이거는 4분면으로 나타냄.(플이어의 위치)

    # 미로에서 던전 생성
    # 전체를 벽으로
    for y in range(DUNGEON_H): #y의 값에 대한 '던전' 세로의 값 정리, 미로는 maze
        for x in range(DUNGEON_W): #x의 값에 대한 가로 정리
            dungeon[y][x] = 9 #여기서 9는 벽을 뜻한다 #던전에서는 길을 0 벽을 9로함.
    # 방과 통로 배치
    for y in range(1, MAZE_H - 1): #2중으로 반복한다.
        for x in range(1, MAZE_W - 1): 
            # 통로는 MAZE(3개) 가운데
            dx = x * 3 + 1 
            dy = y * 3 + 1 
            if maze[y][x] == 0: #만약 yx값이 0일때 가운데 상태를 아무것도 없는 걸로 만든다.
                if random.randint(0, 99) < 20:  # 방 생성인데 (0부터 99사이에 숫자가 20보다 작으면)
                    for ry in range(-1, 2): # 길 생성
                        for rx in range(-1, 2):  #길생성
                            dungeon[dy + ry][dx + rx] = 0 #이러므 3곱하기 3칸으로 방만듦
                else:  # 통로 생성(방을 만들지 않을경우) 
                    dungeon[dy][dx] = 0  #MAZE(3개)의 가운데를 0(통로)으로 하기 
                    # # MAZE의 통로로 되어있는 방향을 0(통로)로 한다(방으로 할시 9개 모두 통로로 한다)
                    if maze[y - 1][x] == 0: dungeon[dy - 1][dx] = 0#미로 위칸의 길이라면 통로를 위로 연장
                    if maze[y + 1][x] == 0: dungeon[dy + 1][dx] = 0#미로 아래 칸이 길이라면 통로를 아래로 연장
                    if maze[y][x - 1] == 0: dungeon[dy][dx - 1] = 0#미로 왼쪽 칸이 길이라면 통로를 왼쪽으로 연장
                    if maze[y][x + 1] == 0: dungeon[dy][dx + 1] = 0#미로 오른쪽 칸이 길이라면 통로를 오른쪽으로 연장

def draw_dungeon(bg, fnt):  # 던전 표시
    bg.fill(BLACK) #지정된 색으로 스크린 전체 클리어
    for y in range(-4, 6):
        for x in range(-5, 6):
            X = (x + 5) * 80 #화면 표시용 x좌표 계산값 윈도우 왼쪽 위 모서리부터 그리기 시작함 왼쪽 위 5칸부터 오른쪽 아래 5칸까지 범위의 던전 배경을 그림 pl_x, pl_y 값이 변화하면 그리는 범위도 달라지므로 화면이 스크롤됨
            Y = (y + 4) * 80 #화면 표시용 y좌표 계산값
            dx = pl_x + x #던전 칸 x 좌표 계산 dx=던전 x값
            dy = pl_y + y #던전 컨 y 좌표 계산 dy=던전 y값
            if 0 <= dx and dx < DUNGEON_W and 0 <= dy and dy < DUNGEON_H: #만약에 dx(던전x)가 0보다 크거나 같다면 그리고 던전보다 작고 그리고 dy가 0보다 크거나 같고 그리고 던전보다 작을때
                if dungeon[dy][dx] <= 3: #만약 던전 칸 xy가 3보다 작거나 같을때
                    bg.blit(imgFloor[dungeon[dy][dx]], [X, Y]) #xy는 층수로 바뀐다
                if dungeon[dy][dx] == 9: #만약 던전 칸 xy가 9랑 같을떄
                    bg.blit(imgWall, [X, Y - 40]) #벽이미지를 표시한다
                    if dy >= 1 and dungeon[dy - 1][dx] == 9: #만약 위에 조건을 충족 된 상태에서 던전y값이 1보다 크거나 같고 그리고 던전[dy - 1][dx]이 9일때
                        bg.blit(imgWall2, [X, Y - 80]) #이미지 벽을 생성합니다.
            if x == 0 and y == 0:  #만약 x가 0과 같거나 y가 0과 같을떄
                bg.blit(imgPlayer[pl_a], [X, Y - 40]) # 주인공 캐릭터 표시
    bg.blit(imgDark, [0, 0])  # 네 모서리가 어두운 이미지 겹침
    draw_para(bg, fnt)  # 주인공 능력치 표시

def put_event():  # 길에 이벤트 배치
    global pl_x, pl_y, pl_d, pl_a #밖에있는 플레이어 값들을 꺼내온다.
    # 계단 배치
    while True:
        x = random.randint(3, DUNGEON_W - 4) 
        y = random.randint(3, DUNGEON_H - 4) 
        if (dungeon[y][x] == 0): #만약 던전값이 0이랑 같다면.
            for ry in range(-1, 2):  # 계단 주변을 길로 만듦
                for rx in range(-1, 2): 
                    dungeon[y + ry][x + rx] = 0 #길
            dungeon[y][x] = 3 #던전값이 [y][x] = 3이 나온다면 중단한다. 층수
            break
    # 보물 상자와 누에고치 배치
    for i in range(60): #60번 반복한다.
        x = random.randint(3, DUNGEON_W - 4) 
        y = random.randint(3, DUNGEON_H - 4) 
        if (dungeon[y][x] == 0): #만약 던전[y][x] == 0이라면= 길
            dungeon[y][x] = random.choice([1, 2, 2, 2, 2])#던전값에서 랜덤으로 뽑는다
    # 플레이어 초기 위치
    while True:
        pl_x = random.randint(3, DUNGEON_W - 4) #플레이어 x의 값에서 랜덤으로 뽑는데 값이 3이거나 던전-4이면
        pl_y = random.randint(3, DUNGEON_H - 4) #플레이어 y의 값에서 랜덤으로 뽑는데 값이 3이거나 던전-4이면
        if (dungeon[pl_y][pl_x] == 0): #만약 플레이어 값이 0이면 중단한다.
            break
    pl_d = 1 #플레이어의 방향은 1이고
    pl_a = 2 #플레이어의 애니메이션 움직임은 2이다

def move_player(key):  # 주인공 이동
    global idx, tmr, pl_x, pl_y, pl_d, pl_a, pl_life, food, potion, BlackDiamond, treasure 

    if dungeon[pl_y][pl_x] == 1:  # 보물상자에 닿음(1)
        dungeon[pl_y][pl_x] = 0
        treasure = random.choice([0, 0, 0, 1, 1, 1, 1, 1, 1, 2])
        if treasure == 0:
            potion = potion + 1
        if treasure == 1:
            BlackDiamond = BlackDiamond + 1
        if treasure == 2:
            food = int(food / 2)
        idx = 3
        tmr = 0
        return
    if dungeon[pl_y][pl_x] == 2:  # 크리스탈에 닿음(2)
        dungeon[pl_y][pl_x] = 0
        r = random.randint(0, 99) #랜덤으로 99까지
        if r < 40:  # 랜덤으로 돌렸는데 40보다 작으면 식량이 뜬다
            treasure = random.choice([3, 3, 3, 4])
            if treasure == 3: food = food + 50
            if treasure == 4: food = food + 200
            idx = 3
            tmr = 0
        else:  # 적 출현
            idx = 10
            tmr = 0
        return
    if dungeon[pl_y][pl_x] == 3:  # 계단에 닿음(3)
        idx = 2
        tmr = 0
        return

    # 방향 키로 상하좌우 이동
    x = pl_x # 이동했는지를 확인하기 위해 지금 위치를 저장
    y = pl_y # 이동했는지를 확인하기 위해 지금 위치를 저장
    if key[K_UP] == 1: 
        pl_d = 0
        if dungeon[pl_y - 1][pl_x] != 9: #해당 방향이 벽이 아니라면(벽이면 막히니까 못감 앞으로)
            pl_y = pl_y - 1 #Y좌표를 변경한다.
    if key[K_DOWN] == 1: 
        pl_d = 1 
        if dungeon[pl_y + 1][pl_x] != 9: #방향키 하를 눌렀다면 해당 방향이 벽이 아니면
            pl_y = pl_y + 1 # Y좌표 변경
    if key[K_LEFT] == 1:
        pl_d = 2
        if dungeon[pl_y][pl_x - 1] != 9: #해당뱡향이 벽이 아니라면 X좌표 변경
            pl_x = pl_x - 1
    if key[K_RIGHT] == 1:
        pl_d = 3
        if dungeon[pl_y][pl_x + 1] != 9: #해당방향이 벽이 아니라면 X좌표 변경
            pl_x = pl_x + 1
    pl_a = pl_d * 2 # 0:상 1:하 2:좌 3:우
    if pl_x != x or pl_y != y:  # 이동 시 식량 및 체력 계산
        pl_a = pl_a + tmr % 2  # 이동 시 걷기 애니메이션
        if food > 0:
            food = food - 1
            if pl_life < pl_lifemax:
                pl_life = pl_life + 1
        else:
            pl_life = pl_life - 5
            if pl_life <= 0:
                pl_life = 0
                pygame.mixer.music.stop()
                idx = 9
                tmr = 0

def draw_text(bg, txt, x, y, fnt, col):  # 그림자 포함한 문자 표시
    sur = fnt.render(txt, True, BLACK) #render=어떤 상태가 되게 만든는거, 입각= 폰트가 BLACK가 true가 되도록 한다.
    bg.blit(sur, [x + 1, y + 2])  
    sur = fnt.render(txt, True, col) 
    bg.blit(sur, [x, y]) 

def draw_para(bg, fnt):  # 주인공 능력 표시
    X = 30 
    Y = 600
    bg.blit(imgPara, [X, Y])
    col = WHITE
    if pl_life < 10 and tmr % 2 == 0: col = RED
    draw_text(bg, "{}/{}".format(pl_life, pl_lifemax), X + 128, Y + 6, fnt, col)
    draw_text(bg, str(pl_str), X + 128, Y + 33, fnt, WHITE)
    col = WHITE 
    if food == 0 and tmr % 2 == 0: col = RED
    draw_text(bg, str(food), X + 128, Y + 60, fnt, col)
    draw_text(bg, str(potion), X + 266, Y + 6, fnt, WHITE)
    draw_text(bg, str(BlackDiamond), X + 266, Y + 33, fnt, WHITE)

def init_battle():  # 전투 시작 준비
    global imgEnemy, emy_name, emy_lifemax, emy_life, emy_str, emy_x, emy_y
    typ = random.randint(0, floor) #이거때문에 floor 여서 높은 위치에 있는 보스몹들이 나오지 않음.
    if floor >= 10:
        typ = random.randint(0, 9)# 0부터 9까지의 수를 무작위로 선정한다...
    lev = random.randint(1, floor)
    imgEnemy = pygame.image.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\image_RPG\\enemy" + str(typ) + ".png")
    emy_name = EMY_NAME[typ] + " LV" + str(lev)
    emy_lifemax = 60 * (typ + 1) + (lev - 1) * 10 #적의 생명값.
    emy_life = emy_lifemax
    emy_str = int(emy_lifemax / 8) #적의 공격력은 생명값의 8분의 1
    emy_x = 440 - imgEnemy.get_width() / 2
    emy_y = 560 - imgEnemy.get_height()

def draw_bar(bg, x, y, w, h, val, ma):  # 적 체력 표시 게이지
    pygame.draw.rect(bg, WHITE, [x - 2, y - 2, w + 4, h + 4])
    pygame.draw.rect(bg, BLACK, [x, y, w, h])
    if val > 0:
        pygame.draw.rect(bg, (0, 128, 255), [x, y, w * val / ma, h])

def draw_battle(bg, fnt):  # 전투 화면 표시
    global emy_blink, dmg_eff
    bx = 0
    by = 0
    if dmg_eff > 0:
        dmg_eff = dmg_eff - 1
        bx = random.randint(-20, 20)
        by = random.randint(-10, 10)
    bg.blit(imgBtlBG, [bx, by])
    if emy_life > 0 and emy_blink % 2 == 0:
        bg.blit(imgEnemy, [emy_x, emy_y + emy_step])
    draw_bar(bg, 340, 580, 200, 10, emy_life, emy_lifemax)
    if emy_blink > 0:
        emy_blink = emy_blink - 1
    for i in range(5):  # 전투 메시지 표시
        draw_text(bg, message[i], 600, 100 + i * 50, fnt, WHITE)
    draw_para(bg, fnt)  # 주인공 능력 표시

def battle_command(bg, fnt, key):  # 커맨드 입력 및 표시
    global btl_cmd
    ent = False
    if key[K_a]:  # A 키
        btl_cmd = 0
        ent = True
    if key[K_p]:  # P 키
        btl_cmd = 1
        ent = True
    if key[K_b]:  # B 키
        btl_cmd = 2
        ent = True
    if key[K_r]:  # R 키
        btl_cmd = 3
        ent = True
    if key[K_UP] and btl_cmd > 0:  # ↑ 키
        btl_cmd -= 1
    if key[K_DOWN] and btl_cmd < 3:  # ↓ 키
        btl_cmd += 1
    if key[K_SPACE] or key[K_RETURN]:
        ent = True
    for i in range(4):
        c = WHITE
        if btl_cmd == i: c = BLINK[tmr % 6]
        draw_text(bg, COMMAND[i], 20, 360 + i * 60, fnt, c)
    return ent

# 전투 메시지 표시 처리
message = [""] * 10 #전투 메시지 입력 리스트
def init_message(): #메시지 초기화 함수
    for i in range(10): #반복
        message[i] = ""  #리스트의 문자열 대입

def set_message(msg): #메시지 설정 함수
    for i in range(10):  #반복
        if message[i] == "": #만약 문자열이 설정되어 있지 않다면
            message[i] = msg #새로운 문자열을 대입한다.
            return #함수 처리 종류
    for i in range(9):  #pygame 모듈 반복
        message[i] = message[i + 1] #메시지를 한 문자씩 슬라이드
    message[9] = msg  #마지막 행에 새로운 문자열 대입 

def main():  # 메인 처리
    global speed, idx, tmr, floor, fl_max, welcome           
    global pl_a, pl_lifemax, pl_life, pl_str, food, potion, BlackDiamond #위에 있는것들 다 끄집어 온다.
    global emy_life, emy_step, emy_blink, dmg_eff
    dmg = 0
    lif_p = 0
    str_p = 0

    pygame.init()
    pygame.display.set_caption("INFINITE Castle") 
    screen = pygame.display.set_mode((880, 720))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    fontS = pygame.font.Font(None, 30)

    se = [ #효과음&징글
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_se_attack.ogg"),
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_se_blaze.ogg"),
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_se_potion.ogg"),
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_jin_gameover.ogg"),
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_jin_levup.ogg"),
        pygame.mixer.Sound("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_jin_win.ogg"),
    ]
    

    while True: #무한 반복
        for event in pygame.event.get(): #파이게임 이벤트 반복 처리
            if event.type == QUIT: #윈도우 X버튼을 누른 경우
                pygame.quit() #파이게임 모듈 초기화
                sys.exit() #프로그램을 종료 시킨다.
            if event.type == KEYDOWN: #키를 누른 이벤트가 발생한 경우
                if event.key == K_s: 
                    speed = speed + 1
                    if speed == 4: 
                        speed = 1

        tmr = tmr + 1
        key = pygame.key.get_pressed()

        if idx == 0:  # 타이틀 화면
            if tmr == 1:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\Chapter12_sound_ohd_bgm_title.ogg")
                pygame.mixer.music.play(-1)
            screen.fill(BLACK)
            screen.blit(imgTitle, [40, 60])
            if fl_max >= 2: #2보다 작으면 안뜸.
                draw_text(screen, "You reached floor {}.".format(fl_max), 300, 460, font, CYAN) #죽고난후
            draw_text(screen, "Press Space Key", 320, 560, font, BLINK[tmr % 6])
            if key[K_SPACE] == 1:
                make_dungeon()
                put_event()
                floor = 1
                welcome = 15
                pl_lifemax = 200
                pl_life = pl_lifemax
                pl_str = 120
                food = 300
                potion = 1
                BlackDiamond = 0
                idx = 1
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\ohd_bgm_field.ogg") 
                pygame.mixer.music.play(-1)

        elif idx == 1:  # 플레이어 이동
            move_player(key)
            draw_dungeon(screen, fontS)
            draw_text(screen, "floor {} ({},{})".format(floor, pl_x, pl_y), 60, 40, fontS, WHITE) #게임 플레이화면 왼쪽에있음.
            if welcome > 0:
                welcome = welcome - 1
                draw_text(screen, "Welcome to floor {}.".format(floor), 300, 180, font, CYAN)

        elif idx == 2:  # 화면 전환
            draw_dungeon(screen, fontS)
            if 1 <= tmr and tmr <= 5:
                h = 80 * tmr
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h]) # 위쪽을 닫고 가다
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h]) # 아래쪽을 닫고 가다
            if tmr == 5:
                floor = floor + 1
                if floor > fl_max:
                    fl_max = floor
                welcome = 15
                make_dungeon()
                put_event()
            if 6 <= tmr and tmr <= 9:
                h = 80 * (10 - tmr)
                pygame.draw.rect(screen, BLACK, [0, 0, 880, h])# 위쪽을 열고 가다
                pygame.draw.rect(screen, BLACK, [0, 720 - h, 880, h])# 아래쪽을 열고 가다
            if tmr == 10:
                idx = 1

        elif idx == 3:  # 아이템 입수 혹은 함정
            draw_dungeon(screen, fontS)
            screen.blit(imgItem[treasure], [320, 220])
            draw_text(screen, TRE_NAME[treasure], 380, 240, font, WHITE) # 아이템 텍스트
            if tmr == 10:
                idx = 1

        elif idx == 9:  # 게임 오버
            if tmr <= 30:
                PL_TURN = [2, 4, 0, 6]
                pl_a = PL_TURN[tmr % 4]
                if tmr == 30: pl_a = 8  # 쓰러진 그림
                draw_dungeon(screen, fontS)
            elif tmr == 31:
                se[3].play()
                draw_text(screen, "You died.", 360, 240, font, RED)
                draw_text(screen, "Game over.", 360, 380, font, RED)
            elif tmr == 100:
                idx = 0
                tmr = 0

        elif idx == 10:  # 전투 시작
            if tmr == 1:
                pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\ohd_bgm_battle.ogg")
                pygame.mixer.music.play(-1)
                init_battle()
                init_message()
            elif tmr <= 4:
                bx = (4 - tmr) * 220
                by = 0
                screen.blit(imgBtlBG, [bx, by])# 배틀 화면을 오른쪽에서 왼쪽으로 삽입해 가다
                draw_text(screen, "Encounter!", 350, 200, font, WHITE)
            elif tmr <= 16:
                draw_battle(screen, fontS)
                draw_text(screen, emy_name + " appear!", 300, 200, font, WHITE)
            else:
                idx = 11
                tmr = 0

        elif idx == 11:  # 플레이어 턴
            draw_battle(screen, fontS)
            if tmr == 1: set_message("Your turn.")
            if battle_command(screen, font, key) == True:
                if btl_cmd == 0:
                    idx = 12
                    tmr = 0
                if btl_cmd == 1 and potion > 0:
                    idx = 20
                    tmr = 0
                if btl_cmd == 2 and BlackDiamond > 0:
                    idx = 21
                    tmr = 0
                if btl_cmd == 3:
                    idx = 14
                    tmr = 0

        elif idx == 12:  # 플레이어 공격
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You attack!")
                se[0].play()
                dmg = pl_str + random.randint(0, 9)
            if dmg < 300:
                if 2 <= tmr and tmr <= 4:
                    screen.blit(imgEffect[0], [700 - tmr * 120, -100 + tmr * 120]) #플레이어 공격이 300일때랑 300넘어서의 모션은 다르게 설정해 두었답니다.
            if dmg > 300:      
                if 2 <= tmr and tmr <= 4:
                    screen.blit(imgEffect[2], [700 - tmr * 120, -100 + tmr * 120])
            if tmr == 5:
                emy_blink = 5
                set_message(str(dmg) + "pts of damage!")
            if tmr == 11:
                emy_life = emy_life - dmg
                if emy_life <= 0:
                    emy_life = 0
                    idx = 16
                    tmr = 0
            if tmr == 16:
                idx = 13
                tmr = 0
        
        elif idx == 13:  # 적 턴, 적 공격
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Enemy turn.")
            if tmr == 5:
                set_message(emy_name + " attack!")
                se[0].play()
                emy_step = 30
            if tmr == 9:
                dmg = emy_str + random.randint(0, 9)
                set_message(str(dmg) + "pts of damage!")
                dmg_eff = 5
                emy_step = 0
            if tmr == 15:
                pl_life = pl_life - dmg
                if pl_life < 0:
                    pl_life = 0
                    idx = 15
                    tmr = 0
            if tmr == 20:
                idx = 11
                tmr = 0

        elif idx == 14:  # 도망 가능한가?
            draw_battle(screen, fontS)
            if tmr == 1: set_message("...")
            if tmr == 2: set_message("......")
            if tmr == 3: set_message(".........")
            if tmr == 4: set_message("............")
            if tmr == 5:
                if random.randint(0, 99) < 60:
                    idx = 22
                else:
                    set_message("You failed to flee.")
            if tmr == 10:
                idx = 13
                tmr = 0

        elif idx == 15:  # 패배
            draw_battle(screen, fontS)
            if tmr == 1:
                pygame.mixer.music.stop()
                set_message("You lose.")
            if tmr == 11:
                idx = 9
                tmr = 29

        elif idx == 16:  # 승리
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("You win!")
                pygame.mixer.music.stop()
                se[5].play()
            if tmr == 28:
                idx = 22
                if random.randint(0, emy_lifemax) > random.randint(0, pl_lifemax):
                    idx = 17
                    tmr = 0

        elif idx == 17:  # 레벨업
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Level up!")
                se[4].play()
                lif_p = random.randint(30, 50)
                str_p = random.randint(20, 40)
            if tmr == 21:
                set_message("Max life + " + str(lif_p))
                pl_lifemax = pl_lifemax + lif_p
            if tmr == 26:
                set_message("Str + " + str(str_p))
                pl_str = pl_str + str_p
            if tmr == 50:
                idx = 22

        elif idx == 20:  # Potion
            draw_battle(screen, fontS)
            if tmr == 1:
                set_message("Potion!")
                se[2].play()
            if tmr == 6:
                pl_life = pl_lifemax
                potion = potion - 1
            if tmr == 11:
                idx = 13
                tmr = 0

        elif idx == 21:  # Black Diamond
            draw_battle(screen, fontS)
            img_rz = pygame.transform.rotozoom(imgEffect[1], 30 * tmr, (12 - tmr) / 8)
            X = 440 - img_rz.get_width() / 2
            Y = 360 - img_rz.get_height() / 2
            screen.blit(img_rz, [X, Y])
            if tmr == 1:
                set_message("Black Diamond!")
                se[1].play()
            if tmr == 6:
                BlackDiamond = BlackDiamond - 1
            if tmr == 11:
                dmg = 1000
                idx = 12
                tmr = 4
            
        elif idx == 22:  # 전투 종료
            pygame.mixer.music.load("C:\\Users\\win10\\Desktop\\pythonworkspace\\포트리올\\sound_RPG\\ohd_bgm_field.ogg")
            pygame.mixer.music.play(-1)
            idx = 1
    

        draw_text(screen, "[S]peed " + str(speed), 740, 40, fontS, WHITE)

        pygame.display.update()
        clock.tick(4 + 2 * speed)
        
if __name__ == '__main__': #__name__ == __main__은 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드를 돌리라는 명령이 됩니다.
    main() # 인터프리터 = 소스 코드를 바로 실행하는 컴퓨터 프로그램 또는 환경을 말한다.
