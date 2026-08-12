# Bug Reports

## Project
QA Automation Project

## Application
SauceDemo

---

# BUG-001 - Checkout allows submission with missing required data

**Bug ID:** BUG-001

**Title:** Checkout validation does not correctly prevent missing required information

**Environment:**
- Browser: Google Chrome
- OS: Windows / Linux
- Application: SauceDemo
- URL: https://www.saucedemo.com/

**Preconditions:**
- User is logged in.
- At least one product is added to the cart.
- User is on the checkout information page.

**Steps to Reproduce:**
1. Open the shopping cart.
2. Click the Checkout button.
3. Leave one required field empty.
4. Fill the remaining fields.
5. Click Continue.

**Expected Result:**
- Checkout should not continue.
- A validation message for the missing required field should be displayed.

**Actual Result:**
- Validation behavior may not match the expected required-field validation.

**Severity:** Major

**Priority:** High

**Status:** Open

---

# BUG-002 - Cart item may remain visible after removal

**Bug ID:** BUG-002

**Title:** Product remains visible after clicking Remove from cart

**Environment:**
- Browser: Google Chrome
- OS: Windows / Linux
- Application: SauceDemo
- URL: https://www.saucedemo.com/cart.html

**Preconditions:**
- User is logged in.
- Sauce Labs Backpack is added to the cart.
- User is on the shopping cart page.

**Steps to Reproduce:**
1. Navigate to the cart.
2. Verify that Sauce Labs Backpack is displayed.
3. Click the Remove button.
4. Observe the cart contents.

**Expected Result:**
- Sauce Labs Backpack should immediately disappear from the cart.
- Cart item count should be updated.

**Actual Result:**
- Product may remain visible temporarily after clicking Remove.

**Severity:** Medium

**Priority:** Medium

**Status:** Open

---

# BUG-003 - Cart navigation may fail in headless browser execution

**Bug ID:** BUG-003

**Title:** Shopping cart navigation is unreliable in headless Chrome

**Environment:**
- Browser: Google Chrome Headless
- OS: Linux
- CI Platform: GitHub Actions
- Application: SauceDemo

**Preconditions:**
- Automated test is running in GitHub Actions.
- User is logged in.
- Product has been added to the cart.

**Steps to Reproduce:**
1. Run Selenium tests in headless Chrome.
2. Login with valid credentials.
3. Add Sauce Labs Backpack to the cart.
4. Click the shopping cart icon.

**Expected Result:**
- Browser should navigate to `cart.html`.

**Actual Result:**
- Navigation may not occur and Selenium may reach a timeout.

**Severity:** Medium

**Priority:** High

**Status:** Resolved in Automation Framework

**Resolution:**
- Cart navigation was stabilized by navigating directly to the cart URL during automation execution.

---

# BUG-004 - Checkout interaction unstable in headless CI environment

**Bug ID:** BUG-004

**Title:** Checkout form interactions are unstable during headless execution

**Environment:**
- Browser: Google Chrome Headless
- OS: Linux
- CI Platform: GitHub Actions
- Application: SauceDemo

**Preconditions:**
- User is logged in.
- Product is available in the shopping cart.
- Automated Selenium tests are running.

**Steps to Reproduce:**
1. Navigate to the cart.
2. Click Checkout.
3. Enter customer information.
4. Click Continue.
5. Attempt to finish the order.

**Expected Result:**
- Customer data should be entered successfully.
- Checkout should proceed to the overview page.
- Finish button should complete the order.

**Actual Result:**
- Input or button interactions may occasionally fail in headless execution.

**Severity:** Medium

**Priority:** High

**Status:** Resolved in Automation Framework

**Resolution:**
- Explicit waits were added.
- JavaScript-based interactions were used for unstable elements.
- Form values were verified before continuing the checkout flow.