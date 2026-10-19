
# Benchmark Test Quality

A Python project exploring how automated tests detect common coding mistakes.

## Project Goal

A coding benchmark needs tests that distinguish correct solutions from incorrect ones. This project demonstrates that principle using a simple function that checks whether an integer is even.

## The Task

Implement `is_even(number)` so it returns `True` for even integers and `False` for odd integers.

## Project Features

- A correct reference implementation
- Intentionally incorrect implementations
- Automated unit tests
- A test-quality evaluation script
- Edge cases including zero and negative numbers

## Technologies

- Python
- unittest
- GitHub

## How to Run

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

Run the test-quality evaluation:

```bash
python evaluate_test_quality.py
```

## What This Project Demonstrates

- Writing tests for expected behavior
- Identifying edge cases
- Detecting incorrect implementations
- Evaluating the effectiveness of test cases

## Limitations

This is a small educational project, not a complete mutation-testing framework or a secure environment for running untrusted code.

## Future Improvements

- Add more coding challenges
- Generate JSON evaluation reports
- Expand test coverage
- Add automated continuous integration
