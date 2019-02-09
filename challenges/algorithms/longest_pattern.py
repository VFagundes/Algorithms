class Solution:

    def find_longest_pattern(self, input):
        no_duplicates = len(set(input))
        if no_duplicates == len(input):
            return ''

        n = len(input)
        longest_value = [[0 for _ in range(n + 1)]
                         for _ in range(n + 1)]

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


c = Solution()

print(c.find_longest_pattern('abcwxyzabghwxyz'))
print(c.find_longest_pattern('azbycxdwev'))
print(c.find_longest_pattern('abcaeabcaeabcdabcd'))
