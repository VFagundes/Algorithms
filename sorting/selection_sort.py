import default_data

ini = 0
end = 10000

array = default_data.get_default_array(ini, end)
asserted = list(array)

index = 0


def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b


for index in range(0, len(array)):

    current = array[index]
    for i in range(index + 1, len(array)):
        next_n = array[i]

        if next_n < current:
            next_n, current = swap(next_n, current)
            array[index], array[i] = current, next_n

asserted.sort()

assert asserted == array
print 'well done'