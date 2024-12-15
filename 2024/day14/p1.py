GRID_WIDTH = 101
GRID_HEIGHT = 103
SECONDS = 100


def move_for(secs):

    for i in range(secs):
        pos = bot[0]
        vel = bot[1]

        pos[0] = (pos[0] + vel[0]) % GRID_WIDTH
        pos[1] = (pos[1] + vel[1]) % GRID_HEIGHT

    return pos




with open("day14.txt", 'r') as f:
    lines = f.read().splitlines()

    bots = []
    quads = {'TL': 0, 'TR': 0, 'BR': 0, 'BL': 0}
    for line in lines:

        parts = line.split(" ")
        pos = [int(x) for x in parts[0][2:].split(",")]
        vel = [int(x) for x in parts[1][2:].split(",")]

        bot = (pos, vel)
        final_pos = move_for(SECONDS)

        if final_pos[0] < GRID_WIDTH // 2 and final_pos[1] < GRID_HEIGHT // 2:
            quads['TL'] += 1

        elif final_pos[0] < GRID_WIDTH // 2 and final_pos[1] > GRID_HEIGHT // 2:
            quads['TR'] += 1

        elif final_pos[0] > GRID_WIDTH // 2 and final_pos[1] > GRID_HEIGHT // 2:
            quads['BR'] += 1

        elif final_pos[0] > GRID_WIDTH // 2 and final_pos[1] < GRID_HEIGHT // 2:
            quads['BL'] += 1


    total = quads['TL'] * quads['TR'] * quads['BR'] * quads['BL']

    print(f"\nDay 14-1: {total}")
