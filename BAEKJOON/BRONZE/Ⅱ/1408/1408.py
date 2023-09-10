nh, nm, ns = map(int, input().split(":"))  # 지금 시, 분, 초
mh, mm, ms = map(int, input().split(":"))  # 임무 시, 분, 초

# 임무 시간 - 지금 시간
result = (mh * 3600 + mm * 60 + ms) - (nh * 3600 + nm * 60 + ns)

if result < 0:  # 임무 시간이 지금 시간 보다 작을 때
    result += 60 * 60 * 24  # 24시간을 더해줌

h = result // 3600
m = (result % 3600) // 60
s = result % 60

print("{}:{}:{}".format(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2)))
