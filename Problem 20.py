import math as m 

number = m.factorial(100)  # ვიგებთ რამდენია 100-ის ფაქტორიალი

listed_number = [int(x) for x in str(number)]   # რიცხვის თითოეული ციფრს ვწერთ კარგვეულ ლისთში

answer  =  sum(listed_number)  # ვკრიბავთ მოცემული ლისთის ყველა წევრს 

print(answer)





""" 
ასე შეგვიძლია დავითვალოთ ფაქტორიალი ჩაშენებული ფუნქციის გარეშე

def factorial(number):
    factor = 1
    for i in range(1,number+1):
        factor = factor * i
    print(factor)
    
"""