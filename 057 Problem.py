"""  მოცემული დავალება მოითხოვს მათემატიკურუ აპარატის გარკვეულ ნაწილს დეტალური ახსნა შეგიძლიათ იხილილოთ
    Data-საქაღალდეში, PDF-ის სახით
"""

import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


numerator = 7       # საწყისი გასაყოფი
denominator = 5     # საწყისი გამოყოფი

counter = 0         # ცვლადი რომელსაც გამოვიყენებთ როგრც მთვლელს

for i in range(1,1001):
    new_numerator = 2 * denominator  + numerator       # შემდეგი წევრის გასაყოფი
    new_denominator = numerator + denominator           # შემდეგი წევრის გამოყოფი

    numerator = new_numerator       # ხელახლა ვინახავთ ცვლადებში რათა for-მა შეუფერხებლად იმუშაოს
    denominator = new_denominator   # ხელახლა ვინახავთ ცვლადებში რათა for-მა შეუფერხებლად იმუშაოს

    if len(str(numerator)) > len(str(denominator)): # თუ გასაყოფიმეტნიშნაა ვიდედრე გამოყოფი
        counter += 1        # მაშინ მთველს დაემატოს 1-ი და გააგრძელოს for-ციკლი


print(counter)  # ვპრინტავთ პასუხს
print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს