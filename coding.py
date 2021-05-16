# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#
#     stack = [0 for _ in range(bridge_length)]
#
#     for i in range(len(truck_weights)):
#
#         stack.append(truck_weights[i])
#         stack.pop(0)
#         answer += 1
#
#
#         if i == len(truck_weights)-1:
#             while sum(stack) != 0:
#                 stack.append(0)
#                 stack.pop(0)
#                 answer += 1
#         else:
#             while sum(stack) + truck_weights[i + 1] > weight:
#                 stack.append(0)
#                 stack.pop(0)
#                 answer += 1
#
#     return answer
#
#
# solution(2,10,[7,4,5,6])

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0 for _ in range(bridge_length)])

    for i in range(len(truck_weights)):
        bridge.append(truck_weights[i])
        bridge.popleft()
        answer += 1

        if i == len(truck_weights) - 1:
            answer += bridge_length
        else:
            while True:
                bridge.popleft()
            if sum(bridge) + truck_weights[i + 1] > weight:
                bridge.append(0)
                answer += 1
            else:
                break
    return answer

solution(2,10,[7,4,5,6])