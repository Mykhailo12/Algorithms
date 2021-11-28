#Algorithm for checking numbers for simplicity

def solution(n):
    d = 2
    while n % d != 0 and d * d <= n:
        d += 1
    return d*d>n

if __name__ == '__main__':
    print(solution(3))
