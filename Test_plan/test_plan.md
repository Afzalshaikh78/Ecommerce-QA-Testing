# Software Test Plan – SauceDemo E-commerce Website

## 1. Project Overview

**Application:** https://www.saucedemo.com/

**Project:** E-commerce Website – End-to-End QA Testing

**Objective:** Validate the main e-commerce workflows through manual testing and Selenium automation.

## 2. Scope of Testing

### In Scope
- Login and authentication
- Product listing and product details
- Product count and sorting
- Add and remove products from cart
- Cart validation
- Checkout form validation
- Order overview and confirmation
- Logout and navigation
- Regression testing

### Out of Scope
- Real payment gateway testing
- Bank transaction testing
- Backend database validation
- Email notification testing
- Production load and stress testing

## 3. Testing Types

- Functional Testing
- Positive Testing
- Negative Testing
- Boundary Testing
- UI Testing
- End-to-End Testing
- Regression Testing
- Automation Testing

## 4. Test Environment

| Component | Environment |
|---|---|
| Operating System | Windows |
| Browser | Google Chrome |
| Language | Python |
| Automation | Selenium WebDriver |
| Test Framework | Pytest |
| Defect Tracking | Jira |
| Version Control | Git and GitHub |
| Test Case Documentation | Microsoft Excel |

## 5. Test Approach

1. Analyze application requirements and workflows.
2. Identify test scenarios.
3. Design and document manual test cases.
4. Execute test cases and record actual results.
5. Report defects in Jira.
6. Automate selected test cases using Selenium and Pytest.
7. Execute regression tests.
8. Prepare test execution and summary reports.

## 6. Entry Criteria

- Application is accessible.
- Test environment and browser are available.
- Test scenarios and test cases are prepared.
- Required test data is available.

## 7. Exit Criteria

- Planned test cases have been executed or their pending status documented.
- Critical defects are reported.
- Automation results are recorded.
- Known failures and limitations are documented.
- Test execution summary is prepared.

## 8. Defect Management

Defects are documented with:
- Defect ID
- Summary
- Steps to reproduce
- Expected result
- Actual result
- Severity and priority
- Evidence
- Status

Known defect: **SQA-1 – Checkout allowed with an empty cart.**

## 9. Deliverables

- Test Plan
- Test Scenarios
- Manual Test Cases
- Test Execution Results
- Defect Reports
- Requirement Traceability Matrix
- Automation Test Suite
- Automation Execution Report
- Final Test Summary

## 10. Risks and Limitations

- Application behavior may change.
- Browser or network instability may affect automation.
- Testing is limited to the publicly accessible application workflows.
- No access to internal backend systems or real payment processing is available.
