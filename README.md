# Python 3.10 pytest Project

This is a Python project using pytest for automated testing. It is developed using Python 3.10 and designed for testing
registration form for https://www.dutch.com

## Project Overview

Test tsk for Senior QA Automation role

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:Serdu4ok/registration_form.git

### Run tests

# To run test without headless

- Go to src/fixtures/set_up_ui.py and comment this line of code -options.add_argument('--headless')

1. Run Tests in a Specific Directory:
    - pytest path/to/your/directory
2. Run tests by marker expressions:
    - pytest -m positive
3. Run Tests in a Specific Test File:
    - pytest path/to/your/test_file.py
4. Run Specific Test Functions or Methods:
    - pytest path/to/your/test_file.py::test_function_name
5. Run Tests with Detailed Output:
    - pytest -v
6. Run all tests
    - pytest
