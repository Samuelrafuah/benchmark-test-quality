
def always_true(number):
    """Incorrect: claims every number is even."""
    return True


def always_false(number):
    """Incorrect: claims no number is even."""
    return False


def wrong_for_negative(number):
    """Incorrect: mishandles negative even numbers."""
    if number < 0:
        return False
    return number % 2 == 0


def wrong_for_zero(number):
    """Incorrect: claims zero is odd."""
    if number == 0:
        return False
    return number % 2 == 0
