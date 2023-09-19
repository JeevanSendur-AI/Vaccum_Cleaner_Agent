actions = []
dirt_loc = [(2,2),(0,1),(1,1),(1,0),(2,0)]
dirt_loc.sort()
agent_loc = [0,0]
performance = 0
for location in dirt_loc:
    x, y = location
    while(True):
        if y < agent_loc[1]:
            actions.append('left')
            agent_loc[1] -= 1
            performance -= 1
            print("left   --> performance point lost   = -1, Total ==", performance,"pos -",agent_loc)
        elif y > agent_loc[1]:
            actions.append('right')
            agent_loc[1] += 1
            performance -= 1
            print("right  --> performance point lost   = -1, Total ==", performance,"pos -",agent_loc)
        if x > agent_loc[0]:
            actions.append('down')
            agent_loc[0] += 1
            performance -= 1
            print("down   --> performance point lost   = -1, Total ==", performance,"pos -",agent_loc)
        elif x < agent_loc[0]:
            actions.append('up')
            agent_loc[0] -=1
            performance -= 1
            print("up     --> performance point lost   = -1, Total ==", performance,"pos -",agent_loc)
        if x == agent_loc[0] and y == agent_loc[1]:
            actions.append('suck')
            performance += 1
            print("suck   --> performance point gained = +1, Total ==", performance,"pos -",agent_loc)
            break