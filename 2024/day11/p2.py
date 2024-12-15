from collections import defaultdict

with open("day11.txt", 'r') as f:
    line = f.read()

    stones = line.split(" ")
    blinks = 75

    stone_counts = defaultdict(int)
    for stone in stones:
        stone_counts[stone] = 1

    for i in range(blinks):
        new_counts = defaultdict(int)
        for stone, count in stone_counts.items():

            if stone == "0":
                new_counts["1"] += count
            elif len(stone) % 2 == 0 :
                stone_divide = int(len(stone) / 2)
                left_stone = str(int(stone[:stone_divide]))
                right_stone = str(int(stone[stone_divide:]))

                new_counts[left_stone] += count
                new_counts[right_stone] += count
            else:
                transformed_stone = str(int(stone) * 2024)
                new_counts[transformed_stone] += count
        stone_counts = new_counts

    total_stones = sum(stone_counts.values())


    print(f"\nDay 11-2: {total_stones}")



