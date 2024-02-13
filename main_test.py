# test_main.py

import random
import main

def generate_random_numbers():
    # Generate a random list of numbers with a random length between 1 and 10
    length = random.randint(1, 10)
    numbers = [random.randint(1, 100) for _ in range(length)]
    return numbers

def calculate_average_expected(numbers):
    # Calculate the expected average of the numbers
    return sum(numbers) / len(numbers) if numbers else 0.0

def test_calculate_average():
    # Test with random inputs
    for _ in range(10):  # Run 10 random test cases
        numbers = generate_random_numbers()
        expected_average = calculate_average_expected(numbers)
        assert main.calculate_average(numbers) == expected_average, \
            "The generated random values may not cover enough scenarios. Try different inputs."
