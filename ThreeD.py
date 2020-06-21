import pygame, math
pygame.init()

cols = {"black":(0,0,0),"white":(255,255,255),"grey":(200,200,200),"red":(255,0,0),\
        "orange":(255,100,100),"yellow":(0,255,255),"green":(0,255,0),"blue":(0,0,255),\
        "purple":(100,0,100)}

class camera():
    def __init__(self, render = 1, x = 0, y = 0, z = 0, angle = [0, 0, 0], appearance = []):
        self.x = x
        self.y = y
        self.z = z
        self.a = angle
        self.r = render
        self.app = appearance

class screen():
    def __init__(self, width = 1500, height = 750, distance = 500):
        self.w = width
        self.h = height
        self.d = distance
        self.disp = pygame.display.set_mode((width, height))

def sort(a):
    return a[0][2]

def roundToZero(x):
    return int(math.copysign(math.floor(abs(x)), x))

def makeChunks(items):
    ends = [[0, 0], [0, 0]]
    for item in items:
        if item[0][0] < ends[0][0]: ends[0][0] = item[0][0]
        elif item[0][0] > ends[0][1]: ends[0][1] = item[0][0]
        if item[0][2] < ends[1][0]: ends[1][0] = item[0][2]
        elif item[0][2] > ends[1][1]: ends[1][1] = item[0][2]
    ends = [[math.floor(ends[0][0]/100), math.ceil(ends[0][1]/100)],\
            [math.floor(ends[1][0]/100), math.ceil(ends[1][1]/100)]]
    chunks = {i:{j:[]for j in range(ends[1][0],ends[1][1])}for i in range(ends[0][0],ends[0][1])}
    for item in items:
        chunks[math.floor(item[0][0]/100)][math.floor(item[0][2]/100)].append(item)
    return chunks

def getNear(chunks, c):
    near = []
    x = math.floor(c.x / 100)
    z = math.floor(c.z / 100)
    for i in range(x - c.r, x + c.r + 1):
        for j in range(z - c.r, z + c.r + 1):
            try: near += chunks[i][j]
            except: pass
    return near

def rotate(shape, a, pos):
    s0 = math.sin(a[0])
    s1 = math.sin(a[1])
    s2 = math.sin(a[2])
    c0 = math.cos(a[0])
    c1 = math.cos(a[1])
    c2 = math.cos(a[2])
    points = []
    for point in shape:
        x, y, z = point[0] - pos[0], point[1] - pos[1], point[2] - pos[2]
        x, z = x * c0 - z * s0, z * c0 + x * s0
        y, z = y * c1 - z * s1, z * c1 + y * s1
        x, y = x * c2 - y * s2, y * c2 + x * s2
        points.append([x, y, z])
    return points

def translate(shape, screen):
    points = []
    vis = False
    for point in shape:
        x, y, z = point[0], point[1], point[2]
        if z >= 0: return None
        x = x / z * screen.d
        y = y / z * screen.d
        points.append([screen.w / 2 + x, screen.h / 2 + y, z])
        if x>-screen.w/2 and x<screen.w/2 and y>-screen.h/2 and y<screen.h/2: vis = True
    if vis: return points

def draw(items, c, screen):
    try:
        screen.disp.fill((255, 255, 255))
        shapes = []
        for item in items:
            shape = translate(rotate(item,c.a,[c.x+math.sin(c.a[0])*75,c.y,c.z+math.cos(c.a[0])*75]),screen)
            if shape: shapes.append(shape)
        shapes.sort(key = sort)
        for item in shapes:
            shape = [point[:2] for point in item]
            pygame.draw.polygon(screen.disp, cols["grey"], shape)
            pygame.draw.lines(screen.disp, cols["black"], True, shape)
        pygame.display.update()
    except Exception as e: print(e)
