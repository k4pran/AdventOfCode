from collections import defaultdict, deque

with open("day9.txt", 'r') as f:
    line = f.read()

    id = 0
    file_indices = deque()
    space_indices = list()
    pointer = 0
    for i, c in enumerate(line):
        is_file = i % 2 == 0
        block_length = int(c)
        if is_file:

            for _ in range(block_length):
                file_indices.append((pointer, id))
                pointer += 1

            id += 1
        else:
            if block_length > 0:
                for _ in range(block_length):
                    space_indices.append(pointer)
                    pointer += 1

    checksum = 0
    f_nb = 0
    i = 0
    while file_indices:
        if i in space_indices:
            file_block = file_indices.pop()

            checksum += f_nb * file_block[1]
        else:
            file_block = file_indices.popleft()
            checksum += f_nb * file_block[1]

        f_nb += 1
        i += 1

    print(f"\nDay 9-1: {checksum}")



