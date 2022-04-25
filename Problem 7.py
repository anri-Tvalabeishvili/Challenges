import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


list = []  # ვქმნით ლისთს საჭირო ციფრების შესანახად
number = 1  # საწყისი ციფრი

while len(list)< 10001:  # ძებნის ციკლს ვაგრძელებთ მანამ სანამ 10001-ე წევრს არ ვიპოვით
    
    number += 1     # ყოველი ციკლის შემდეგ წაყის ციფრს ვზრდით ერთით
    prime = True    # ვაძლევთ სიმათლის მნიშვნელობას
    for i in range(2,int(number**0.5) + 1): # ციკლის მეშვეობით ვიგებთ არის თუ არა მოცემული ციფრი prime
        if (number % i==0):
            prime = False
    if prime:               # თუ ციფრი არის prime მაშინ ვამატებთ სიაში
       list.append(number)  
       


print(list[-1])  # ვიღებთ უკანასკნელ ციფრს ლისთიდან




""" 
prime_number= 0
number = 1 

while prime_number < 10001:
    
    number = number + 1 
    prime = True
    for i in range(2,int(number**0.5) + 1):
        if (number % i==0):
            prime = False
    if prime:
       prime_number += 1
       
       if prime_number==10001:
           print(number)
    
 """


end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს