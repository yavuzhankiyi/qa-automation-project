# Severity and Priority Matrix

## Project

QA Automation Project

---

## Purpose

This document explains the difference between Severity and Priority and defines how defects can be classified in the QA Automation Project.

---

## Severity

Severity describes how strongly a defect affects the functionality of the application.

Severity is generally evaluated from a technical and functional perspective.

---

## Priority

Priority describes how urgently a defect should be fixed.

Priority is generally evaluated from a business and delivery perspective.

---

## Severity Levels

### Critical

A critical defect prevents the application or a major business flow from functioning.

Examples:

- Application cannot start
- All users are unable to login
- Checkout cannot be completed by any user
- Data corruption
- System crash

Expected Action:

    Immediate investigation and resolution

---

### Major

A major defect affects an important feature but the application remains partially usable.

Examples:

- User cannot add products to the cart
- Required form validation does not work
- Checkout fails under a common scenario
- API returns incorrect data

Expected Action:

    Should be fixed before release

---

### Medium

A medium severity defect affects functionality but has limited impact or a workaround exists.

Examples:

- Cart update is delayed
- Sorting behaves incorrectly in one scenario
- UI interaction is inconsistent
- Non-critical validation behaves incorrectly

Expected Action:

    Should be planned for correction

---

### Minor

A minor defect has little impact on functionality.

Examples:

- Alignment problem
- Typographical error
- Incorrect icon
- Minor visual inconsistency

Expected Action:

    Can be fixed in a later release

---

## Priority Levels

### P1 - Critical Priority

The defect requires immediate resolution.

Examples:

- Production system is unavailable
- Login is broken for all users
- Payment or checkout completely fails
- Critical security vulnerability

---

### P2 - High Priority

The defect should be resolved as soon as possible.

Examples:

- Important business function fails
- Major checkout validation issue
- Critical regression issue
- Important API endpoint fails

---

### P3 - Medium Priority

The defect should be fixed but does not block the release.

Examples:

- Sorting problem
- Non-critical UI issue
- Minor workflow inconsistency

---

### P4 - Low Priority

The defect has low business impact.

Examples:

- Cosmetic issue
- Typographical mistake
- Minor styling inconsistency

---

## Severity vs Priority Examples

| Scenario | Severity | Priority | Explanation |
|---|---|---|---|
| Application crashes during login | Critical | P1 | Core application flow is unavailable |
| Checkout cannot be completed | Critical | P1 | Critical business flow is blocked |
| Invalid login error text is incorrect | Medium | P3 | Login still works but feedback is incorrect |
| Company logo is slightly misaligned | Minor | P4 | No functional impact |
| Sale banner shows wrong campaign date | Minor | P1 | Small technical issue but urgent business impact |
| Rare admin feature crashes | Major | P3 | High technical impact but limited user impact |
| Product cannot be removed from cart | Major | P2 | Important shopping functionality is affected |
| Sorting order is incorrect | Medium | P3 | Feature is incorrect but main purchasing flow works |

---

## Important Difference

Severity answers:

    How serious is the defect?

Priority answers:

    How quickly should the defect be fixed?

A defect can have:

    High Severity + High Priority

Example:

    Checkout completely fails.

A defect can also have:

    Low Severity + High Priority

Example:

    A promotional banner displays the wrong campaign date during an active marketing campaign.

A defect can have:

    High Severity + Low Priority

Example:

    A rarely used internal admin function crashes but does not affect customers.

---

## Defect Classification Example

### Example 1

Bug:

    User cannot complete checkout.

Severity:

    Critical

Priority:

    P1

Reason:

    Checkout is a critical business function and users cannot complete purchases.

---

### Example 2

Bug:

    Incorrect validation message is displayed.

Severity:

    Medium

Priority:

    P3

Reason:

    The application continues functioning but the user receives incorrect feedback.

---

### Example 3

Bug:

    Product card spacing is inconsistent.

Severity:

    Minor

Priority:

    P4

Reason:

    The problem is visual and does not affect functionality.

---

## Bug Report Fields

A complete bug report should generally include:

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
- Screenshot or video when applicable
- Logs when applicable

---

## Bug Life Cycle

A common defect life cycle may include:

    New
    ↓
    Assigned
    ↓
    In Progress
    ↓
    Fixed
    ↓
    Retest
    ↓
    Closed

If the problem still exists after retesting:

    Reopened

---

## QA Interview Notes

Severity is primarily related to:

    Technical impact

Priority is primarily related to:

    Business urgency

Severity is commonly determined with QA and development input.

Priority is commonly influenced by:

- Product Owner
- Project Manager
- Business Stakeholders
- QA Team
- Development Team

---

## Author

Yavuzhan Kiyi

Computer Engineer