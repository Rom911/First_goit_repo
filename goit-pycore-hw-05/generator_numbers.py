import re
from typing import Callable

def generator_numbers(text: str):
    # Find all numbers with decimals clearly separated by spaces
    numbers = re.findall(r'\d+\.\d+', text)
    for num in numbers:
        yield float(num)  # Convert each found number to float and yield it

def sum_profit(text: str, func: Callable):
    # Use the provided generator function to calculate total profit
    return sum(func(text))
