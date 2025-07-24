def taste():
    # 2번 조건
    if S[0] != "a" or S[-1] != "a":
        return False

    # 3번 조건
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            return False
    # 4번 조건
    for i in ["a", "b", "c", "d"]:
        if S.count(i) > hamburger[ord(i) - ord("a")]:
            return False

    # 모두 만족하면 True 반환
    return True


N = int(input())
hamburger = list(map(int, input().split()))
S = input()

# taste()의 반환된 값을 통한 결과값 출력
print("Yes" if taste() else "No")
