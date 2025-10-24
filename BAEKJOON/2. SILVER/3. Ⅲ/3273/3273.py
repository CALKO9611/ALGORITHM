n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())
s, e = 0, n - 1  # start, end
result = 0

while s < e:
    if numbers[s] + numbers[e] < x:
        s += 1
    elif numbers[s] + numbers[e] > x:
        e -= 1
    else:  # x 값과 같을 때
        result += 1
        s += 1

print(result)
