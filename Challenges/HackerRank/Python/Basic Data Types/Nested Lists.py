if __name__ == '__main__':
    aswers = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        aswers[name] = score
        
    sort_orders = sorted(aswers.items(), key=lambda x: x[1], reverse=False)
    number_list = (list(set([i[1] for i in sort_orders])))
    number_list.sort()
    second_lowest_score = number_list[1]
    
    names = []
    for i in sort_orders:
        if i[1] == second_lowest_score:
            names.append(i[0])
    
    names.sort()
    for i in names:
        print(i)

 
