def createStats(names, goals, goals_avoided, assists) :
    names = names.replace(",","")
    names = names.split()
    stats = {}
    for name, goal, avoided, assist in zip(names, goals, goals_avoided, assists):
        stats[name] = (goal, avoided, assist)
    return stats

def getGoleador(stats):
    goleador = max(stats, key=lambda x: stats[x][0])
    return goleador, stats[goleador][0]

def getInfluyente(stats):
    influyente = max(stats, key=lambda x: stats[x][0] * 1.5 + stats[x][1] * 1.25 + stats[x][2])
    return influyente

def getMatchProm(goals):
    return sum(goals) / 25

def getGoleadorProm(stats):
    return stats[getGoleador(stats)[0]][0] / 25
