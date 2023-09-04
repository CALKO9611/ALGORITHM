cnt = 0

for i in range(8):
    horse = input()
    if i % 2 == 0:
        for j in range(0, 8, 2):
            if horse[j] == "F":
                cnt += 1
    elif i % 2 != 0:
        for j in range(1, 8, 2):
            if horse[j] == "F":
                cnt += 1
print(cnt)
