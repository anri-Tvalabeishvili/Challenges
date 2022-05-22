from sympy import *
from itertools import permutations
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


Pandigital = '0123456789'    # ზუსტად არ ვიცით რამდენ ნიშნა იქნება ეს რიცხვი ამიტომ 9-ნიშნიდან ნელ-ნელ მოვყვებით ქვემოთ. ბოლოს მივიღებთ რომ პირველი ასეთი რიცხვი 7 ნიშნაა


P9 = list(permutations(Pandigital))     # ვქმნით n-ნიშნა რიცხვის ყველა შესაძლო კომბინაციას
P9.reverse()        # ვალაგებთ კლების მიხედვით რადგან უდიდესი გვაინტერესებს

sum = 0     # შემოგვყავს ცვლადი რომელშიც დავამატებთ ყველა sub-string divisibility რიცხვს

for i in P9:
    number = ""
    for k in i:     # ამ for ლუპის დახმარებით თითოეულ კომბინაციას ვაძლევთ str(რიცხვის ფორმას)
        number +=k

    if int(number[1:4]) % 2 == int(number[2:5]) % 3 == int(number[3:6]) % 5 == int(number[4:7]) % 7 == int(number[5:8]) % 11 == int(number[6:9]) % 13 == int(number[7:10]) % 17 == 0:
        sum += int(number)  # თუ ყველაფერი აკმაყოფილებს ზემოთ აღნიშნულ ლოგიკას მაშინ ეს რიცხვი sub-string divisibility-ია და ვამატებთ ჯამში
        
print(sum)          # ტერმინალში გამოგვყავს პასუხი


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს

