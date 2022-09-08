import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


def is_Pentagon(number):                # google-ში ნაპოვნი ფორმულის გამოყენებით ვამოწმებთ არის თუ არა რიცხვი pentagonal
    if ((24*number+1)**0.5  + 1) % 6 == 0:
        return True
    return False



Stop = True

i = 1

while Stop :
    for k in range(1,i):
        a = i*(3*i-1)/2         # ინდექსები მიხედვით ვქმნით pentagonal რიცხვს
        b = k*(3*k-1)/2         # ინდექსები მიხედვით ვქმნით pentagonal რიცხვს

        if is_Pentagon(a+b) and is_Pentagon(a-b):  # თუ მიღებული pentagonal-ი რიცხვების სხვაობა და ჯამი არის ისევ pentagonal -რიცხვი მაშინ ვწყვეტთ კოდს
            print(int(a-b))     # ვპრინტავთ ამ რიცხვების სხვაობას
            Stop = False        # ამით ვაჩერებთ while ციკლს
            break       # ამით ვაჩერებთ for ციკლს
    i +=1       # ნელ ნელა ვზრდით ინდექსებს სანამ არ ვიპოვით პასუხს და არ შევწყვეტთ ციკლს



print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს
