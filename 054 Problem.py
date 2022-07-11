from itertools import permutations
from statistics import mode
from typing import Counter

from numpy import sort
from sympy import false



#cards = ["2S", "2W", "4C", "4C", "KC"]

def sum_index_finder(combnation):
    number = [str(i) for i in range(1,11)]

    sum = 0
    sum_index = ""
    for i in combnation:
        if i in number or i == "T":

            if i =="T":
                sum += 10
                continue
            
            sum += int(i)
        else:
            sum_index += i


    return (str(sum) + sum_index)


# დამთავრებულია
def Royal_Flush(cards):
    chaker = set("TJQKA")   # ვქმნით რაღაც შესადარებელ სეთს
    if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1] and chaker == set(cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]) : 
        return True
    else:
        return False


# დამთავრებულია
def Straight_Flush(cards):

    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    
    Possible_combinations = ["20", "25", "30", "35", "40", "34J", "27JQ","27QJ", "19JQK","19JKQ","19QJK","19QKJ","19KJQ","19KQJ"]   # აქ წერია ყველა შესაძლო კომბინაცია რათა მივიღოთ Straight_Flush 

    if cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1] and len(set(combnation)) == 5 :
        
        if sum_index_finder(combnation) in Possible_combinations: # ეს ფუნქცია პასუხად ამბრუნებს მოთამაშის კარტის
            return True
        else:

            return False
       
    else:
        return False


# დამთავრებულია
def Four_of_Kind(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    counted = (Counter(combnation))

    answers = list(counted.values())
    answers.sort()
    first_value = answers[1]
    second_value = answers[0]
    
    if len(check) == 2 and first_value == 4 and second_value == 1:
        return (mode([i for i in (combnation)]))
    else:
        return False


# დამთავრებულია
def Full_House(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    counted = (Counter(combnation))
    answers = list(counted.values())
    answers.sort()
    first_value = answers[1]
    second_value = answers[0]

    if len(check) == 2 and first_value == 3 and second_value == 2:
        return (mode([i for i in (combnation)]))
    else:
        return False


# დამთავრებულია
def Flush(cards):
    combnation = cards[0][1] + cards[1][1] + cards[2][1] + cards[3][1] + cards[4][1]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    
    if len(check) == 1 :
        return True
    else:
        return False 


# დამთავრებულია
def Straight(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    
    Possible_combinations = ["20", "25", "30", "35", "40", "34J", "27JQ","27QJ", "19JQK","19JKQ","19QJK","19QKJ","19KJQ","19KQJ"]   # აქ წერია ყველა შესაძლო კომბინაცია რათა მივიღოთ Straight_Flush 


    if sum_index_finder(combnation) in Possible_combinations: # ეს ფუნქცია პასუხად ამბრუნებს მოთამაშის კარტის
        return True
    else:
        return False
       

# დამთავრებულია
def Three_of_Kind(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    counted = (Counter(combnation))

    answers = list(counted.values())
    answers.sort()
    first_value = answers[-1]
    second_value = answers[0]
    print(answers)
    if len(check) == 3 and first_value == 3 and second_value == 1:
        return (mode([i for i in (combnation)]))
    else:
        return False


# დამთავრებულია
def Two_Pairs(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    counted = Counter(combnation)
    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]
    
    if len(check) == 3:
        for i in list:
            if counted[i] == 2:
                return i
                break
    else:
        return False


# დამთავრებულია
def One_Pair(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს
    check= set(combnation)
    counted = Counter(combnation)
    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]
    
    if len(check) == 4:
        for i in list:
            if counted[i] == 2:
                return i
                break
    else:
        return False


# დამთავრებულია
def High_Card(cards):
    combnation = cards[0][0] + cards[1][0] + cards[2][0] + cards[3][0] + cards[4][0]     # ვწერთ მნიშვნელობების საერთო სტრინგს

    list = ["A","K","Q","J","T", "9", "8", "7" , "6", "5","4","3","2"]
    
    
    for i in list:
        if i in combnation:
            return i
            break




f = open('Data/Problem_54.txt', 'r')   # შემოგვყავს ფაილი

content = f.read()  # ფაილის ელემენტს ვინახავთ რაიმე ცვლადში

content = content.split("\n")


for cards in content:
    card = cards.split(" ")
    player_1 = card[:5]
    player_2 = card[5:]

    
    if Straight(player_1) :
        print(player_1)

    



