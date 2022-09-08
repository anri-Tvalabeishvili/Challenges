import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()


number = "."

# 9 x 1 digit
# 90 x 2 digit
# 900 x 3 digit
# 9000 x 4 digit
# 90000 x 5 digit
# n x 6 digit

# = 9*1 + 90*2 + 900*3+ 9000*4 + 90000*5 + n*6 = 1000000
# n = lim = 185186

lim = 185186  # ვითვლით იმ ზღვარს რომლამდეც გვაინტერესებს რიცხვები

for i in range(1,lim): 
    number += str(i)        # ვამატებთ სტრინგებათ რათა შემდგომში მარტივად ამოვიღოთ ინდექსის ნომრით


# თითოელი წევრი საკუთარი ინდექსის ნომრით ამოგვყავს
d1 = int(number[1])

d10 = int(number[10])

d100 = int(number[100])

d1000 = int(number[1000])

d10000 = int(number[10000])

d100000 = int(number[100000])

d1000000 = int(number[1000000])


print( d1*d10*d100*d1000*d10000*d100000*d1000000)   # ვპრინტავთ პასუხს

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს