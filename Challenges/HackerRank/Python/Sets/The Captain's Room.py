# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_groups = int(input())

number_of_rooms = input().split()
number_of_rooms_set = set(number_of_rooms)

for i in number_of_rooms_set:
    number_of_rooms.remove(i)
    
Captain_room = list(number_of_rooms_set.difference  (set(number_of_rooms)))

print(Captain_room[0])


