from collections import defaultdict
from itertools import count
from string import ascii_lowercase

class Solution:

    def find_longest_pattern(self, input):
        no_duplicates = len(set(input))
        if no_duplicates == len(input):
            return ''

        n = len(input)
        longest_value = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        res_length = 0

        index = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):

                if (input[i - 1] == input[j - 1] and
                        longest_value[i - 1][j - 1] < (j - i)):
                    longest_value[i][j] = longest_value[i - 1][j - 1] + 1

                    if (longest_value[i][j] > res_length):
                        res_length = longest_value[i][j]
                        index = max(i, index)

                else:
                    longest_value[i][j] = 0
        longest_pattern = ''
        if (res_length > 0):
            for i in range(index - res_length + 1,
                           index + 1):
                longest_pattern = longest_pattern + input[i - 1]

        return longest_pattern

    def getsubs(self, loc, s):
        substr = s[loc:]
        i = -1
        while substr:
            yield substr
            print(s[loc:i + 1] if s[loc:i + 1] else s[loc:i])
            substr = s[loc:i]
            i -= 1

    def find_longest_pattern2(self, r):
        occ = defaultdict(int)
        for i in range(len(r)):
            for sub in self.getsubs(i, r):
                occ[sub] += 1
        filtered = [k for k, v in occ.items() if v >= 2]
        if filtered:
            maxkey = max(filtered, key=len)
            return maxkey

    def long_alphabet(self, input_string):
        maxsubstr = input_string[0:0]  # empty slice (to accept subclasses of str)
        for start in range(len(input_string)):  # O(n)
            for end in count(start + len(maxsubstr) + 1):  # O(m)
                substr = input_string[start:end]  # O(m)
                if len(substr) != (end - start):  # found duplicates or EOS
                    break
                if sorted(substr) == list(substr):
                    maxsubstr = substr
        return maxsubstr

    def getsubs2(self, loc, s):
        substr = s[loc:]
        i = -1
        while substr:
            yield substr
            substr = s[loc:i]
            i -= 1

    def find_longest_alphabetically_pattern(self, r):
        groups = []
        for i in range(len(r)):
            for sub in self.getsubs2(i,r):
                if len(sub) > 1:
                    groups.append(sub)

        letters = ascii_lowercase
        filtered = []
        for group in groups:
            if group in letters:
                filtered.append(group)
        if filtered:
            return max(filtered,key=len)
        return ''

x = Solution()

print(x.find_longest_alphabetically_pattern("abcaeabcaeabcdabcd"))
print(x.find_longest_alphabetically_pattern("acwxyzabghwxyo"))
print(x.find_longest_alphabetically_pattern("azbycxdwev"))

