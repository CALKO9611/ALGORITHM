# [ 첫 번째 방법 ]
# a = input()
# word = 'ILOVEYONSEI'
# result = 0

# for i in range(len(word)) :
#     result += abs(ord(word[i]) - ord(a))
#     a = word[i]

# print(result)

# [ 두 번째 방법 ]
a = input()
result = abs(ord(a) - ord("I"))
print(result + 84)