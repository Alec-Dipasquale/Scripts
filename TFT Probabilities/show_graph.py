


probability = [
    [1.00,  0,      0,      0,      0],
    [1.00,  0,      0,      0,      0],
    [.65,   .3,     .05,    0,      0],
    [.5,    .35,    .15,    0,      0],
    [.37,   .35,    .25,    .03,    0],
    [.245,  .35,    .30,    .10,    .005],
    [.2,    .3,     .33,    .15,    .02],
    [.15,   .25,    .35,    .2,     .05],
    [.10,   .15,    .35,    .3,     .1]
]

xpNeededByLevel = [0, 2, 6, 10, 18, 30, 46, 70]

def getTable():
    table = '\t\tTIER 1\t\tTIER 2\t\tTIER 3\t\tTIER 4\t\t TIER 5\n'
    count = 1
    count2 = 1
    while(count <= 9):
        table = table + 'LEVEL ' + str(count)
        while(count2 <= 5):
            percent = getProbability(count-1, count2-1)*100
            table = table + '\t\t%.1f' %percent + "%"
            count2 = count2 + 1
        count = count + 1
        count2 = 1
        table = table + '\n'
    return table

def getProbability(level, tier):
    percentNotGettingChamp = (1- probability[level][tier])**5
    chanceToGetTierChamp = 1- percentNotGettingChamp
    amountOfTierChampsPerRoll = chanceToGetTierChamp*5
    totalCost = 0
    refreshCost = 2
    xpCost = 4
    xpGain = 4

    # while(xpNeededByLevel[level]>)

    return chanceToGetTierChamp
