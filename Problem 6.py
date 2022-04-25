import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

list = []  # ვქმნით სიას სადაც შევინახავთ რიცხვთა სიმრავლეს

for i in range(1,101):   # ზემოთ აღნიშნულ სიაში ვამატებთ ამ ციფრებს
    list.append(i)   


sum_and_square = sum(list)**2   # ვკრიბავთ სიაში არსებულ რიცხვებბს და აგვყავს კვატრატში 

for i in range (0,len(list)):  # სიიდან ვიღებთ თითოეულ ციფრს და მას ვანაცვლებთ მისი გვადრატული მნიშვნელობით
    list[i]= list[i]**2

square_and_sum = sum(list)     # აკვადრატებულ ციფრებს ვკრიბავთ 

answer =  sum_and_square  - square_and_sum  # ვაკლებთ ერმანეთს

print(answer)

end = time.time()  
print(end-start)    # ვპრინტავთ გამოთვალზე დახარჯულ დროს