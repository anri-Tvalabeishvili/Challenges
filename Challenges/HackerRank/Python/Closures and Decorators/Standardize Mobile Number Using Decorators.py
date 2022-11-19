def wrapper(f):
    def fun(l):
        # complete the function
        f(["+91 "+i[-10:-5]+" "+i[-5:] for i in l])   
        # for i in l:
        #     f(["+91 " + i[-10:-5] + " " + i[-5:]])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


