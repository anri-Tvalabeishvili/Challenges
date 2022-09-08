if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    numbers = list(set(arr))
    numbers.sort()
    
    print(numbers[-2])
