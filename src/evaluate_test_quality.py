
from src.solutions import is_even
from src.mutants import (
    always_true,
    always_false,
    wrong_for_negative,
    wrong_for_zero,
)


TEST_CASES = [
    (4, True),
    (7, False),
    (-4, True),
    (-3, False),
    (0, True),
]


MUTANTS = {
    "always_true": always_true,
    "always_false": always_false,
    "wrong_for_negative": wrong_for_negative,
    "wrong_for_zero": wrong_for_zero,
}


def passes_all_tests(function):
    """Return True if a function passes every test case."""
    return all(function(number) == expected
               for number, expected in TEST_CASES)


def main():
    print("Checking the correct solution...")

    if passes_all_tests(is_even):
        print("PASS: Correct solution passes all tests.")
    else:
        print("FAIL: Correct solution did not pass all tests.")

    print("\nChecking incorrect implementations...")

    detected = 0

    for name, function in MUTANTS.items():
        if passes_all_tests(function):
            print(f"NOT DETECTED: {name}")
        else:
            print(f"DETECTED: {name}")
            detected += 1

    total = len(MUTANTS)
    score = detected / total * 100

    print(f"\nMutants detected: {detected}/{total}")
    print(f"Mutation detection score: {score:.0f}%")


if __name__ == "__main__":
    main()
