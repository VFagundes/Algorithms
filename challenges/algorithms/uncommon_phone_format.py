
strs =['00-44  48 5555 8361',
       '0 - 22 1985--324',
       '555372654']


def solution(S):
    cleanedS = S.replace('-', '').replace(' ', '')
    result = []
    str_length= len(cleanedS)
    for i in range(1, str_length + 1):
        result += cleanedS[i - 1]
        if i % 3 == 0 and i != len(cleanedS):
            result += '-'

    result_length=len(result)
    last_chars= result[result_length-2:]
    if '-' in last_chars:
        result.insert(result_length-3, result.pop(result_length-2))

    return ''.join(result)

for i in strs:
    print solution((i))
