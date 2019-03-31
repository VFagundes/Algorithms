input = [4, 73, 67, 38, 33]
result = []
result.append(input[0])

for i in input[1:]:
    diff = 5 - (i % 5)
    if diff < 3 and i >= 38:
        result.append(i+diff)
    else:
        result.append(i)


print result