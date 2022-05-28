import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

number = 1

while True:     # ვამოწწმებთ სანამ არ ვიპოვით შესაბამის რიცხვს
    number +=1      # წინა შემოწმებულ რიცხვს ვუმატებთ 1-ს რათა შევამოწმოთ

    if set(str(number)) == set(str(number*2)) == set(str(number*3)) == set(str(number*4)) == set(str(number*5)) == set(str(number*6)): # თუ ჩვენი რიცხვის ყველა ნამრავლში შემავალი ციფრები ერთი და იგივეა მაშინ
        print(number)   # ტერმინალში გამოგვყავს ეს რიცხვი 
        break   # ვწყვეტთ კოდს

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს
