# Requirements Traceability Matrix

## Project

QA Automation Project

---

## Purpose

The purpose of this Requirements Traceability Matrix is to map application requirements to corresponding manual and automated test cases.

This document helps ensure that critical application requirements are covered by testing activities.

---

## Requirements

| Requirement ID | Requirement Description | Priority |
|---|---|---|
| REQ-001 | User should be able to login with valid credentials | High |
| REQ-002 | User should receive an error when login credentials are invalid | High |
| REQ-003 | Username field should be mandatory | High |
| REQ-004 | Password field should be mandatory | High |
| REQ-005 | User should be able to add a product to the cart | High |
| REQ-006 | Cart badge should display the number of added products | High |
| REQ-007 | Added product should be visible in the shopping cart | High |
| REQ-008 | User should be able to remove a product from the cart | Medium |
| REQ-009 | User should be able to proceed to checkout | High |
| REQ-010 | First Name should be mandatory during checkout | High |
| REQ-011 | Postal Code should be mandatory during checkout | High |
| REQ-012 | User should be able to complete checkout with valid information | Critical |
| REQ-013 | Products should be sortable from low price to high price | Medium |
| REQ-014 | Products should be sortable from high price to low price | Medium |
| REQ-015 | API should return all posts successfully | High |
| REQ-016 | API should return a specific post successfully | High |
| REQ-017 | API should allow creating a post | High |
| REQ-018 | API should allow updating a post | High |
| REQ-019 | API should allow deleting a post | High |
| REQ-020 | API should return an appropriate response for an invalid resource | Medium |

---

## Traceability Matrix

| Requirement ID | Manual Test Case | Automated Test | Status |
|---|---|---|---|
| REQ-001 | TC-001 | test_valid_login | Covered |
| REQ-002 | TC-002 | test_invalid_login | Covered |
| REQ-003 | TC-003 | test_invalid_login | Covered |
| REQ-004 | TC-003 / Login Negative Scenario | test_invalid_login | Covered |
| REQ-005 | TC-004 | test_add_product_to_cart | Covered |
| REQ-006 | TC-004 | test_add_product_to_cart | Covered |
| REQ-007 | TC-005 | test_add_product_to_cart | Covered |
| REQ-008 | TC-006 | test_remove_product_from_cart | Covered |
| REQ-009 | TC-007 | test_successful_checkout | Covered |
| REQ-010 | TC-008 | test_checkout_without_first_name | Covered |
| REQ-011 | TC-009 | test_checkout_without_postal_code | Covered |
| REQ-012 | TC-007 | test_successful_checkout | Covered |
| REQ-013 | TC-010 | test_sort_price_low_to_high | Covered |
| REQ-014 | TC-011 | test_sort_price_high_to_low | Covered |
| REQ-015 | API Test Documentation | test_get_all_posts | Covered |
| REQ-016 | API Test Documentation | test_get_single_post | Covered |
| REQ-017 | API Test Documentation | test_create_post | Covered |
| REQ-018 | API Test Documentation | test_update_post | Covered |
| REQ-019 | API Test Documentation | test_delete_post | Covered |
| REQ-020 | API Test Documentation | test_invalid_post | Covered |

---

## Coverage Summary

Total Requirements:

    20

Covered Requirements:

    20

Not Covered Requirements:

    0

Requirement Coverage:

    100%

---

## Functional Coverage

### Authentication

Covered requirements:

- REQ-001
- REQ-002
- REQ-003
- REQ-004

Coverage:

    100%

---

### Shopping Cart

Covered requirements:

- REQ-005
- REQ-006
- REQ-007
- REQ-008

Coverage:

    100%

---

### Checkout

Covered requirements:

- REQ-009
- REQ-010
- REQ-011
- REQ-012

Coverage:

    100%

---

### Product Sorting

Covered requirements:

- REQ-013
- REQ-014

Coverage:

    100%

---

### API

Covered requirements:

- REQ-015
- REQ-016
- REQ-017
- REQ-018
- REQ-019
- REQ-020

Coverage:

    100%

---

## Traceability Benefits

This traceability matrix provides:

- Requirement coverage visibility
- Test coverage visibility
- Easier regression planning
- Identification of untested requirements
- Relationship between requirements and test cases
- Relationship between manual and automated testing
- Better QA documentation

---

## Current Status

All currently defined project requirements have corresponding test coverage.

Current automated regression suite:

    18 tests
    18 passed
    0 failed

Requirement coverage:

    100%

---

## Author

Yavuzhan Kiyi

Computer Engineer