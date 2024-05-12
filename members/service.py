from random import randint
from datetime import datetime


def random_with_N_digits(no_digits, max_attempts=10):
    """Generate a random integer with n digits."""
    from members.models import Member

    if max_attempts <= 0:
        raise ValueError("max_attempts must be a positive integer")

    # Define the range for n-digit numbers
    range_start = 10 ** (no_digits - 1)  # Smallest n-digit number
    range_end = (10**no_digits) - 1  # Largest n-digit number

    attempts = 0
    while attempts < max_attempts:
        generated_number = randint(range_start, range_end)
        # Check if the combination of lead_source, lead_type, and generated number already exists

        unique_number = f"{str(datetime.now().year)[:2]}{generated_number}"

        if not Member.objects.filter(unique_id=unique_number).exists():
            return unique_number
        attempts += 1

    # If max_attempts reached without finding a unique number, return None
    return None
