# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.


sample_input = [7, 11, 5, 15, 3, 2, -2, 2, 1, 5, -6]

starting_point = 7
ending_point = 11
appleTree = 5
orange_tree = 15
apples = [-2, 2, 1]
oranges = [5, -6]
apple_count = filter(lambda x: x + appleTree >= starting_point and x + appleTree <= ending_point, apples)

orange_count = filter(lambda x: x + orange_tree>= starting_point and x + orange_tree <= ending_point, oranges)

print len(apple_count)
print len(orange_count)
