N = int(input())
problem_level = [int(input()) for _ in range(N)]

if problem_level[0] == min(problem_level):
    print("ez")
elif problem_level[0] == max(problem_level):
    print("hard")
else:
    print("?")
