from math import floor


def get_min_topping_cost(combinations, topping_dict):
    min_topping_cost = int(1e10)
    for combination in combinations:
        min_topping_cost = min(min_topping_cost, topping_dict[combination])

    return min_topping_cost


tea_count = int(input())
tea_prices = list(map(int, input().split()))
topping_count = int(input())
topping_prices = list(map(int, input().split()))

topping_dict = {}
for i in range(topping_count):
    topping_dict[i] = topping_prices[i]

for i in range(tea_count):
    combinations = list(map(lambda x: int(x) - 1, input().split()))
    combinations = combinations[1:]

    tea_prices[i] += get_min_topping_cost(combinations, topping_dict)

money = int(input())
cheapest = sorted(tea_prices)[0]
max_students = floor(money / cheapest) - 1

if max_students <= 0:
    print(0)
else:
    print(max_students)
