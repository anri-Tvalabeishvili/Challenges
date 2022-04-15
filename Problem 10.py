import time

start = time.time()


list = [0,]  # ვქმნით ლისთს საჭირო ციფრების შესანახად
number = 1  # საწყისი ციფრი

while list[-1] < 2000000:  # ძებნის ციკლს ვაგრძელებთ მანამ სანამ 10001-ე წევრს არ ვიპოვით
    
    number += 1     # ყოველი ციკლის შემდეგ წაყის ციფრს ვზრდით ერთით
    prime = True    # ვაძლევთ სიმათლის მნიშვნელობას
    for i in range(2,int(number**0.5) + 1): # ციკლის მეშვეობით ვიგებთ არის თუ არა მოცემული ციფრი prime
        if (number % i==0):
            prime = False
    if prime:               # თუ ციფრი არის prime მაშინ ვამატებთ სიაში
       list.append(number)  
       

del list[-1]
print(sum(list))  # ვიღებთ უკანასკნელ ციფრს ლისთიდან


end = time.time()

print( end- start)