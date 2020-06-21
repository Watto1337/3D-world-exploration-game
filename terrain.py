import noise

def getTerrain(w, h, u, yScale):
    hMap = noise.getNoise(w, h, u, yScale)
    terrain = []
    for i in range(w * u):
        for j in range(h * u):
            terrain.append([[(i-w/2*u)*20,   hMap[i][j],     (j-h/2*u)*20],\
                            [(i-1-w/2*u)*20, hMap[i-1][j],   (j-h/2*u)*20],\
                            [(i-1-w/2*u)*20, hMap[i-1][j-1], (j-1-h/2*u)*20]])
            terrain.append([[(i-w/2*u)*20,   hMap[i][j],     (j-h/2*u)*20],\
                            [(i-w/2*u)*20,   hMap[i][j-1],   (j-1-h/2*u)*20],\
                            [(i-1-w/2*u)*20, hMap[i-1][j-1], (j-1-h/2*u)*20]])
    return [terrain, hMap]
