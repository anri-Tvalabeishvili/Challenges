import math as m 
import time
start = time.time()

number = m.factorial(100)  # ვიგებთ რამდენია 100-ის ფაქტორიალი

listed_number = [int(x) for x in str(number)]   # რიცხვის თითოეული ციფრს ვწერთ კარგვეულ ლისთში

answer  =  sum(listed_number)  # ვკრიბავთ მოცემული ლისთის ყველა წევრს 

print(answer)

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს



""" 
ასე შეგვიძლია დავითვალოთ ფაქტორიალი ჩაშენებული ფუნქციის გარეშე

def factorial(number):
    factor = 1
    for i in range(1,number+1):
        factor = factor * i
    print(factor)
    
"""