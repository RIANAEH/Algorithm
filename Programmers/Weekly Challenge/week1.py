def solution(price, money, count):
    total = int(count * (count + 1) / 2) * price
    
    result = total - money
    if result <= 0:
        return 0
    else:
        return result
