sentence = "chandramukhi champaklal chhatriwala"
for ch in "abcdefghijklmnopqrstuvwxyz":
    count = 0
    for i in sentence:
        if i == ch:
            count += 1
    if count > 0:
        print(ch, "=", count)
