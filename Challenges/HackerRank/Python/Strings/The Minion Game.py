# There are as many possible combinations as there are letters after a particular letter

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    Stuart_score = 0 
    Kevin_score = 0
    length = len(string)
    
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in vowels:
            Kevin_score += score
        else:
            Stuart_score += score
            
            
    if Stuart_score == Kevin_score:
        print('Draw')
    if Stuart_score > Kevin_score:
        print(f'Stuart {Stuart_score}')
    if Stuart_score < Kevin_score:
        print(f'Kevin {Kevin_score}')
    
if __name__ == '__main__':
    s = input()
    minion_game(s)