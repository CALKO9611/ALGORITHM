party_people = [input() for _ in range(5)]
photo = [""] * 5  # 변환할 값 저장할 문자열 리스트

for i in range(len(party_people[0])):
    # people_mod // 5줄을 세로로 한 줄 씩 보았을 때의 문자열 값 저장
    people_mod = (
        party_people[0][i]
        + party_people[1][i]
        + party_people[2][i]
        + party_people[3][i]
        + party_people[4][i]
    )

    if people_mod == ".omln":  # 도약 준비 → 도약 중
        photo[0] += "o"
        photo[1] += "w"
        photo[2] += "l"
        photo[3] += "n"
        photo[4] += "."
    elif people_mod == "owln.":  # 도약 중 → 도약 준비
        photo[0] += "."
        photo[1] += "o"
        photo[2] += "m"
        photo[3] += "l"
        photo[4] += "n"
    else:  # 착석
        photo[0] += "."
        photo[1] += "."
        photo[2] += "o"
        photo[3] += "L"
        photo[4] += "n"

for p in photo:  # 출력
    print(p)
