cur_pos = input()
row = int(cur_pos[1])
col = int(ord(cur_pos[0]) - ord('a')) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
count = 0

for i in range(len(steps)):
    next_row = row + steps[i][1]
    if next_row < 1 or next_row > 8:
        continue
    next_col = col + steps[i][0]
    if next_col < 1 or next_col > 8:
        continue
    count += 1

print(count)

