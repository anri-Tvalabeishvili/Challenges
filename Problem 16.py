import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

number = 2**1000         # ვწერთ რიცხვს

listed_number = [int(x) for x in str(number)]   # რიცხვის თითოეული ციფრს ვწერთ კარგვეულ ლისთში

answer  =  sum(listed_number)  # ვკრიბავთ მოცემული ლისთის ყველა წევრს 

print(answer)

end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს