
def sevenish_number(n):
    num = 7
    # arg 1 // base case. 7**0 = 1 // 7** n - 1 valid
    # arg 2 // 7 ** n -1 valid
    if n == 1:
        return 0 
    # arg 3 // 7 ** n -1 invalid // expected 8 (7**0 + 7**1) result 49
