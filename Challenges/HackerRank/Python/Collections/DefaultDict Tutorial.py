# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
Groups = defaultdict(list)

list1=[]

n, m = map(int,input().split())

for i in range(n):
    Groups[input()].append(str(i+1))

for i in range(m):
    Member_of_Group_B = input()
    if Member_of_Group_B in Groups:
         print(' '.join(Groups[Member_of_Group_B]))
    else:
         print(-1)