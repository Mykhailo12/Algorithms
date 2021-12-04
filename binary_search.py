#Binary search algorithm, finding a number
def solution(num_list, num):
    first = 0
    last = len(num_list)-1
    i = -1
    while (first <= last) and (i == -1):
        mid = (first+last)//2
        if num_list[mid] == num:
            i = mid
        else:
            if num<num_list[mid]:
                last = mid -1
            else:
                first = mid +1
    return print(i)

if __name__ == '__main__':
    solution([6, 17, 21, 27, 32, 35, 35, 36, 37, 48], 48)