
import datetime     # შემოგყვავს თარიღების ბიბლიოთეკა
counter = 0         # შემოგვყავს მთველი

for year in range(1901, 2001):      # ვწერთ წლების დიაპაზონს
    for month in range(1, 13):      # ვწერთ თვეების დიაპაზონს
        if datetime.date(year, month, 1).weekday() == 6:        # თუ გარკვეული წლის, გარკვეული თვის პირველი რიცხვი დაემთხვევა კვირის მე-6 დღეს ანუ Sundays-ს
            counter += 1        # მაშინ ქაუნთერს დაემატოს 1

print(counter)
