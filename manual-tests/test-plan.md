# Test Plan

## 1. Project Name

QA Automation Project

---

## 2. Objective

The objective of this test plan is to validate the core functionality of the SauceDemo web application and demonstrate both manual and automated software testing practices.

The project covers UI testing, API testing, automated regression testing, manual test case design, bug reporting, and continuous integration.

---

## 3. Scope

The following areas are included in the testing scope:

- User Login
- Product Listing
- Shopping Cart
- Checkout Process
- Product Sorting
- REST API Operations
- Form Validation
- Error Message Validation

---

## 4. Out of Scope

The following areas are not covered in this project:

- Performance Testing
- Load Testing
- Security Penetration Testing
- Mobile Application Testing
- Database Testing
- Cross-browser compatibility testing beyond Google Chrome
- Accessibility Testing

---

## 5. Test Applications

### UI Application

SauceDemo

https://www.saucedemo.com/

### API Application

JSONPlaceholder

https://jsonplaceholder.typicode.com/

---

## 6. Test Environment

### Local Environment

- Operating System: Windows
- Browser: Google Chrome
- Language: Python
- Test Framework: Pytest
- UI Automation: Selenium WebDriver

### CI Environment

- Platform: GitHub Actions
- Operating System: Ubuntu Linux
- Browser: Google Chrome Headless
- Python Version: 3.13

---

## 7. Testing Types

The project includes the following testing types:

- Functional Testing
- Regression Testing
- Positive Testing
- Negative Testing
- UI Automation Testing
- API Testing
- Form Validation Testing
- Integration Testing
- Manual Testing

---

## 8. Test Approach

### Manual Testing

Manual test cases are created for critical user flows.

Each test case includes:

- Test Case ID
- Scenario
- Preconditions
- Test Steps
- Expected Result
- Priority
- Test Type

### UI Automation

UI automation is implemented using:

- Python
- Selenium WebDriver
- Pytest
- Page Object Model

Automated UI tests cover:

- Login
- Cart
- Checkout
- Product Sorting

### API Automation

API tests are implemented using:

- Python Requests
- Pytest
- Postman

API coverage includes:

- GET
- POST
- PUT
- DELETE
- Invalid resource validation

---

## 9. Entry Criteria

Testing can begin when:

- Application is accessible.
- Test environment is available.
- Required test credentials are available.
- Python dependencies are installed.
- Browser and WebDriver are available.
- API endpoints are accessible.

---

## 10. Exit Criteria

Testing is considered complete when:

- All planned test scenarios have been executed.
- Critical functionality has been validated.
- Automated regression tests pass successfully.
- API tests complete successfully.
- Known issues are documented.
- CI pipeline executes successfully.

---

## 11. Test Data

### SauceDemo Login Credentials

Username:

    standard_user

Password:

    secret_sauce

### Checkout Test Data

First Name:

    Yavuzhan

Last Name:

    Kiyi

Postal Code:

    54000

---

## 12. Test Coverage

### Login

- Valid credentials
- Invalid password
- Empty username
- Empty password
- Empty credentials

### Cart

- Add product
- Verify cart count
- Verify cart item
- Remove product

### Checkout

- Successful checkout
- Missing first name validation
- Missing postal code validation

### Sorting

- Price Low to High
- Price High to Low

### API

- Get all posts
- Get single post
- Create post
- Update post
- Delete post
- Invalid post request

---

## 13. Automation Framework

The automation framework follows the Page Object Model design pattern.

Page objects include:

- LoginPage
- ProductsPage
- CartPage
- CheckoutPage

The framework also provides:

- Explicit waits
- Reusable page methods
- Pytest fixtures
- Parameterized tests
- Automatic screenshots on test failure
- HTML test reporting
- GitHub Actions execution

---

## 14. Defect Management

Defects are documented using the following information:

- Bug ID
- Title
- Environment
- Preconditions
- Steps to Reproduce
- Expected Result
- Actual Result
- Severity
- Priority
- Status

Bug documentation is stored in:

    manual-tests/bug-reports.md

---

## 15. Test Deliverables

The project includes the following testing deliverables:

- Automated UI Tests
- Automated API Tests
- Postman Collection
- Manual Test Cases
- Bug Reports
- Test Plan
- HTML Test Reports
- Failure Screenshots
- GitHub Actions CI Workflow
- Project Documentation

---

## 16. Risks

Possible risks include:

- External test applications may become unavailable.
- UI element locators may change.
- Network issues may affect API tests.
- Browser updates may affect Selenium execution.
- Headless browser behavior may differ from local browser execution.

---

## 17. Regression Strategy

The complete automated test suite is executed whenever changes are pushed to the main branch.

GitHub Actions automatically runs the regression test suite.

Current automated regression suite:

    18 tests

Expected result:

    18 passed
    0 failed

---

## 18. Test Completion Summary

The current automated test suite successfully validates the core user flows and API operations included in this project.

The project demonstrates practical experience with:

- Test Planning
- Test Case Design
- UI Automation
- API Testing
- Defect Reporting
- Regression Testing
- CI Integration
- Automated Reporting

---

## Author

Yavuzhan Kiyi

Computer Engineer