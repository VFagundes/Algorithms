# must connect related points a to b then to n (the last number)
def is_connected_to_n(A, B, N):
    return A == N or B == N


def solutionC(A, B, N):
    length = len(B)
    connections = []
    for i in range(length):
        if A[i] in B or B[i] in A:
            if not connections:
                connections.append((A[i], B[i]))
            else:
                connected_points = []
                for c in connections[0]:
                    connected_points.append(c)

                last_index = len(connected_points) - 1
                if A[i] <= connected_points[last_index] or B[i] <= connected_points[last_index]:
                    connections.append((A[i], B[i]))
                if i== N-1 and  is_connected_to_n(A[i],B[i],N):
                    connections.append((A[i], B[i]))


    return len(connections)

#
# a = [1, 2, 3, 3]
# b = [2, 3, 1, 4]
# n = 4
#
# print(solutionC(a, b, n))
#
# a = [1, 2, 4, 5]
# b = [2, 3, 5, 6]
# n = 6
#
# print(solutionC(a, b, n))
