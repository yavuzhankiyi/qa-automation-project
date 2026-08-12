# Manual Test Cases

## Project
QA Automation Project

## Test Application
SauceDemo

## Test Environment
- Browser: Google Chrome
- OS: Windows / Linux CI
- Test URL: https://www.saucedemo.com/

---

# TC-001 - Successful Login

**Test Case ID:** TC-001

**Test Scenario:** Login with valid credentials

**Preconditions:**
- User is on the SauceDemo login page.

**Test Steps:**
1. Enter `standard_user` into the Username field.
2. Enter `secret_sauce` into the Password field.
3. Click the Login button.

**Expected Result:**
- User should successfully log in.
- Products page should be displayed.

**Priority:** High

**Test Type:** Positive

---

# TC-002 - Login With Invalid Password

**Test Case ID:** TC-002

**Test Scenario:** Login with invalid password

**Preconditions:**
- User is on the SauceDemo login page.

**Test Steps:**
1. Enter `standard_user` into the Username field.
2. Enter an incorrect password.
3. Click the Login button.

**Expected Result:**
- User should not be logged in.
- An error message should be displayed.

**Priority:** High

**Test Type:** Negative

---

# TC-003 - Login With Empty Username

**Test Case ID:** TC-003

**Test Scenario:** Login without entering username

**Preconditions:**
- User is on the SauceDemo login page.

**Test Steps:**
1. Leave the Username field empty.
2. Enter `secret_sauce` into the Password field.
3. Click the Login button.

**Expected Result:**
- Login should fail.
- `Username is required` error should be displayed.

**Priority:** High

**Test Type:** Negative

---

# TC-004 - Add Product To Cart

**Test Case ID:** TC-004

**Test Scenario:** Add Sauce Labs Backpack to cart

**Preconditions:**
- User is logged in.
- Products page is displayed.

**Test Steps:**
1. Locate Sauce Labs Backpack.
2. Click the Add to cart button.
3. Check the cart badge.

**Expected Result:**
- Product should be added to the cart.
- Cart badge should display `1`.

**Priority:** High

**Test Type:** Positive

---

# TC-005 - Verify Product In Cart

**Test Case ID:** TC-005

**Test Scenario:** Verify added product appears in cart

**Preconditions:**
- User is logged in.
- Sauce Labs Backpack has been added to the cart.

**Test Steps:**
1. Open the shopping cart.
2. Check the product list.

**Expected Result:**
- `Sauce Labs Backpack` should be displayed in the cart.

**Priority:** High

**Test Type:** Positive

---

# TC-006 - Remove Product From Cart

**Test Case ID:** TC-006

**Test Scenario:** Remove product from shopping cart

**Preconditions:**
- User is logged in.
- Sauce Labs Backpack is in the cart.

**Test Steps:**
1. Open the shopping cart.
2. Click the Remove button.

**Expected Result:**
- Sauce Labs Backpack should be removed from the cart.

**Priority:** Medium

**Test Type:** Positive

---

# TC-007 - Successful Checkout

**Test Case ID:** TC-007

**Test Scenario:** Complete checkout with valid customer information

**Preconditions:**
- User is logged in.
- At least one product is in the cart.

**Test Steps:**
1. Open the shopping cart.
2. Click Checkout.
3. Enter a valid first name.
4. Enter a valid last name.
5. Enter a valid postal code.
6. Click Continue.
7. Click Finish.

**Expected Result:**
- Checkout should complete successfully.
- `Thank you for your order!` message should be displayed.

**Priority:** Critical

**Test Type:** Positive

---

# TC-008 - Checkout Without First Name

**Test Case ID:** TC-008

**Test Scenario:** Attempt checkout without first name

**Preconditions:**
- User is logged in.
- At least one product is in the cart.
- Checkout page is displayed.

**Test Steps:**
1. Leave First Name empty.
2. Enter a valid Last Name.
3. Enter a valid Postal Code.
4. Click Continue.

**Expected Result:**
- Checkout should not continue.
- `First Name is required` error should be displayed.

**Priority:** High

**Test Type:** Negative

---

# TC-009 - Checkout Without Postal Code

**Test Case ID:** TC-009

**Test Scenario:** Attempt checkout without postal code

**Preconditions:**
- User is logged in.
- At least one product is in the cart.
- Checkout page is displayed.

**Test Steps:**
1. Enter a valid First Name.
2. Enter a valid Last Name.
3. Leave Postal Code empty.
4. Click Continue.

**Expected Result:**
- Checkout should not continue.
- `Postal Code is required` error should be displayed.

**Priority:** High

**Test Type:** Negative

---

# TC-010 - Sort Products Price Low To High

**Test Case ID:** TC-010

**Test Scenario:** Sort products by ascending price

**Preconditions:**
- User is logged in.
- Products page is displayed.

**Test Steps:**
1. Open the sorting dropdown.
2. Select `Price (low to high)`.

**Expected Result:**
- Products should be ordered from the lowest price to the highest price.

**Priority:** Medium

**Test Type:** Functional

---

# TC-011 - Sort Products Price High To Low

**Test Case ID:** TC-011

**Test Scenario:** Sort products by descending price

**Preconditions:**
- User is logged in.
- Products page is displayed.

**Test Steps:**
1. Open the sorting dropdown.
2. Select `Price (high to low)`.

**Expected Result:**
- Products should be ordered from the highest price to the lowest price.

**Priority:** Medium

**Test Type:** Functional