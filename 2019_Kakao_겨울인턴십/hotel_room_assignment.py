from collections import defaultdict


def solution(k, room_number):
    answer = []

    def is_assigned(number):
        if number not in upper_room:
            upper_room[number] = number + 1
            return number

        room = is_assigned(upper_room[number])
        upper_room[number] = room + 1
        return room

    upper_room = defaultdict()

    for i in room_number:
        room = is_assigned(i)
        answer.append(room)
    return answer


k, room_number = 10, [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))
