from __future__ import annotations

import sys

from common import print_hello


import numpy as np

def hello_function(name: str) -> str:
    lucky_number = np.random.randint(1, 100)
    return f"Hello {name}! Your Snowpark NumPy lucky number is {lucky_number}."
