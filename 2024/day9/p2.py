def merge_free_range(space_ranges, start, end):

    if start >= end:
        return space_ranges

    space_ranges.append((start, end))
    space_ranges.sort(key=lambda x: x[0])

    merged = []
    for (rng_start, rng_end) in space_ranges:
        if not merged:
            merged.append((rng_start, rng_end))
        else:
            last_start, last_end = merged[-1]
            if rng_start <= last_end:
                merged[-1] = (last_start, max(last_end, rng_end))
            else:
                merged.append((rng_start, rng_end))
    return merged


with open("day9.txt", "r") as f:
    line = f.read().strip()

    files = []
    space_ranges = []
    pointer = 0
    file_id = 0

    for i, c in enumerate(line):
        length = int(c)
        if i % 2 == 0:
            start = pointer
            end = pointer + length
            files.append((file_id, (start, end)))
            pointer = end
            file_id += 1
        else:
            if length > 0:
                space_ranges.append((pointer, pointer + length))
            pointer += length

    files.sort(key=lambda x: x[0])
    files = files[::-1]

    final_positions = {}

    for (f_id, file_block) in files:
        old_start, old_end = file_block
        size = old_end - old_start
        moved = False

        space_ranges.sort(key=lambda x: x[0])

        for i, space_range in enumerate(space_ranges):
            sr_start, sr_end = space_range
            sr_size = sr_end - sr_start
            if sr_size >= size and (sr_start + size) <= old_start:
                new_start = sr_start
                new_end = sr_start + size

                space_ranges[i] = (new_end, sr_end)

                space_ranges = merge_free_range(space_ranges, old_start, old_end)

                final_positions[f_id] = (new_start, new_end)
                moved = True
                break

        if not moved:
            final_positions[f_id] = (old_start, old_end)

    checksum = 0
    for f_id, (start, end) in final_positions.items():
        for pos in range(start, end):
            checksum += pos * f_id

    print(f"\nDay 9-2: {checksum}")
