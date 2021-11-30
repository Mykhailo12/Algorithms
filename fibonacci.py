#algorithm for finding a number in a series of Fibonacci numbers by index
def solution(n):
    fib1 = fib2 = 1
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1

    return print(fib2)

if __name__ == '__main__':
    solution(3)