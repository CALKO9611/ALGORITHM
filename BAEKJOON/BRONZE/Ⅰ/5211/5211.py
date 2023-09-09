A_Minor = ["A", "D", "E"]
C_Major = ["C", "F", "G"]

scale = input().split("|")
A_Minor_cnt, C_Major_cnt = 0, 0

for s in scale:
    if s[0] in A_Minor:
        A_Minor_cnt += 1
    elif s[0] in C_Major:
        C_Major_cnt += 1

# 개수가 같다면 맨 마지막 음악의 마지막 음으로 구별
if A_Minor_cnt == C_Major_cnt:
    if scale[-1][-1] in A_Minor:
        A_Minor_cnt += 1
    elif scale[-1][-1] in C_Major:
        C_Major_cnt += 1

if A_Minor_cnt > C_Major_cnt:
    print("A-minor")
else:
    print("C-major")
