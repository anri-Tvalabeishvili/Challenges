from statistics import mode
from typing import Counter
import time 
start = time.time()


""" 
რათა მოვახდინოთ გამარჯვებულის იდენტიფიცირება საჭიროა თითოეულ კარტსა და თითოეულ კომბინაციას შევუსაბამოთ გარკვეული ქულა

კარტებისთვის:                   კომბინაციებისთვის:
"A":    14                          Royal Flush         1000
"K":    13                          Straight Flush      900 + უმაღლესი კარტის ქულა
"Q":    12                          Four of Kind        800 + 4 წყვილი კარტიდან 1-ის ქულა
"J":    11                          Full House          700 + 3 წყვილი კარტიდან 1-ის ქულა
"T":    10                          Flush               600 + უმაღლესი კარტის ქულა
"9":    9                           Straight            500 + უმაღლესი კარტის ქულა
"8":    8                           Three of Kind       400 + 3 წყვილი კარტიდან 1-ის ქულა
"7":    7                           Two Pairs           300 + ქყვილიდან მაღალი კარტის ქულა
"6":    6                           One Pair            200 + წყვილი კარტიდან 1-ის ქულა
"5":    5                           High Card           უმაღლესი კარტის ქულა   
"4":    4 
"3":    3 
"2":    2

"""


card_values = {"A":14, "K":13, "Q":12, "J":11, "T": 10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}


# ეს ფუქნცია სპეციალურად არის შექმნილი Straight Flush-სა და  Straight-ისთვის
# ეს ფუნქცია აბრუნებს კარტების კომბინაციას დაბალიდან მაღალი თანრიგისკენ
def sum_index_finder(combnation): 
    # ვქმნით გარკვეულ ცვლადს რომელშიც თანმიმდევრობით შევიყვანთ კარტებს დაბლიდან მაღალი თანრიგის მიმართულებით
    sorted_combinations = ""

    if "2" in combnation:
        sorted_combinations += "2"
    if "3" in combnation:
        sorted_combinations += "3"
    if "4" in combnation:
        sorted_combinations += "4"
    if "5" in combnation:
        sorted_combinations += "5"
    if "6" in combnation:
        sorted_combinations += "6"
    if "7" in combnation:
        sorted_combinations += "7"
    if "8" in combnation:
        sorted_combinations += "8"
    if "9" in combnation:
        sorted_combinations += "9"
    if "T" in combnation:
        sorted_combinations += "T"
    if "J" in combnation:
        sorted_combinations += "J"
    if "Q" in combnation:
        sorted_combinations += "Q"
    if "K" in combnation:
        sorted_combinations += "K"
    if "A" in combnation:
        sorted_combinations += "A"

    return (sorted_combinations)  # ვაბრუნებთ დალაგებულ კარტებს



""" ქვემოთ მოყვანილი ფუქნციები ადგენენ თუ რომელ კარტსა თუ კომბინაციას ფლობს მოთამაშე """

def Royal_Flush(cards):
    # Royal Flush-ისთვის აუცილებელია უმაღლესი რეგისტრის 5 კარტი (T, J, Q, K, A)
    # ამავდროულად ეს 5 კარტი უნდა ერთი და იყოს იგივე suits-ის წარმომადგენლები

    upper_register = set("TJQKA")   # ვქმნით set-ს რათა მომავალში შეგვეძლოს მოთამაშის კარტის შედარეა ამ set-თან

    player_cards = set(cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]) # მოთამაშის კარტები set-ის სახით
    player_suits = set(cards[0][1] + cards[1][1] + cards[2][1] + cards[3][1] + cards[4][1]) # მოთამაშის suits-ები set-ის სახით

    # ლოგიკა ამოწმებს წარმოადგენს თუ არა კარტები ერთი და იმავე suits-სა და უმაღლესი რეგისტრის 
    if len(player_suits) == 1 and upper_register == player_cards : 
        return 1000  # თუ წამოადგენს ვაბრუნებთ 1000 ქულას 
    else:
        return 0    # თუ არ წამოადგენს ვაბრუნებთ 0 ქულას 


def Straight_Flush(cards):
    # Straight Flush-ისთვის აუცილებელია 5 ერთმანეთის მეზობელი კარტის ქონა
    # ამავდროულად ეს 5 კარტი უნდა იყოს ერთი და იგივე suits-ის წარმომადგენლები

    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით
    player_suits = set(cards[0][1] + cards[1][1] + cards[2][1] + cards[3][1] + cards[4][1]) # მოთამაშის suits-ები set-ის სახით
    
    # ეს სია შეიცავს ყველა შესაძლო კომბინაციას რომლიდანაც შესაძლებელია მივიღოთ Straight Flush 
    Possible_combinations = ["23456", "34567", "45678", "56789", "6789T", "789TJ", "89TJQ", "9TJQK", "TJQK"] 


    # ლოგიკა ამოწმებს წარმოადგენს თუ არა კარტები ერთი და იმავე suits-ს და განსხვავდებიან თუ არა ისინი მნიშვნელობებით
    if player_suits == 1 and len(set(player_cards)) == 5 :
        # sum_index_finder-ის მეშვეობით ვალაგებთ მოთამაშის კარტებს და ვამოწმებთ არის თუ არა Possible_combinations-ის სიაში
        if sum_index_finder(player_cards) in Possible_combinations:
            return 900 + High_Card(cards)    # თუ არის ვაბრუნებთ 900 ქულას  + უმაღლესი კარტის ქულა
        else:
            return 0        # თუ არ არის ვაბრუნებთ 0 ქულას  
    else:
        return 0            # თუ არ არის ვაბრუნებთ 0 ქულას  


