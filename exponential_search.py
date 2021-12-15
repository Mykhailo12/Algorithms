#Exponential search for the index of a number in a list
def BinarySearch(list, num):
    first = 0
    last = len(list)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if list[mid] == num:
            index = mid
        else:
            if num<list[mid]:
                last = mid -1
            else:
                first = mid +1
    return print(index)

def solution(list, num):
    if list[0] == num:
        return 0
    index = 1
    while index < len(list) and list[index] <= num:
        index = index * 2
    return BinarySearch( list[:min(index, len(list))], num)

if __name__ == '__main__':
    solution([1,2,3,4,5,6,7,8], 3)


