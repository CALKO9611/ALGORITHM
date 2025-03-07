digital_humanities = ["social", "history", "language", "literacy"]
topic = input()

for i in digital_humanities:
    if i in topic:
        print("digital humanities")
        exit(0)

print("public bigdata")
