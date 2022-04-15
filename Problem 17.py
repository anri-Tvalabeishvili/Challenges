

wors = ["" , "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",     # ვქმნით ლისთს სადაც მოთავსებულია რიცხვების ინგლისური
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",]   # შესატყვისები 1-დან 20-მდე


wors_2 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  # ვქმნით ლისთს სადაც მოტავსებულია ათეულების აღმნიშვნელი ციფრების შესატყვისები


length = [11, ]   # ვქმნით ლისთს სადაც დავამატებთ თითოეული რიცხვის სიტყობრივ სიგრძეს 
# ლისთი ისწყება 11-ის ანუ 1000-სის შესატყვისი სიტყვის სიგრძით "one thousand"


def enlish(number):    # ვქმნით ფუნქციას რომელი რიცხვებს გადაიყვანს სიტყვებში და დათვლის ამ სიტყვების ასოების რაოდენობას

    if 0 < number <20:   # თუ რიცხვი არის 0-დან 20-მდე მაშინ ის იპოვის მის შესატყვისს wors-ის ლისთში
        length.append(len(wors[number]))
        

    if 20<= number < 100:       # თუ რიცხვი არის 20-დან 100-მდე 
        Dozens = number // 10       # ვიპოვით მის ათეულების აღმნიშვნელ ციფრს
        last_num = number - Dozens*10 # ვიპოვით მის ერთეულების აღმნიშვნელ ციფრს 

        length.append(len(wors_2[Dozens] + wors[last_num]))     # და ამ ნაპოვნი ციფრებით ვიპოვით შესაბამისობას wors-სა და wors_2-ის ლისტებში და ვამატებთ length-ის ლისთში
        

    if 100<= number <1000:  # თუ რიცხვი არის 100-დან 1000-მდე 
        Hundreds = number // 100        # ვიპოვით მის ასეულების ათღმნიშვნელ ციფრს
        new_num = number- Hundreds*100   # 251 - 200 = 51

        Dozens = new_num // 10      # ვიპოვით მის ათეულების აღმნიშვნელ ციფრს

        if new_num == 0:  # თუ ციფრს არ აქვს ათეულები და ერთეულები 
            length.append(len(wors[Hundreds] + "hundred"))  # ვნახულობთ მის ასეულების აღმნიშვნელ ციფრს და ვუმატებთ "hundred"-ს და ვამატებთ length-ის ლისთში

        elif Dozens !=1 : # თუ ცუფრის ათეულების ნიშანი განსხვავდება 1-სგან მაშინ ვაგრძელებთ შემდეგ ლოგიკას 
            last_num = number - Hundreds*100 - Dozens*10    
            length.append(len(wors[Hundreds] + "hundred" + "and" + wors_2[Dozens] + wors[last_num])) 
                  
        else:   # დანარჩენ ყველა შემთხვევაში მივყვებით ამ ლოგიკას
            last_num = number - Hundreds*100
            length.append(len(wors[Hundreds] + "hundred" + "and" +  wors[last_num]))
            


for i in range (1,1000):   # ვიგებთ ყველა რიცხვის "სიტყვიერ"-სიგრძეს 1-დან 999-ჩათვლით და ვამატებთ length-ის ლისთში
    enlish(i)

print(sum(length))  # ვკრიბავთ ყველა სიგრძეს
