import time   #  შემოგვყავს ტაიმერი რათა დავითვალოთ გამოთვლაზე დახარჯული დრო
start = time.time()

Lychrel_numbers = 0

for i in range(2,10001):

    reverse_number = int(str(i)[::-1])  # აღებული ციფრი შევატრიალოთ

    sum_number = i + reverse_number    # ავჯამოთ აღაბეული და აღებულის შეტრიალებული რიცხვი

    iterations = 1      # ზემოთ აღნიშნული მოქმედება უკვე 1 იტერაციაა

    while True:
        if str(sum_number) == str(sum_number)[::-1]:  # თუ მიღებული ჯამი და ჯამის შებრუნებული ერთი დაიგივეა მაშინ
            break

        if iterations > 50:   # თუ იტერაციების რიცხვი აღემატება 50 მაშინ
            Lychrel_numbers +=1   #  დავამატოთ ერთი
            break
        


        reverse_number = int(str(sum_number)[::-1])  # მიღებული ძველი ჯამი შევატრიალოთ
        sum_number +=  reverse_number  # ძველ ჯამს დავუმატოთ ახლად შეტრიალებული ძველი ჯამი და შევინახოთ ახალ ჯამში

        iterations +=1   # 22 და 23 ხაზზე განხორციელებული მანუპულაცია თავისთავად არის 1 იტერაციაა
        

print(Lychrel_numbers)
print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს