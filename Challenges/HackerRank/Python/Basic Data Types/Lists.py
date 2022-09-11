if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0,N):
        comand=input().split();
        
        if comand[0] == "insert":
            lst.insert(int(comand[1]),int(comand[2]))
        elif comand[0] == "print":
            print(lst)
        elif comand[0] == "remove":
            lst.remove(int(comand[1]))
        elif comand[0] == "append":
            lst.append(int(comand[1]))
        elif comand[0] == "sort":
            lst.sort()
        elif comand[0] == "pop":
            lst.pop()
        elif comand[0] == "reverse":
            lst.reverse()