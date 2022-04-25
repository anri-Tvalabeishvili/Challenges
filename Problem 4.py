import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

palindromic_numbers = []   # ვქმნით სიას რათა შევინახოთ ყველა palindrom-ული რიცხვი 

for i in range(100,999):   # ვქმნით for-ლუპს პირველი მამრავლისთვის
    for k in range(100,999):    # ვქმნით for-ლუპს მეორე მამრავლისთვის
        Number = str(i*k)       # ვამრავლებთ ამ რიცხვებს და ვწერთ str-ებში
        if Number == Number[::-1] :     # თუ ეს რიცხვი წაღმა და უკუღმაც ერნაირია მაშინ ვამატებთ მას სიაში

            palindromic_numbers.append(i*k)


print(max(palindromic_numbers)) # სიიდან ვიღებთ უდიდესს 

end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს