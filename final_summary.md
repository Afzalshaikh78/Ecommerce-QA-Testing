## 2. Manual Test Case Coverage

| Metric | Result |
|---|---:|
| Total manual test cases designed | 47 |
| Login | 7 |
| Inventory | 12 |
| Cart | 12 |
| Checkout | 16 |

These 47 test cases are documented in the consolidated Excel workbook. Their manual execution status must be tracked separately.

## 3. Automation Execution Results

| Metric | Result |
|---|---:|
| Automation tests executed | 25 |
| Passed | 24 |
| Failed | 1 |
| Pass rate | 96% |

## 4. Known Defect

**Defect:** Empty-cart checkout  
**Jira ID:** SQA-1  
**Status:** Open

The failing automation test detects that the application allows checkout to proceed with zero products.
