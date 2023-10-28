N = int(input())
people = input()

cup_holder = people.count("LL")

if cup_holder <= 1:
    print(len(people))
else:
    print(len(people) - cup_holder + 1)
