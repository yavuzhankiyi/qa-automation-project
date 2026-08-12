# API Test Documentation

## Project

QA Automation Project

---

## API Under Test

JSONPlaceholder

Base URL:

    https://jsonplaceholder.typicode.com

---

## Purpose

The purpose of this document is to describe the API test scenarios implemented in the QA Automation Project.

The API test suite validates basic CRUD operations and negative scenarios using both Python Requests and Postman.

---

## Tools Used

- Python
- Requests
- Pytest
- Postman
- GitHub Actions

---

## API Test Coverage

The API test suite covers the following HTTP methods:

- GET
- POST
- PUT
- DELETE

---

## Test Scenario Summary

| Test ID | Method | Endpoint | Scenario | Expected Status |
|---|---|---|---|---|
| API-TC-001 | GET | /posts | Get all posts | 200 |
| API-TC-002 | GET | /posts/1 | Get single post | 200 |
| API-TC-003 | POST | /posts | Create new post | 201 |
| API-TC-004 | PUT | /posts/1 | Update existing post | 200 |
| API-TC-005 | DELETE | /posts/1 | Delete existing post | 200 |
| API-TC-006 | GET | /posts/999999 | Request invalid resource | 404 |

---

# API-TC-001 - Get All Posts

## Method

GET

## Endpoint

    /posts

## Full URL

    https://jsonplaceholder.typicode.com/posts

## Objective

Verify that the API successfully returns the list of posts.

## Expected Status Code

    200

## Validations

- Response status code should be 200.
- Response body should contain data.
- The returned list should contain at least one post.
- Each post should contain an ID.
- Each post should contain a title.
- Each post should contain a body.
- Each post should contain a userId.

## Automated Test

    test_get_all_posts

## Result

    PASS

---

# API-TC-002 - Get Single Post

## Method

GET

## Endpoint

    /posts/1

## Full URL

    https://jsonplaceholder.typicode.com/posts/1

## Objective

Verify that a specific post can be retrieved successfully.

## Expected Status Code

    200

## Validations

- Response status code should be 200.
- Returned post ID should be 1.
- Response should contain a title.
- Response should contain a body.
- Response body should not be empty.

## Automated Test

    test_get_single_post

## Result

    PASS

---

# API-TC-003 - Create New Post

## Method

POST

## Endpoint

    /posts

## Full URL

    https://jsonplaceholder.typicode.com/posts

## Objective

Verify that a new post can be created.

## Request Body

    {
        "title": "QA Automation Project",
        "body": "API testing with Python",
        "userId": 1
    }

## Expected Status Code

    201

## Validations

- Response status code should be 201.
- Response should contain an ID.
- Returned title should match the request.
- Returned userId should match the request.

## Automated Test

    test_create_post

## Result

    PASS

---

# API-TC-004 - Update Existing Post

## Method

PUT

## Endpoint

    /posts/1

## Full URL

    https://jsonplaceholder.typicode.com/posts/1

## Objective

Verify that an existing post can be updated.

## Request Body

    {
        "id": 1,
        "title": "Updated QA Project",
        "body": "Updated using Python",
        "userId": 1
    }

## Expected Status Code

    200

## Validations

- Response status code should be 200.
- Returned ID should remain 1.
- Returned title should match the updated title.
- Returned userId should remain 1.

## Automated Test

    test_update_post

## Result

    PASS

---

# API-TC-005 - Delete Existing Post

## Method

DELETE

## Endpoint

    /posts/1

## Full URL

    https://jsonplaceholder.typicode.com/posts/1

## Objective

Verify that a delete request is accepted successfully.

## Expected Status Code

    200

## Validations

- Response status code should be 200.
- Request should complete without an error.

## Automated Test

    test_delete_post

## Result

    PASS

---

# API-TC-006 - Invalid Resource Request

## Method

GET

## Endpoint

    /posts/999999

## Full URL

    https://jsonplaceholder.typicode.com/posts/999999

## Objective

Verify the API response when requesting a resource that does not exist.

## Expected Status Code

    404

## Validations

- Response status code should be 404.
- API should not return a valid post for the invalid resource ID.

## Automated Test

    test_invalid_post

## Result

    PASS

---

## Python API Automation

Python API tests are located in:

    api-tests/python/test_api.py

The test suite uses the Requests library to send HTTP requests.

Example:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

Status codes and response body data are validated using Pytest assertions.

---

## Postman API Testing

The project also contains a Postman collection.

Location:

    api-tests/postman/E-Commerce-QA-API-Tests.postman_collection.json

The Postman collection contains tests for:

- GET all posts
- GET single post
- POST new post
- PUT existing post
- DELETE existing post
- Invalid resource request

---

## Status Code Coverage

| Status Code | Meaning | Covered |
|---|---|---|
| 200 | Successful Request | Yes |
| 201 | Resource Created | Yes |
| 404 | Resource Not Found | Yes |

---

## CRUD Coverage

| Operation | HTTP Method | Covered |
|---|---|---|
| Create | POST | Yes |
| Read | GET | Yes |
| Update | PUT | Yes |
| Delete | DELETE | Yes |

CRUD Coverage:

    100%

---

## Negative Testing

Negative API testing currently includes:

- Requesting a non-existing post.
- Validating 404 response behavior.

Future improvements may include:

- Invalid request body validation
- Missing required fields
- Invalid data types
- Unauthorized requests
- Rate limit scenarios
- Response time validation

---

## CI Integration

API tests are automatically executed by GitHub Actions.

The workflow executes:

    pytest -v

This runs both UI automation tests and API tests.

The CI pipeline validates API behavior whenever changes are pushed to the main branch.

---

## Current API Test Result

Total API Tests:

    6

Passed:

    6

Failed:

    0

Final Result:

    PASS

---

## Skills Demonstrated

This API testing implementation demonstrates practical knowledge of:

- REST API Testing
- HTTP Methods
- Status Code Validation
- JSON Response Validation
- CRUD Testing
- Positive API Testing
- Negative API Testing
- Python Requests
- Pytest
- Postman
- CI Integration

---

## Author

Yavuzhan Kiyi

Computer Engineer