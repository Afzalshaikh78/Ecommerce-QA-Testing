# E-commerce Website – End-to-End QA Testing

An end-to-end software testing project on [SauceDemo](https://www.saucedemo.com/), covering manual testing, test case design, defect reporting, and UI automation using Selenium with Python.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Jira
- Git and GitHub
- Excel

## Testing Scope

- Login and authentication validation
- Product listing and sorting
- Add/remove cart functionality
- Cart validation
- Checkout form validation
- Order summary and confirmation
- Regression testing

## Project Structure

```text
Ecommerce-QA-Testing/
├── 01_Test_Plan/
├── 02_Test_Scenarios/
├── 03_Test_Cases/
├── 04_Test_Execution/
├── 05_Bug_Reports/
├── 06_RTM/
├── 07_Test_Summary/
├── 08_Automation/
├── pages/
├── tests/
├── test_data/
├── utilities/
├── reports/
├── screenshots/
├── conftest.py
├── requirements.txt
└── README.md
```

## Automation Framework

Implemented using the Page Object Model (POM).

- Reusable page classes
- Explicit waits
- Data-driven login tests using JSON
- Pytest fixtures for browser setup and teardown
- Logging
- Automated regression tests

## Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest -v tests/
```

## Latest Automation Results

| Metric | Result |
|---|---:|
| Total tests | 25 |
| Passed | 24 |
| Failed | 1 |

The failing test identifies a known application defect: checkout can proceed with an empty cart.

## Defect Tracking

**Jira Issue:** SQA-1

**Title:** Application allows checkout completion with an empty cart.

**Expected:** Checkout should be prevented when the cart contains no products.

**Actual:** The application allows the empty-cart checkout flow to proceed.

**Status:** Open

## Scope Limitations

This project tests the application's available UI workflows. It does not include real payment processing, backend database validation, or production load testing.

## Author

Afzal Shaikh
