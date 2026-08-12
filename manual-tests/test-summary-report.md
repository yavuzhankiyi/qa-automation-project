# Test Summary Report

## 1. Project Name

QA Automation Project

---

## 2. Test Objective

The purpose of this test execution was to validate the core functionality of the SauceDemo web application and JSONPlaceholder API using both automated and manual QA practices.

The test suite covers UI functionality, API behavior, form validation, shopping cart operations, checkout scenarios, product sorting, and negative test cases.

---

## 3. Test Environment

### Local Environment

- Operating System: Windows
- Browser: Google Chrome
- Programming Language: Python
- Test Framework: Pytest
- UI Automation Tool: Selenium WebDriver

### CI Environment

- Platform: GitHub Actions
- Operating System: Ubuntu Linux
- Browser: Google Chrome Headless
- Python Version: 3.13
- CI Trigger: Push and Pull Request to main branch

---

## 4. Applications Under Test

### UI Testing

SauceDemo

https://www.saucedemo.com/

### API Testing

JSONPlaceholder

https://jsonplaceholder.typicode.com/

---

## 5. Test Execution Summary

Current automated regression suite:

    Total Tests: 18
    Passed: 18
    Failed: 0
    Errors: 0

Final Result:

    PASS

The complete automation suite successfully passed in both local execution and GitHub Actions CI.

---

## 6. UI Automation Results

### Login Tests

Covered scenarios:

- Successful login
- Login with invalid password
- Login with empty username
- Login with empty password
- Login with empty username and password

Result:

    PASS

---

### Cart Tests

Covered scenarios:

- Add Sauce Labs Backpack to cart
- Verify cart badge
- Verify product in cart
- Remove product from cart

Result:

    PASS

---

### Checkout Tests

Covered scenarios:

- Successful checkout
- Checkout without first name
- Checkout without postal code

Result:

    PASS

---

### Product Sorting Tests

Covered scenarios:

- Sort products by Price Low to High
- Sort products by Price High to Low

Result:

    PASS

---

## 7. API Automation Results

API tests were implemented using Python Requests and Pytest.

Covered HTTP methods:

- GET
- POST
- PUT
- DELETE

Covered scenarios:

- Get all posts
- Get single post
- Create new post
- Update existing post
- Delete post
- Request invalid post

Result:

    PASS

---

## 8. Manual Testing Results

Manual test cases were created for the major user flows.

Manual documentation includes:

- Positive scenarios
- Negative scenarios
- Preconditions
- Test steps
- Expected results
- Test priorities
- Test types

Manual test case documentation is available at:

    manual-tests/test-cases.md

---

## 9. Defect Documentation

Bug report documentation is included in:

    manual-tests/bug-reports.md

The bug report format includes:

- Bug ID
- Title
- Environment
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Priority
- Status

Some issues identified during automation development were related to headless browser execution and automation stability rather than confirmed application defects.

These automation issues were resolved inside the test framework using:

- Explicit waits
- Stable navigation methods
- JavaScript interactions where required
- Element state validation
- Input value validation

---

## 10. Automation Framework Summary

The project uses the Page Object Model design pattern.

Page objects:

- LoginPage
- ProductsPage
- CartPage
- CheckoutPage

Framework capabilities include:

- Reusable page methods
- Selenium WebDriver
- Explicit waits
- Pytest fixtures
- Parameterized tests
- Failure screenshots
- HTML reports
- GitHub Actions CI
- API automation

---

## 11. CI/CD Test Execution

The automated regression suite is executed using GitHub Actions.

Workflow behavior:

1. Checkout repository
2. Configure Python environment
3. Install dependencies
4. Execute automated tests
5. Generate HTML test report
6. Upload test report as CI artifact

The CI pipeline successfully validates the project after changes are pushed to the main branch.

---

## 12. Test Reporting

The project supports HTML test reporting using pytest-html.

Example command:

    pytest -v --html=reports/test-report.html --self-contained-html

Failure screenshots are automatically stored in:

    reports/screenshots/

Generated test reports and screenshots are excluded from Git version control.

---

## 13. Risks and Limitations

The following limitations exist:

- UI tests currently focus on Google Chrome.
- The test application is an external demo application.
- External application changes may break locators.
- API tests depend on JSONPlaceholder availability.
- Performance testing is not included.
- Security testing is not included.
- Accessibility testing is not included.
- Mobile testing is not included.

---

## 14. Final Assessment

The automated regression suite successfully validates the main functional flows included in the project.

Final automated test result:

    18 Passed
    0 Failed

The project demonstrates practical knowledge of:

- Software Testing
- Manual Testing
- Test Case Design
- Functional Testing
- Negative Testing
- UI Automation
- API Testing
- Selenium WebDriver
- Pytest
- Page Object Model
- Bug Reporting
- Regression Testing
- CI/CD Testing
- GitHub Actions
- Automated Reporting

---

## 15. Conclusion

The QA Automation Project successfully demonstrates a complete beginner-to-intermediate QA workflow combining manual and automated software testing.

The project includes test planning, test case design, UI automation, API testing, defect documentation, regression testing, CI execution, failure screenshots, and automated reporting.

All current automated tests are passing successfully.

---

## Author

Yavuzhan Kiyi

Computer Engineer