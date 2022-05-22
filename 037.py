from sympy import *
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


def left_to_right_Truncatable(numbers):  # მარცხნიდან მარჯვნივ ნელ-ნელა აცილებს რიცხვებს
    number = str(numbers)       # რიცხვს ვწერთ სტრინგათ რათა უკეთესად ვიმანიპულიროთ 
    counter = 1                 # შემოგვყავს მთველი
    for i in range(len(number)-1):      # რიცვს წინიდან რიგრიგობით ვაცილებთ იმდენ ციფრს სანამ ბოლოს 1-სიბოლო არ დარჩება
        number = number[1:]         # ამით პირველი ციფრის გარდა ყველა ციფრს ვტოვებთ
        
        if isprime(int(number)):    # თუ უკვე 1-ციფრ ჩამოშორებული რიცხვი მარტივია მაშინ მთვლელს დავამატებთ 1-ს
            counter += 1
    if counter == len(str(numbers)):    # თუ ბოლოში მთველის მნიშვნელობა გაუტოლდება საწყისი რიცხვის, ციფრთა ჯამს ესეიგი, ეს რიცხვი Truncatable-ია
        return True



def right_to_left_Truncatable(numbers): # მარჯვნიდან მარცხნივ ნელ-ნელა აცილებს რიცხვებს
    number = str(numbers)   # რიცხვს ვწერთ სტრინგათ რათა უკეთესად ვიმანიპულიროთ 
    counter = 1         # შემოგვყავს მთველი
    for i in range(len(number)-1):  # რიცვს ბოლოდან რიგრიგობით ვაცილებთ იმდენ ციფრს სანამ ბოლოს 1-სიბოლო არ დარჩება
        number = number[:-1]    # ამით ბოლო ციფრის გარდა ყველა ციფრს ვტოვებთ
        
        if isprime(int(number)):    # თუ უკვე 1-ციფრ ჩამოშორებული რიცხვი მარტივია მაშინ მთვლელს დავამატებთ 1-ს
            counter += 1
    if counter == len(str(numbers)): # თუ ბოლოში მთველის მნიშვნელობა გაუტოლდება საწყისი რიცხვის, ციფრთა ჯამს ესეიგი, ეს რიცხვი Truncatable-ია
        return True




answers = []  # ვქმნით პასუხების სიას სადაც შევინაავთ ყველა Truncatable რიცხვს
number = 10     # ათვლას ვიწყებთ 10-დან

while len(answers) < 11 :       #  თუ სიის ელემენტების რაოდენობა გადაცდება 11-მაშინ კოდს ვაჩერებთ, რადგან მხოლო პირველი 11 Truncatable-ი გვაინტერესებს
    number += 1     # ყოველი ციკლის შემდეგ საცდელ ციფრს ვზრდით 1-ით

    if isprime(number) and left_to_right_Truncatable(number) and right_to_left_Truncatable(number): # თუ საცდელი ციფრი prime-ია და ამავდოულად Truncatable-ია ორივე მხრიდან
        answers.append(number)      # მაშინ მას ვამატებთ პასუხების ლისთში


print(sum(answers))     # საბოლოო პასუხად ვწერთ 11-ივე Truncatable რიცხვის ჯამს

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს