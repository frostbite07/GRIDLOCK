import math

def round_up(n, decimals=0): 
    multiplier = 10 ** decimals 
    return math.ceil(n * multiplier) / multiplier

def evaluate_score(a,b,c,d,e):
    test_1 = a*1.50
    test_2 = b*3.00
    test_3 = c*2.25
    test_4 = d*3.50
    test_5 = e*4.75

    total_15 = test_1+test_2+test_3+test_4+test_5
    total_5 = 5 - (total_15/3)
    final_score = round_up(total_5,2) 
    
    return final_score

