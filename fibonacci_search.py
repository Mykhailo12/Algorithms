#Search algorithm, that uses Fibonacci numbers
def solution(list, num):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(list):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(list)-1))
        if list[i] < num:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif list[i] > num:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return print(i)
    if fibM_minus_1 and index < (len(list)-1) and list[index+1] == num:
        return index+1
    return print(-1)

if __name__ == '__main__':
    solution([1,2,3,4,5,6,7,8,9,10,11], 11)