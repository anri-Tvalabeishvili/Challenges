import time

start = time.time()

sum  = 0        # შემოგვყავს ცვლადი რომელშიც შევკრიბავთ პალინდრომებს

for number in range(int(1e6)):  # ვიღებთ ყველა ციფრს მილიონამდე

    number_binary = bin(number)     # გადაგვყავს ეს რიცხვები 2-ობით სისტემაში
    number_binary =  number_binary[2:]  # ორობითში გადაყვანის დროს წინა კოეფიცინეტის მოშორებით მიზნით ვიმახსოვრებთ ყველაფერს ამ კოეფივიენტის გარდა
    Number = str(number)    # 10-ბითი სისტემის რიცხვს ვწერთ სტინგებში

    if Number == Number[::-1] and number_binary == number_binary[::-1]:     # ვამოწმებთ 10-ითი და 2-ობითი სისტემის რიცხვების პალინდრომობას
        sum += number       # თუ ორივე პალინდრომია მაშინ ვკრიბავთ

print(sum)

print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს