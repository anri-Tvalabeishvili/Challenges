# Enter your code here. Read input from STDIN. Print output to STDOUT

Students, Subjects = map(int,input().split())

sheet = []
for i in range(Subjects):
    sheet.append( list(map(float, input().split())) ) 



for i in zip(*sheet): 
     print( sum(i)/len(i) )