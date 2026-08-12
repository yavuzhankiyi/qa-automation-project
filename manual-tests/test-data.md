# Test Data Documentation

## Project

QA Automation Project

---

## Purpose

This document defines the test data used in manual and automated testing activities for the QA Automation Project.

The purpose of maintaining test data documentation is to ensure repeatable, consistent, and understandable test execution.

---

## UI Application

Application:

    SauceDemo

URL:

    https://www.saucedemo.com/

---

## Login Test Data

### Valid User

Username:

    standard_user

Password:

    secret_sauce

Expected Result:

    User should successfully login and access the products page.

---

### Invalid Password Scenario

Username:

    standard_user

Password:

    wrong_password

Expected Result:

    Login should fail.

Expected Error:

    Username and password do not match

---

### Empty Username Scenario

Username:

    [EMPTY]

Password:

    secret_sauce

Expected Result:

    Login should fail.

Expected Error:

    Username is required

---

### Empty Password Scenario

Username:

    standard_user

Password:

    [EMPTY]

Expected Result:

    Login should fail.

Expected Error:

    Password is required

---

### Empty Credentials Scenario

Username:

    [EMPTY]

Password:

    [EMPTY]

Expected Result:

    Login should fail.

Expected Error:

    Username is required

---

## Product Test Data

Product Name:

    Sauce Labs Backpack

Expected Cart Quantity:

    1

Expected Result:

    Product should be successfully added to the shopping cart.

---

## Checkout Test Data

### Valid Checkout Data

First Name:

    Yavuzhan

Last Name:

    Kiyi

Postal Code:

    54000

Expected Result:

    Checkout should complete successfully.

Expected Completion Message:

    Thank you for your order!

---

### Missing First Name

First Name:

    [EMPTY]

Last Name:

    Kiyi

Postal Code:

    54000

Expected Result:

    Checkout should not continue.

Expected Error:

    First Name is required

---

### Missing Postal Code

First Name:

    Yavuzhan

Last Name:

    Kiyi

Postal Code:

    [EMPTY]

Expected Result:

    Checkout should not continue.

Expected Error:

    Postal Code is required

---

## Product Sorting Test Data

### Price Low to High

Sort Value:

    lohi

Expected Result:

    Product prices should be sorted in ascending order.

---

### Price High to Low

Sort Value:

    hilo

Expected Result:

    Product prices should be sorted in descending order.

---

## API Test Data

Base URL:

    https://jsonplaceholder.typicode.com

---

## GET All Posts

Endpoint:

    /posts

Expected Status Code:

    200

---

## GET Single Post

Endpoint:

    /posts/1

Expected Status Code:

    200

Expected Post ID:

    1

---

## Create Post

Endpoint:

    /posts

Method:

    POST

Request Body:

    {
        "title": "QA Automation Project",
        "body": "API testing with Python",
        "userId": 1
    }

Expected Status Code:

    201

---

## Update Post

Endpoint:

    /posts/1

Method:

    PUT

Request Body:

    {
        "id": 1,
        "title": "Updated QA Project",
        "body": "Updated using Python",
        "userId": 1
    }

Expected Status Code:

    200

---

## Delete Post

Endpoint:

    /posts/1

Method:

    DELETE

Expected Status Code:

    200

---

## Invalid Resource

Endpoint:

    /posts/999999

Method:

    GET

Expected Status Code:

    404

---

## Test Data Management Principles

The project follows these test data principles:

- Test data should be predictable.
- Test data should be reusable.
- Test data should not contain sensitive information.
- Positive and negative scenarios should use clearly separated values.
- Test data should produce repeatable test results.
- Expected results should be documented with the input data.

---

## Future Improvements

Future improvements may include:

- Moving test data into JSON files
- Using Pytest fixtures for centralized test data
- Environment-specific configuration files
- Dynamic test data generation
- Data-driven testing
- Faker integration
- Secret management using environment variables

---

## Author

Yavuzhan Kiyi

Computer Engineer