num = input()

num = [n for n in num]

for i in range(len(num)):
    cur_num = int(num[i])
    inverted_num = 9 - cur_num

    if inverted_num < cur_num:
        if i == 0 and inverted_num == 0:
            pass
        else:
            num[i] = str(inverted_num)

print(int("".join(num)))