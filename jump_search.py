#Jump search algorithm, finding the index of a number in the list
import math
def solution(list, num):
    length = len(list)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and list[left] <= num:
        right = min(length - 1, left + jump)
        if list[left] <= num and list[right] >= num:
            break
        left += jump
    if left >= length or list[left] > num:
        return print(-1)
    right = min(length - 1, right)
    i = left
    while i <= right and list[i] <= num:
        if list[i] == num:
            return print(i)
        i += 1
    return print(-1)

if __name__ == '__main__':
    solution([1,2,3,4,5,6,7,8,9], 5)