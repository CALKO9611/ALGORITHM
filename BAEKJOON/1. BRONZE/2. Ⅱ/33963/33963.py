N = input()
N_digit = len(N)
click = 0

while True:
    N = str(int(N) * 2)

    if N_digit < len(N):
        break
    else:
        click += 1

print(click)
