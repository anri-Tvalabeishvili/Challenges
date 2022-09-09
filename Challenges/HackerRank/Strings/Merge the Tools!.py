def merge_the_tools(string, k):
    # your code goes here
    partitions_Number = int(len(string) / k)

    for i in range(partitions_Number):
        T = string[ (i*k) : (k*(i+1)) ]
        U= ""
           
        for i in T:
            if i not in U:
                U += i  
                           
        print(U)
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)