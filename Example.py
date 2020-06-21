import ThreeD, terrain, math, time
p = ThreeD.pygame

c = ThreeD.camera(render = 3, y = 50)
screen = ThreeD.screen()

t = terrain.getTerrain(50, 10, 10, 50)
n = ThreeD.makeChunks(t[0])
mouse = False

# 25 tall, 30 wide, 70 long

def wheel(x, y, z):
    w = [[[x-2,y-4,z-4],[x-2,y-4,z+4],[x-2,y+4,z+4]],\
         [[x-2,y-4,z-4],[x-2,y+4,z-4],[x-2,y+4,z+4]],\
         [[x+2,y-4,z-4],[x+2,y-4,z+4],[x+2,y+4,z+4]],\
         [[x+2,y-4,z-4],[x+2,y+4,z-4],[x+2,y+4,z+4]],\
         [[x-2,y-4,z-4],[x-2,y-4,z+4],[x+2,y-4,z+4],[x+2,y-4,z-4]],\
         [[x-2,y+4,z-4],[x-2,y+4,z+4],[x+2,y+4,z+4],[x+2,y+4,z-4]],\
         [[x-2,y-4,z-4],[x-2,y+4,z-4],[x+2,y+4,z-4],[x+2,y-4,z-4]],\
         [[x-2,y-4,z+4],[x-2,y+4,z+4],[x+2,y+4,z+4],[x+2,y-4,z+4]],\
         ]
    return w

def chassis(x, y, z, w, h):
    ws = w / round(w / 5)
    hs = h / round(h / 5)
    c = []
    for i in range(round(w / ws)):
        for j in range(round(h / hs)):
            c.append([[x+i*ws,y,z+j*hs],[x+(i+1)*ws,y,z+j*hs],[x+i*ws,y,z+(j+1)*hs]])
            c.append([[x+i*ws,y,z+(j+1)*hs],[x+(i+1)*ws,y,z+(j+1)*hs],[x+(i+1)*ws,y,z+j*hs]])
    return c

frame = []
frame += wheel(-14, 4, 20) + wheel(-14, 4, -20) + wheel(14, 4, 20) + wheel(14, 4, -20)
frame += chassis(-15, 6, -35, 30, 70)

on = True
while on:
    keys = p.key.get_pressed()

    s0 = math.sin(c.a[0])
    c0 = math.cos(c.a[0])

    if keys[p.K_w]:
        c.x -= s0 * c.r
        c.z -= c0 * c.r
    if keys[p.K_s]:
        c.x += s0 * c.r
        c.z += c0 * c.r
    if keys[p.K_a]:
        c.x += c0 * c.r
        c.z -= s0 * c.r
    if keys[p.K_d]:
        c.x -= c0 * c.r
        c.z += s0 * c.r

    if mouse:
        pos = p.mouse.get_pos()
        c.a[0] = (c.a[0] - (screen.w / 2 - pos[0]) / math.pi / 80) % (math.pi * 4)
        c.a[1] -= (screen.h / 2 - pos[1]) / math.pi / 80
        if c.a[1] < -math.pi / 2: c.a[1] = -math.pi / 2
        elif c.a[1] > math.pi / 2: c.a[1] = math.pi / 2
        p.mouse.set_pos(screen.w / 2, screen.h / 2)
    if p.mouse.get_pressed()[0]:
        p.mouse.set_visible(mouse)
        mouse = not mouse
        time.sleep(0.1)
    
    #middle=t[1][round(c.x/20+len(t[1])/2)][round(c.z/20+len(t[1][0])/2)]
    front=t[1][round((c.x-s0*35)/20+len(t[1])/2)][round((c.z-c0*35)/20+len(t[1][0])/2)]
    back=t[1][round((c.x+s0*35)/20+len(t[1])/2)][round((c.z+c0*35)/20+len(t[1][0])/2)]
    left=t[1][round((c.x+c0*15)/20+len(t[1])/2)][round((c.z-s0*15)/20+len(t[1][0])/2)]
    right=t[1][round((c.x-c0*15)/20+len(t[1])/2)][round((c.z+s0*15)/20+len(t[1][0])/2)]
    c.y = (front+back+left+right)/4 + 50

    fbTilt = math.tan((back - front) / 50) / math.pi
    lrTilt = math.tan((right - left) / 30) / math.pi

    c.app = [ThreeD.rotate(shape,[-c.a[0],fbTilt,lrTilt],[0,0,0]) for shape in frame]
    c.app = [[[c.x+point[0],c.y+point[1]-50,c.z+point[2]]for point in item]for item in c.app]

    r = ThreeD.getNear(n, c) + c.app
    ThreeD.draw(r, c, screen)
    
    for e in ThreeD.pygame.event.get():
        if e.type == ThreeD.pygame.QUIT:
            ThreeD.pygame.quit()
            on = False
