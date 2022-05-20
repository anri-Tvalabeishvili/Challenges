from sympy import *
from itertools import permutations
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()



Pandigital = '1234567'    # ზუსტად არ ვიცით რამდენ ნიშნა იქნება ეს რიცხვი ამიტომ 9-ნიშნიდან ნელ-ნელ მოვყვებით ქვემოთ. ბოლოს მივიღებთ რომ პირველი ასეთი რიცხვი 7 ნიშნაა


P9 = list(permutations(Pandigital))     # ვქმნით n-ნიშნა რიცხვის ყველა შესაძლო კომბინაციას
P9.reverse()        # ვალაგებთ კლების მიხედვით რადგან უდიდესი გვაინტერესებს


for i in (P9):  # სათითაოდ ვიღებთ ყველა კომბინაციას
    number = ""
    for k in i:     # ამ for ლუპის დახმარებით თითოეულ კომბინაციას ვაძლევთ str(რიცხვის ფორმას)
        number +=k
    
    if isprime(int(number)):    # და ბოლოს თუ ეს რიცხვი იქნება prime მაშინ პასუხი მიღებულია და ვწყვეტთ ციკლს.         (მაქსიმალური ისედაც იქნება რადგან კლებადობითაა დალაგებილი)
        print(number) # ტერმინალში გამოგვყავს პასუხი
        break
    



print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს





# ეს კოდიც ზუსტად იგივეს აკეთებს რასაც ზემოთა უბრალოდ აქ ყველაფერი ავტომატურად ხდება არ გვიწევს ხელით შევცვალოთ Pandigital-ის მნიშვნელობები მაგ:
#                                                                                                                           '123456789' დან '12345678'-მდე


""" 

Pandigital = '123456789'
stop = False


for i in range(8):
    P9 = list(permutations(Pandigital))
    P9.reverse()

    Pandigital_len = len(Pandigital)
    Pandigital = Pandigital[:Pandigital_len-1]

    for i in (P9):
        number = ""
        for k in i:
            number +=k
        
        if isprime(int(number)):
            print(number)
            stop = True
            break
    if stop :
        break

"""
        

