import string
word = """we promptly judged antique ivory buckles for the next prize
we promptly judged antique ivory buckles for the prizes
the quick brown fox jumps over the lazy dog
the quick brown fox jump over the lazy dog"""

def check_pangram(word):
    alphabet = []
    for i in string.lowercase:
        alphabet.append(i)
    arr = word.split('\n')
    return_values=[]
    for w in arr:
        for j in alphabet:
            if not j in w:
                return_values.append('0')
                break
            elif j == 'z':
                return_values.append('1')
    return ''.join(return_values)





print(check_pangram(word))
    

