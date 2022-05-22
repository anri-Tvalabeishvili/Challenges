from sympy import primefactors  # შემოგვყავს ბიბლიოთეკა რომელსაც შეუძლია დაითვალოს რიცხვის prime factors
import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


# მინიმალური რიცხვი რომელსაც აქვს 4 prime factors
i = 2*3*5*7

while True:
    
    if len(primefactors(i)) == 4:  # თუ რიცხვს აქვს 4 prime factors მაშინ შევამოწმოთ ამ რიცხვზე 1-ით მეტ რიცხვს ასევე თუ აქვს 4 prime factors
        i += 1
        if len(primefactors(i)) == 4:  # თუ რიცხვს + 1 აქვს 4 prime factors მაშინ შევამოწმოთ ამ რიცხვზე 2-ით მეტ რიცხვს ასევე თუ აქვს 4 prime factors
            i += 1
            if len(primefactors(i)) == 4:  # თუ რიცხვს + 2 აქვს 4 prime factors მაშინ შევამოწმოთ ამ რიცხვზე 3-ით მეტ რიცხვს ასევე თუ აქვს 4 prime factors
                i += 1
                if len(primefactors(i)) == 4:   # თუ ბოლო რიცხვას აქვს 4 prime factors მაშინ მიგვიღია პასუხი
                    print (i-3)
                    break
    i += 1


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს
