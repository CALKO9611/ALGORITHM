name = input()

if "(" in name:
    start, end = name.index("("), name.index(")")
    print(name[: start - 1])
    print(name[start + 1 : end])
else:  # 부역명이 없다면
    print(name + "\n-")
