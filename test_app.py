from app import categorize_numbers

def test_categorize_numbers_empty():
    evens, odds = categorize_numbers([])
    assert evens == []
    assert odds == []


def test_categorize_numbers_mixed():
    evens, odds = categorize_numbers([1, 2, 3, 4, 5, 6])
    assert evens == [2, 4, 6]
    assert odds == [1, 3, 5]


def test_categorize_numbers_all_even():
    evens, odds = categorize_numbers([2, 4, 6, 8])
    assert evens == [2, 4, 6, 8]
    assert odds == []


def test_categorize_numbers_all_odd():
    evens, odds = categorize_numbers([1, 3, 5, 7])
    assert evens == []
    assert odds == [1, 3, 5, 7]
    