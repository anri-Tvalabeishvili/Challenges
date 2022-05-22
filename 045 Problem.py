import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


def is_Pentagon(number):                # google-ში ნაპოვნი ფორმულის გამოყენებით ვამოწმებთ არის თუ არა რიცხვი pentagonal
    if ((24*number+1)**0.5  + 1) % 6 == 0:
        return True
    return False


def is_Hexagonal(number):               # google-ში ნაპოვნი ფორმულის გამოყენებით ვამოწმებთ არის თუ არა რიცხვი Hexagonal
    if ((8*number+1)**0.5  + 1) % 4 == 0:   
        return True
    return False


counter = 0     # შემოგვყავს მთველი რომ while ციკლი გავაჩეროთ
number = 1      # შემოგვყავს ცვლადი რომელიც წარმოადგენს ინდექსს

while counter<=2:

    Triangle = (number*(number+1))/2        # ინდექსის მიხედვით ვითვლით Triangle რიცხვს

    if is_Pentagon(Triangle) and is_Hexagonal(Triangle):    #  თუ ეს Triangle რიცხვი ერთდროულად არის pentagonal და  Hexagonal მაშინ ვპრინტავთ მას და მთველს ვუამტებთ 1
        print(int(Triangle))    # ტერმინალში გამოგვყავს რიცხვი
        counter += 1        # მთვლელს ვუმატებთ 1 რათა მეორე დაპრინტულ რიცხვზე while ციკლი გავაჩეროთ 
    
    number += 1     # სანამ არ ვიპოვით შესაბამის რიცხვებს ინდექსს ვზრდით 1-ით


print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს
