def categorize_numbers(numbers):
    if not numbers:
        return [], []

    evens = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)
    return evens, odds
