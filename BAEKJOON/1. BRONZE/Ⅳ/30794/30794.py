keyNote = input().split()

if keyNote[1] == "miss":
    print(0)
elif keyNote[1] == "bad":
    print(200 * int(keyNote[0]))
elif keyNote[1] == "cool":
    print(400 * int(keyNote[0]))
elif keyNote[1] == "great":
    print(600 * int(keyNote[0]))
elif keyNote[1] == "perfect":
    print(1000 * int(keyNote[0]))