def Four_of_Kind(cards):
    # Four of Kind-ისთვის აუცილებელია 4 ერთნაირი კარტის ქონა 


    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით

    counted = (Counter(player_cards))   # ვითვლით რამდენი ერთნარი კარტი აქვს მოთამაშეს

    answers = list(counted.values())    # list-ის სახით ვწერთ მიღებული values-ებს
    answers.sort()                      # ვალაგებთ ზრდის მიხედვით

    # ლოგიკით ვამოწმებთ უჭირავს თუ არა მოთამაშეს 4 ერთნაირი და 1 განსხვავებული კარტი
    if len(set(player_cards)) == 2 and answers[1] == 4 and answers[0] == 1:
        return 800 + card_values[(mode([i for i in (player_cards)]))] # თუ უჭირავს მაშინ ვაბრუნებთ 800 ქულას + 4 წყვილიდან ერთ-ერთის ქულა
    else:
        return 0    # თუ არ უჭირავს ვაბრუნებთ 0 ქულას


def Full_House(cards):
    # Full House-ისთვის აუცილებელია 3 ერთნაირი კარტისა და დამატებით წყვილი კარტის ყოლა

    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით

    
    counted = (Counter(player_cards))   # ვითვლით რამდენი ერთნარი კარტი აქვს მოთამაშეს

    answers = list(counted.values())    # list-ის სახით ვწერთ მიღებული values-ებს
    answers.sort()                      # ვალაგებთ ზრდის მიხედვით


    # ლოგიკით ვამოწმებთ უჭირავს თუ არა მოთამაშეს 3 ერთნაირი და დამატებით 2 ერთნაირი კარტი
    if len(set(player_cards)) == 2 and answers[1] == 3 and answers[0] == 2:
        return 700 + card_values [(mode([i for i in (player_cards)]))]  # თუ უჭირავს მაშინ ვაბრუნებთ 700 ქულას + 3 წყვილიდან ერთ-ერთის ქულა
    else:
        return 0    # თუ არ უჭირავს ვაბრუნებთ 0 ქულას


def Flush(cards):
    # Flush-ისთვის აუცილებელია 5 ერთნაირი suit-ის კარტის ყოლა

    player_suits = set(cards[0][1] + cards[1][1] + cards[2][1] + cards[3][1] + cards[4][1]) # მოთამაშის suits-ები set-ის სახით
    
    # ვამოწმებთ აქვს თუ არა მოთამაშეს 5 ერთნაირი suit-ის კარტი
    if len(player_suits) == 1 :
        return 600 + High_Card(cards)  # თუ აქვს მაშინ ვაბრუნებთ 600 ქულას + უმაღლესი კარტის ქულა
    else:
        return 0    # თუ არ აქვს მაშინ ვაბრუნებთ 0 ქულას


def Straight(cards):
    # Straight-ისთვის აუცილებელია 5 ერთმანეთის მეზობელი კარტის ქონა

    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით
    
    # ეს სია შეიცავს ყველა შესაძლო კომბინაციას რომლიდანაც შესაძლებელია მივიღოთ Straight
    Possible_combinations = ["23456", "34567", "45678", "56789", "6789T", "789TJ", "89TJQ", "9TJQK", "TJQK"]
    
    # ლოგიკა ამოწმებსა არის თუ არა მოთამაშის კარტების კომბინაცია შესაძლო სიაში
    if sum_index_finder(player_cards) in Possible_combinations :
        return 500 + High_Card(cards)    # თუ არის ვაბრუნებთ 500 ქულას  + უმაღლესი კარტის ქულა
    else:
        return 0    # თუ არ არის ვაბრუნებთ 0 ქულას 
       

def Three_of_Kind(cards):
    # Three of Kind-ისთვის აუცილებელია 3 ერთნაირი კარტის ქონა 

    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით
   
    counted = (Counter(player_cards))   # ვითვლით რამდენი ერთნარი კარტი აქვს მოთამაშეს

    answers = list(counted.values())    # list-ის სახით ვწერთ მიღებული values-ებს
    answers.sort()                      # ვალაგებთ ზრდის მიხედვით
    
    # ლოგიკით ვამოწმებთ უჭირავს თუ არა მოთამაშეს 3 ერთნაირი და თითო განსხვავებული კარტი
    if len(set(player_cards)) == 3 and answers[-1] == 3 and answers[0] == 1 and answers[1] == 1:
        return 400 + card_values [(mode([i for i in (player_cards)]))]     # თუ უჭირავს მაშინ ვაბრუნებთ 400 ქულას + 3 წყვილიდან ერთ-ერთის ქულა
    else:
        return 0    # თუ არ უჭირავს ვაბრუნებთ 0 ქულას


