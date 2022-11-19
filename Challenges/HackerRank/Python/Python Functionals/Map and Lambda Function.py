cube = lambda x: x**3 # complete the lambda function 


def fibonacci(n):
    fibonacci_list = [0,1]
    # return a list of fibonacci numbers
    for i in range(n-2):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[:n]

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))