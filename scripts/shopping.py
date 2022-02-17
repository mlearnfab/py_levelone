

prices = [1.5, 23.25, 11.10, 2.53, 12.3]


def bill(costs):
    total = 0
    for cost in costs:
        total = total + cost
    return total

print(bill(prices))
    
    