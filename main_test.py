# test_main.py

import random
from main import calculate_average

def generate_random_numbers():
    # Generate a random list of numbers with a random length between 0 and 10
    length = random.randint(0, 10)
    numbers = [random.randint(1, 100) for _ in range(length)]
    return numbers

def test_calculate_average():
    # Test with random inputs
    for _ in range(10):  # Run 10 random test cases
        numbers = generate_random_numbers()
        expected_average = sum(numbers) / len(numbers) if numbers else 0
        assert calculate_average(numbers) == expected_average
