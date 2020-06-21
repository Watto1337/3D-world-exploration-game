import noise

def getTerrain(w, h, u, yScale, buffer):
    hMap = noise.getNoise(w, h, u, yScale)
    terrain = []
    for i in range(-buffer, w * u + buffer):
        for j in range(-buffer, h * u + buffer):
            terrain.append([[(i-w/2*u)*15,  hMap[i%(w*u)][j%(h*u)],        (j-h/2*u)*15],\
                            [(i-1-w/2*u)*15,hMap[(i-1)%(w*u)][j%(h*u)],    (j-h/2*u)*15],\
                            [(i-1-w/2*u)*15,hMap[(i-1)%(w*u)][(j-1)%(h*u)],(j-1-h/2*u)*15]])
            terrain.append([[(i-w/2*u)*15,  hMap[i%(w*u)][j%(h*u)],        (j-h/2*u)*15],\
                            [(i-w/2*u)*15,  hMap[i%(w*u)][(j-1)%(h*u)],    (j-1-h/2*u)*15],\
                            [(i-1-w/2*u)*15,hMap[(i-1)%(w*u)][(j-1)%(h*u)],(j-1-h/2*u)*15]])
    return [terrain, hMap]
