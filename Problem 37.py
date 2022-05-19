from sympy import *
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


def left_to_right_Truncatable(numbers):
    number = str(numbers)
    counter = 1
    for i in range(len(number)-1):
        number = number[1:]
        
        if isprime(int(number)):
            counter += 1
    if counter == len(str(numbers)):
        return True



def right_to_left_Truncatable(numbers):
    number = str(numbers)
    counter = 1
    for i in range(len(number)-1):
        number = number[:-1]
        
        if isprime(int(number)):
            counter += 1
    if counter == len(str(numbers)):
        return True




answers = []
number = 10

while len(answers) < 11 :
    number += 1

    if isprime(number) and left_to_right_Truncatable(number) and right_to_left_Truncatable(number):
        answers.append(number)


print(sum(answers))

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს