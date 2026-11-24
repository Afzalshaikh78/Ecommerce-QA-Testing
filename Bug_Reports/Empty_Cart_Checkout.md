# BUG-001: Checkout Allowed with Empty Cart

**Project:** SauceDemo E-commerce QA  
**Bug ID:** BUG-001  
**Related Jira ID:** SQA-1  
**Module:** Checkout  
**Severity:** Major  
**Priority:** High  
**Status:** Open  
**Reported By:** QA Tester

## Environment
- Application: https://www.saucedemo.com/
- Browser: Google Chrome
- Operating System: Windows 11

## Preconditions
1. User is logged in.
2. Shopping cart contains zero products.

## Steps to Reproduce
1. Open SauceDemo.
2. Log in using valid credentials.
3. Navigate to the cart.
4. Ensure the cart is empty.
5. Click Checkout.
6. Enter valid customer details.
7. Continue to the order overview.
8. Click Finish.

## Expected Result
The application should prevent checkout when the cart is empty and display an appropriate validation message.

## Actual Result
The application allows the checkout process to proceed with zero products and displays an order confirmation.

## Impact
Users can complete an order with no products in their cart, resulting in an invalid order flow.

## Evidence
- Manual testing confirmed the issue.
- Automated test: `test_empty_cart_checkout_defect`
- Assertion: `assert checkout.get_item_count() > 0`

## Related Jira Issue
SQA-1
