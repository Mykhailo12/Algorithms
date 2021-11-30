#Algorithm for finding the factorial of a number

def solution(n):
    if n == 0:
        return print(1)
    f = 1
    i = 0
    while i < n:
        i += 1
        f = f * i
    return print(f)

if __name__ == '__main__':
    solution(12)