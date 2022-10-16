# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    answer = True
    try:
        reg = re.compile(input())
    except re.error:
        answer = False
        
    print(answer)