from hw4_util import part2_get_week, print_abbreviations

test = part2_get_week(1)
for i in test:
    if i[0] == "AK":
        list = i

print(list[2:8])


