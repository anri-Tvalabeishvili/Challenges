import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


answer = {}  # ვქმნით პასუხებისთვის დიქშინარის სადაც თითოეულ გამყოფს შესაბამისობაში ეყოლება თავისი recurring- სიგრძე


for Divider in range(1,1000):   # ვიღებთ რიცხვებს 1-დან 1000-მდე
    liste = []      # ვქმნით ლისთს რათა თითოეული რიცხვისთვის დავთავალოთ recurring- სიგრძე
    dividend = 1    # შემოგვაქ გასაყოფი
    while True:  # ციკლი გაგრძელდეს მანამ სანამ ხელოცნურად არ შევწყვეტთ
        if dividend*10 in liste:        # ქვეშმიწერით გაყოფისას თუ გასაყოფი რიცხვი დაემთხვა იმ რიცხვს რომელშიც უკვე მოთავსდა გამყოფი მაშინ შევწყვიტოთ ციკლი
            break

        number = dividend*10 // Divider     # ვატარებთ ჩვეულებრივ ქვეშმიწერით ოპერაციას
        liste.append(dividend*10)           
        dividend = dividend*10 - number*Divider
        
    answer[Divider] = len(liste) # რიცხვს და მის recurring- სიგრძეს ვამატებთ პასუხებში


new_value = max(answer, key=answer.get)  # ვირებთ მაქსიმალურ recurring-ის მნიშვნელობას  და მის შესაბამის რიცხვს
print(new_value) 


end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს
