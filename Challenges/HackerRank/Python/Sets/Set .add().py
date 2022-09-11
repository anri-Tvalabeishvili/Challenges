# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
countries = set()
for i in range(int(N)):
    country  = input()
    countries.add(country)
    
print(len(countries))