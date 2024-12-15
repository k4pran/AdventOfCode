with open("day11.txt", 'r') as f:
    line = f.read()

    stones = line.split(" ")
    blinks = 6

    for i in range(blinks):
        updated_stones = []
        for stone in stones:

            if stone == "0":
                updated_stones.append("1")
            elif len(stone) % 2 == 0 :
                stone_divide = int(len(stone) / 2)
                left_stone = str(int(stone[:stone_divide]))
                right_stone = str(int(stone[stone_divide:]))

                updated_stones.append(left_stone)
                updated_stones.append(right_stone)
            else:
                updated_stones.append(str(int(stone) * 2024))
        stones = updated_stones
        print(stones)

    print(f"\nDay 11-1: {len(stones)}")



