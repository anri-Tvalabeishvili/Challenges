from sympy import *
import time          #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
 

start = time.time()     # ვიწყებთ დროის ათვალს
primes = (list(primerange(1, 1e4)))     # ვქმნით ლისთს სადაც იქნება ყველა მარტივი რიცხვი

# ვქმნით ცვალდს სადაც შევინახავთ მარტივი რიცხვების ჯამის სიგრძეს
length = 21      # საყისად ვიღებთ 21 ამოცანის პირობიდან გამომდინარე
number = 0       # ვქმნით ცვლადს სადაც შევინახავთ ისეთ რიცხვს რომელიც აკმაყოფილებს ჩვენს პირობას

# ვქმნით ჩადგმულ ციკლს რომლის ინდექსების მეშვეობით დავაგენერირებთ
# ყველა შესაძლო კომბინაციას რომელიც შეიძლება მივიღოთ primes-ლისთისგან
for i in range(len(primes)-1):

    for k in range(len(primes),i,-1):
        # თუ მოცემული სიმრავლე დააკამყოფილებს ამ პირობებს მაშინ ვუშვებთ შემდეგ ლოგიკას
        if isprime(sum(primes[i:k])) and len(primes[i:k]) > length and sum(primes[i:k]) < 1e6:  
            # ძველ სიგრძეს ვცვლით ახალი სიგრძით და ხელმეორედ ვუშვებთ ციკლს იმის შესამოწმებლად 
            # არსებობს თუ არა სხვა რიცხვი რომელიც უფრო დიდი სიგრძის მატარებელია
            length = len(primes[i:k])
            number = sum(primes[i:k])
           

print(f"The longest sum of consecutive primes below one-million that adds to a prime, contains {length} terms, and is equal to {number}.")
print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს