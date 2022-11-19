# Enter your code here. Read input from STDIN. Print output to STDOUT

value = input()

lowercase = []
uppercase = []
even = []
odd = []

for letter in value:
    
    if letter.isdigit():
        if int(letter) % 2 == 0:
            even.append(letter)
        else:
            odd.append(letter)
    else:
        if letter.islower():
            lowercase.append(letter)
        else:
            uppercase.append(letter)

            
lowercase.sort()
uppercase.sort()
odd.sort()
even.sort()

odd = map(str, odd)
even = map(str, even)

answer = "".join(lowercase) + "".join(uppercase) + "".join(odd) + "".join(even)

print(answer)