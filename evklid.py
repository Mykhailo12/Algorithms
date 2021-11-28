#Euclid's algorithm
#It is used to find the natural greatest divisor of two numbers

def solution(a, b):
    while a > 0 and b > 0:
        a,b = b, a % b

    return a + b

if __name__ == '__main__':
    print(solution(18, 30))