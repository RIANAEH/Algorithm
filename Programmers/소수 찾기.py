import math
from itertools import permutations

def solution(numbers):
    ans_list = []
    for i in range(1, len(numbers)+1):
        per_set = set(map(''.join, permutations(numbers, i)))
        for per in per_set:
            if is_prime_number(int(per)):
                ans_list.append(int(per))
    
    return len(set(ans_list))

def is_prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
        	return False
    return True
