N, Name = input().split()
result = ""

# 1
abandonedText = 0  # 버려진 문자
for i in Name:
    if i not in result:
        result += i
    else:
        abandonedText += 1

# 2, 3
result = str(int(N) + 1906) + result + str(abandonedText + 4)

# 4, 5
result = "smupc_" + result[::-1]

print(result)
