word = input().upper()
new_word = list(set(word))

cnt_list = []
for x in new_word:
    cnt = word.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(new_word[max_index])
