#Algorithm for finding natural divisors of numbers
#Дефолтний алгоритм, но най буде
def solution(n):
    for i in range(1, n):
        if n % i == 0:
            print(str(i))

if __name__ == '__main__':
    solution(12)