def Two_Pairs(cards):
    # Two Pairs-ისთვის აუცილებელია 2 ორკატიანი წყვლის  ქონა   
    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით

    counted = Counter(player_cards)     # ვითვლით რამდენი ერთნარი კარტი აქვს მოთამაშეს

    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]         # ვქმნით კარტების სიას
    
    if len(set(player_cards)) == 3: # თუ მოთამაშეს ნამდვილად უჭირავს 2 ორკატიანი წყვილი მაშინ
        for i in list:      # ვიღებთ თითოეულ კარტს კარტების სიიდან
            if counted[i] == 2:     # და ვიგებთ რომელი კარტის წყვილი აქვს მოთამაშეს
                return 300 + card_values[i]  # პასუხის გაგების შემდეგ ვაბრუნებთ 300 ქულას + კარტების წყვილიდან უმაღლესი ქარტის ქულას
                break   # ვწყვეტთ კოდს
    else:
        return 0    # თუ მოთამაშეს არ უჭირავს წყვილი პაბრუნებთ 0 ქულას


def One_Pair(cards):
    # Two Pairs-ისთვის აუცილებელია 2 ერთნარი კარტის ქონა 
    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით

    counted = Counter(player_cards)     # ვითვლით რამდენი ერთნარი კარტი აქვს მოთამაშეს

    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]         # ვქმნით კარტების სიას
    
    if len(set(player_cards)) == 4: # თუ მოთამაშეს ნამდვილად უჭირავს 2 ერთნარი კარტი მაშინ
        for i in list:              # ვიღებთ თითოეულ კარტს კარტების სიიდან
            if counted[i] == 2:     # და ვიგებთ რომელი კარტის წყვილი აქვს მოთამაშეს
                return 200 + card_values[i] # პასუხის გაგების შემდეგ ვაბრუნებთ 200 ქულას + კარტების წყვილიდან ერთ-ერთის ქულას
                break # ვწყვეტთ კოდს
    else:
        return 0    # თუ მოთამაშეს არ უჭირავს წყვილი პაბრუნებთ 0 ქულას


def High_Card(cards):
    player_cards = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # მოთამაშის კარტები str-ის სახით

    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]
    
    # ვირჩევთ მოთამაში კარტიდან უმაღლეს კარტს და ვაბრუნებთ მის მნიშვნელობას
    for i in list:
        if i in player_cards:
            return card_values[i]
            break





""" ეს ფუნქცია ამოწმებს თუ რამდენი ქულით ფასდება თითოეული მოთამაშის კარტი """
def winner_value(palyer_card):

    if Royal_Flush(palyer_card) != 0 :
        return Royal_Flush(palyer_card)

    elif Straight_Flush(palyer_card) != 0 :
        return Straight_Flush(palyer_card)

    elif Four_of_Kind(palyer_card) != 0 :
        return Four_of_Kind(palyer_card)

    elif Full_House(palyer_card) != 0 :
        return Full_House(palyer_card)

    elif Flush(palyer_card) != 0 :
        return Flush(palyer_card)

    elif Straight(palyer_card) != 0 :
        return Straight(palyer_card)

    elif Three_of_Kind(palyer_card) != 0 :
        return Three_of_Kind(palyer_card)

    elif Two_Pairs(palyer_card) != 0 :
        return Two_Pairs(palyer_card)

    elif One_Pair(palyer_card) != 0 :
        return One_Pair(palyer_card)

    elif High_Card(palyer_card) != 0 :
        return High_Card(palyer_card)





f = open('Data/Project Euler/Problem_54.txt', 'r')   # შემოგვყავს ფაილი

content = f.read()  # ფაილის ელემენტს ვინახავთ ცვლადში

content = content.split("\n")   # ვსფლითავთ ელემეტებს

counter = 0     # შემოგყვას ცვლადი რომელშიც შევინახავთ მოთამაშის გამარჯვებების რაოდენობას

for cards in content:
    card = cards.split(" ") # ვიღებთ თითოეულ ხელს და კიდევ ერთხელ ვსფლითავთ
    player_1 = card[:5]     # გასფლითური ლისთიდან ვიღებთ პირველი მოთამაშის კარტებს
    player_2 = card[5:]     # გასფლითური ლისთიდან ვიღებთ მეორე მოთამაშის კარტებს


    # თუ პირველი მოთამაშის ქულა მეტი იქნება მეორე მოთამაშის ქულაზე მაშინ მთვლელს ვამატებთ 1-ს
    if winner_value(player_1) > winner_value(player_2):
        counter += 1


print(counter) # ვბეჭდავთ საბოლოო პასუხს
print("Calculation time:" , time.time() -start)     # ვპრინტავთ გამოთვალზე დახარჯულ დროს
