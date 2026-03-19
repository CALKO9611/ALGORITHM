N = int(input())
days = [0, 0, 0, 0, 0]  # 월, 화, 수, 목, 금

for _ in range(N):
    day = int(input())
    days[day - 1] = 1

print("YES" if 0 in days else "NO")
