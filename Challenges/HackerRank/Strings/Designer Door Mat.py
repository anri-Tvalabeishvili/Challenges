# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split()
height = int(size[0])
width = int(size[1])

counter_line = 1
first_half_height =int( (height-1) / 2)
symbol = ".|."

# first half
for i in range(first_half_height):
    counter_symbol = (2*counter_line) - 1
    counter_line += 1
    print((symbol*counter_symbol).center(width,"-"))

# middle
print("WELCOME".center(width,"-"))


# second half
for i in range(first_half_height):
    counter_line -= 1
    counter_symbol = (2*counter_line) - 1
    print((symbol*counter_symbol).center(width,"-"))