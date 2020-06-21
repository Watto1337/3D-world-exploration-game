import random

def scalars(w, h):
    scals = [[random.random() * 2 - 1 for j in range(h)] for i in range(w)]
    for i in range(len(scals)): scals[i].append(scals[i][0])
    scals.append(scals[0])
    return scals

def lerp(a, b, t):
    t = 6*t**5 - 15*t**4 + 10*t**3
    return a + t * (b - a)

def pixels(scals, u, scale):
    pixs = []
    for i in range(len(scals) - 1):
        for k in range(u):
            pixs.append([])
            for j in range(len(scals[i]) - 1):
                for l in range(u):
                    pixs[i * u + k].append(lerp(lerp(scals[i][j],scals[i+1][j],k/u),\
                                                lerp(scals[i][j+1],scals[i+1][j+1],k/u),\
                                                l/u) * scale)
    return pixs

def getNoise(w, h, u, scale):
    scals = scalars(w, h)
    pixs = pixels(scals, u, scale)
    return pixs
