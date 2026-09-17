# IS 218 Test 1 

**Name:** Joshua Mathai

## Purpose

This project is a small Python calculator package that implements addition and subtraction. It includes student tests and supplied acceptance tests to verify that the calculator works correctly.

## Setup

Create the Python virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Run Tests

Run the student tests:

```bash
python -m pytest
```

Run the complete test suite:

```bash
python -m pytest tests checks -v
```

## Issues

* [Issue 1 — Set up Python and pytest](../../issues/1)
* [Issue 2 — Write addition and three tests](../../issues/2)
* [Issue 3 — Write subtraction and three tests](../../issues/3)
* [Issue 4 — Document, verify, and deliver](../../issues/4)

## Test  Explanation

One subtraction test checks subtracting a larger number from a smaller number. For example, the inputs are `3` and `5`, and the expected result is `-2`.

The test uses an assertion to compare the actual result of the subtraction function with the expected result. If the function returns `-2`, the assertion passes. If it returns another value, the test fails.



The `.venv` directory contains the local Python virtual environment and installed packages for this project. It is specific to the developer's computer and does not need to be uploaded to GitHub. The `.gitignore` file prevents `.venv` and other generated files such as caches and bytecode from being tracked.

## Verification


The final Assessment Tests will be run on the pushed `main` commit through GitHub Actions.
