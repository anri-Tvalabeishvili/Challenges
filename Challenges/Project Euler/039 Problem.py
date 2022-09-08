from collections import Counter
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()



perimeters = []     # ვქმნით ლისთს სადაც შევინახავთ ყველა შესაძლო პერიმეტრს

limit = int(1000)

for a in range(1, int(limit/2)):
    for b in range(a, int(limit/2)):
        c = (a**2 + b**2)**0.5
        perimeter = a + b + c
        if  c == int(c) and perimeter <= limit:
            perimeters.append(int(perimeter))


p = Counter(perimeters) # ვითვლით რამდენჯერ განმეორდა გარკვეული პერიმეტრი არსებულ სიაში


print (p.most_common(1)) # გვაჩვენებს ყველაზე უფრო ხშირად გამეორებულ პერიმეტს


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს