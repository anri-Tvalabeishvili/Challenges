from sympy import *


count = 0   # შემოგვყავს მთველი რათა დავითვალოთ Circular primes-ების რაოდენობა

for number in range(1,10**6):       # ვიღებთ სიმრავლეს რომელშიც გვაინტერესებს რამდენი Circular primes-ია

    if isprime(number):            # ვამოწმებთ მხოლოდ იმ რიცხვებს რომლებიც prime-ებია 
        number = str(number)        # რიცხვს ვწერთ სტრინგებად
        
        numbers = []            # ვქმნით ლისთს რომელშიც შევინახავთ კონრეტული რიცხვის Circular რიცხვებს
        primes = []             # ვქმნით ლისთს რათა გავიგოთ თუ რამდენი რიცხვია prime-ი მოცემული რიცხვის Circular რიცხვებიდან

        for i in range(len(number)):        # ამ ფუქნიიც ვითვლით ყველა Circular რიცხვს რომელიც გააჩნია ჩვენს რიცხვს
            number= (number[1:]) + number[0]
            numbers.append(int(number))
            

        for i in numbers:   # თუ მიღებული Circular რიცხვები არიან prime-ები მაშინ ვამატებთ primes-ების ლისთში
            if (isprime(i)):
                primes.append(i)

        if len(primes) ==len(numbers):      # ბოლოს თუ numbers-ლისთის სიგრძე დაემთხვევა primes-ის ლისთის სიგრძეს მაშინ ითველბა რომ საწყისი რიცხვი Circular primes
            count += 1          # ამ შედარებით ვრწმუნდებით იმაში რომ მოცემული რიცხვის ყველა Circular- ციფრი ნამდვილად primes-ია
            

print(count)