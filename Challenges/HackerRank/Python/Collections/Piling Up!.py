# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))

    last_block = max(blocks[0], blocks[-1])
    while True:
        
        if len(blocks) > 1 :
            right = blocks[-1]
            left = blocks[0]

            if last_block < right or last_block < left:
                print("No")
                break            
            

            if right > left:
                last_block = right
                blocks = blocks[0:-1]
                
            else:
                last_block = left
                blocks = blocks[1:]
                
        
        elif len(blocks) == 1 and  last_block >= blocks[0]:
            print("Yes")
            break
        

