lst_1 = [int(input()) for _ in range(5)]
lst_2 = set(lst_1)

for i in lst_2:
    if lst_1.count(i) % 2 == 1:
        print(i)
