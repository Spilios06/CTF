import fileinput

obj = []

for l in fileinput.input():
    obj.append(l)

colums = int(obj[0], 10)

map = lines[1:]
map = [line.strip() for line in map]

answere = 0
for c in range(1, len(map[0]) - 1):
    holding = False
    for r in range(colums):
        if map[r][c] == '-':
            if holding:
                holding = False
                continue
            else:
                answere += 1

                if r + 1 < colums and map[r + 1][c] == '#':
                    holding = True

                continue

    print(answere)
