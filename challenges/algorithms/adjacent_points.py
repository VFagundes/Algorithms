challenge = [0, 3, 3, 7, 5, 3, 11, 1]

NOT_ADJACENT_VALUE= 100000001

def set_contract_response(distance_value):
    if distance_value>NOT_ADJACENT_VALUE:
        return-2
    elif distance_value!= 0:
        return -1
    return distance_value



def solution(A):
    minimum= NOT_ADJACENT_VALUE
    arr_length = len(A)
    for i in range(arr_length):
        if i + 1 > arr_length:
            break

        current_element=A[i]
        next_element=A[+1]
        distance = abs(current_element - next_element)
        if distance<minimum:
            minimum= distance

    return set_contract_response(minimum)

