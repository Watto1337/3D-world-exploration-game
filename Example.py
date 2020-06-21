import ThreeD, terrain, math, time
p = ThreeD.pygame

c = ThreeD.camera(y = 50, render = 3)
screen = ThreeD.screen()

tw = 10
th = 10
tu = 10
t = terrain.getTerrain(tw, th, tu, 50, round(c.r * tu * (6 + 3 / 2)))
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

def rectangle(x, y, z, w, l):
    ws = w / round(w / 5)
    ls = l / round(l / 5)
    c = []
    for i in range(round(w / ws)):
        for j in range(round(l / ls)):
            c.append([[x+i*ws,y,z+j*ls],[x+(i+1)*ws,y,z+j*ls],[x+i*ws,y,z+(j+1)*ls]])
            c.append([[x+i*ws,y,z+(j+1)*ls],[x+(i+1)*ws,y,z+(j+1)*ls],[x+(i+1)*ws,y,z+j*ls]])
    return c

def top(x, y, z, w, l, h):
    t = [[[x,y,z],[x,y,z+l],[x,y+h/2,z+l],[x,y+h/2,z]],\
         [[x+w,y,z],[x+w,y,z+l],[x+w,y+h/2,z+l],[x+w,y+h/2,z]],\
         [[x,y,z],[x+w,y,z],[x+w,y+h/2,z],[x,y+h/2,z]],\
         [[x,y,z+l],[x+w,y,z+l],[x+w,y+h,z+l],[x,y+h,z+l]],\
         [[x,y+h/2,z],[x+w,y+h/2,z],[x+w,y+h/2,z+l/3],[x,y+h/2,z+l/3]],\
         [[x,y+h/2,z+l/3],[x+w,y+h/2,z+l/3],[x+w,y+h,z+l/3],[x,y+h,z+l/3]],\
         [[x,y+h/2,z+l/3],[x,y+h,z+l/3],[x,y+h,z+l],[x,y+h/2,z+l]],\
         [[x+w,y+h/2,z+l/3],[x+w,y+h,z+l/3],[x+w,y+h,z+l],[x+w,y+h/2,z+l]],\
         [[x,y+h,z+l/3],[x+w,y+h,z+l/3],[x+w,y+h,z+l],[x,y+h,z+l]],\
         ]
    return t

frame = []
frame += wheel(-12, 4, 20) + wheel(-12, 4, -20) + wheel(12, 4, 20) + wheel(12, 4, -20)
frame += top(-15, 6, -35, 30, 70, 25)
nsTilt = 0
ewTilt = 0
carAngle = 0

on = True
while on:
    keys = p.key.get_pressed()

    if keys[p.K_w]:
        c.x += math.sin(carAngle) * 3
        c.z -= math.cos(carAngle) * 3
    if keys[p.K_s]:
        c.x -= math.sin(carAngle) * 3
        c.z += math.cos(-carAngle) * 3
    if keys[p.K_a] and (keys[p.K_w] or keys[p.K_s]):
        carAngle += 0.05
        c.a[0] -= 0.05
    if keys[p.K_d] and (keys[p.K_w] or keys[p.K_s]):
        carAngle -= 0.05
        c.a[0] += 0.05

    if mouse:
        pos = p.mouse.get_pos()
        c.a[0] = (c.a[0] - (screen.w / 2 - pos[0]) / math.pi / 80) % (math.pi * 4)
        c.a[1] -= (screen.h / 2 - pos[1]) / math.pi / 80
        if c.a[1] < -math.pi / 2: c.a[1] = -math.pi / 2
        elif c.a[1] > math.pi / 2: c.a[1] = math.pi / 2
        p.mouse.set_pos(screen.w / 2, screen.h / 2)
    if p.mouse.get_pressed()[0]:
        p.mouse.set_pos(screen.w / 2, screen.h / 2)
        p.mouse.set_visible(mouse)
        mouse = not mouse
        time.sleep(0.1)

    if c.x > tw*tu*15: c.x = -tw*tu*15
    elif c.x < -tw*tu*15: c.x = tw*tu*15
    if c.z > th*tu*15: c.z = -th*tu*15
    elif c.z < -th*tu*15: c.z = th*tu*15

    try:
        N=t[1][round(c.x/15+len(t[1])/2)%(tw*tu)][round(c.z/15+len(t[1][0])/2-1)%(th*tu)]
        S=t[1][round(c.x/15+len(t[1])/2)%(tw*tu)][round(c.z/15+len(t[1][0])/2+1)%(th*tu)]
        E=t[1][round(c.x/15+len(t[1])/2+1)%(tw*tu)][round(c.z/15+len(t[1][0])/2)%(th*tu)]
        W=t[1][round(c.x/15+len(t[1])/2-1)%(tw*tu)][round(c.z/15+len(t[1][0])/2)%(th*tu)]
        c.y = ((N+S+E+W)/4 + 2 * (c.y - 50)) / 3 + 50

        nsTilt = (math.tan((N-S)/50)/math.pi*3+2*nsTilt)/3
        ewTilt = (math.tan((E-W)/30)/math.pi*3+2*ewTilt)/3
    except: pass
    
    c.app = [ThreeD.rotate(shape,[carAngle,nsTilt,ewTilt],[0,0,0]) for shape in frame]
    c.app = [[[c.x+point[0],c.y+point[1]-50,c.z+point[2]]for point in item]for item in c.app]

    r = ThreeD.getNear(n, c)
    screen.disp.fill(ThreeD.cols["white"])
    ThreeD.draw(r, c, screen)
    ThreeD.draw(c.app, c, screen)
    p.display.update()
    
    for e in ThreeD.pygame.event.get():
        if e.type == ThreeD.pygame.QUIT:
            ThreeD.pygame.quit()
            on = False
