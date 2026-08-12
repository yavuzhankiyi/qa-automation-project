# QA Automation Project

[![QA Automation Tests](https://github.com/yavuzhankiyi/qa-automation-project/actions/workflows/tests.yml/badge.svg)](https://github.com/yavuzhankiyi/qa-automation-project/actions/workflows/tests.yml)

A comprehensive QA portfolio project covering UI automation, API testing, manual test documentation, reporting, and CI integration.

---

## Project Overview

This project demonstrates end-to-end software testing practices using both manual and automated approaches.

The automation framework includes:

- Selenium WebDriver
- Pytest
- Page Object Model
- API Testing with Python Requests
- Postman Collections
- GitHub Actions CI
- HTML Test Reports
- Screenshot Capture on Failure
- Manual Test Cases
- Bug Report Documentation

---

## Test Application

UI testing is performed on:

https://www.saucedemo.com/

API testing is performed on:

https://jsonplaceholder.typicode.com/

---

## Technologies Used

### UI Automation

- Python
- Selenium WebDriver
- Pytest
- Page Object Model

### API Testing

- Python Requests
- Pytest
- Postman

### CI/CD

- Git
- GitHub
- GitHub Actions

### Reporting

- pytest-html
- Automatic Screenshots on Test Failure
- GitHub Actions Test Report Artifact

---

## Project Structure

    qa-automation-project/
    │
    ├── pages/
    │   ├── login_page.py
    │   ├── products_page.py
    │   ├── cart_page.py
    │   └── checkout_page.py
    │
    ├── tests/
    │   ├── test_login.py
    │   ├── test_cart.py
    │   ├── test_checkout.py
    │   └── test_sorting.py
    │
    ├── api-tests/
    │   ├── postman/
    │   │   └── E-Commerce-QA-API-Tests.postman_collection.json
    │   └── python/
    │       └── test_api.py
    │
    ├── manual-tests/
    │   ├── test-cases.md
    │   └── bug-reports.md
    │
    ├── reports/
    ├── .github/
    │   └── workflows/
    │       └── tests.yml
    │
    ├── conftest.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

---

## UI Test Coverage

### Login Tests

- Successful login
- Invalid password
- Empty username
- Empty password
- Empty username and password

### Cart Tests

- Add product to cart
- Verify cart badge
- Verify product in cart
- Remove product from cart

### Checkout Tests

- Successful checkout
- Checkout without first name
- Checkout without postal code

### Product Sorting Tests

- Price Low to High
- Price High to Low

---

## API Test Coverage

### GET

- Get all posts
- Get single post
- Invalid post request

### POST

- Create new post

### PUT

- Update existing post

### DELETE

- Delete post

---

## Automated Test Results

Current automated test suite:

    18 tests
    18 passed
    0 failed

The test suite contains both:

- Selenium UI tests
- REST API tests

---

## Running the Project Locally

Clone the repository:

    git clone https://github.com/yavuzhankiyi/qa-automation-project.git

Navigate to the project:

    cd qa-automation-project

Create a virtual environment:

    python -m venv venv

Activate the environment on Windows:

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Run all tests:

    pytest -v

---

## Run UI Tests Only

    pytest tests/ -v

---

## Run API Tests Only

    pytest api-tests/python/ -v

---

## Generate HTML Test Report

    pytest -v --html=reports/test-report.html --self-contained-html

---

## Page Object Model

The UI automation framework follows the Page Object Model design pattern.

Page classes are located inside:

    pages/

Each page object contains:

- Element locators
- Page interactions
- Explicit waits
- Reusable page methods

This keeps test code readable and maintainable.

---

## Screenshot on Failure

If a Selenium test fails, the framework automatically saves a screenshot to:

    reports/screenshots/

This makes debugging failed test executions easier.

---

## GitHub Actions

Automated tests run on GitHub Actions whenever code is pushed to the main branch.

The workflow:

1. Checks out the repository
2. Configures Python
3. Installs project dependencies
4. Runs all Pytest tests
5. Generates an HTML test report
6. Uploads the test report as a GitHub Actions artifact

---

## Manual Testing

The project also contains manual QA documentation.

### Manual Test Cases

Located at:

    manual-tests/test-cases.md

Includes:

- Positive test scenarios
- Negative test scenarios
- Preconditions
- Test steps
- Expected results
- Priority
- Test type

### Bug Reports

Located at:

    manual-tests/bug-reports.md

Includes:

- Bug ID
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Status

---

## Testing Concepts Demonstrated

This project demonstrates practical knowledge of:

- Functional Testing
- Regression Testing
- Positive Testing
- Negative Testing
- UI Automation
- API Testing
- Test Case Design
- Bug Reporting
- Explicit Waits
- Test Parameterization
- Page Object Model
- CI Test Execution
- Automated Reporting

---

## Author

**Yavuzhan Kiyi**

Computer Engineer

Interested in:

- Software Testing
- QA Automation
- DevOps
- Software Engineering