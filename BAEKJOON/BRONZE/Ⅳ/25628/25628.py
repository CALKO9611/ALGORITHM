# [두 번째 풀이]

A, B = map(int, input().split())
print(min(A // 2, B))

# [첫 번째 풀이]
# A, B = map(int, input().split())
# cnt = 0

# while 1 :
#     if A >= 2 and B >= 1 :
#         cnt += 1
#         A -= 2
#         B -= 1

#     if A < 2 or B < 1 :
#         break

# print(cnt)
