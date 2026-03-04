N, M = map(int, input().split())
A = list(map(int, input().split()))

print("DIMI" if sum(A) - N >= M else "OUT")
