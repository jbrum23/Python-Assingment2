# Python-Assingment2

## Problem 1: Customer Discount Eligibility
### Description
This program determines a customer’s discount percentage based on membership status and purchase amount using conditional logic inside reusable functions.  
The program calculates and prints the final price after the discount is applied.
### Functions
- determine_discount(purchase_amount, membership_status)
- calculate_final_price(purchase_amount, discount_percent)
- main()
### Assumptions
- Purchase amount must be numeric.
- Membership input must be "yes" or "no" (case insensitive).
- Negative purchase amounts are not expected.
- Final price is formatted to two decimal places.

## Problem 2: Employee Performance Bonus
### Description
This program calculates an employee’s annual performance bonus based on their performance score.  
Conditional logic determines the appropriate bonus percentage, and the bonus amount is calculated as a percentage of the employee’s salary.
### Business Rules Implemented
- 90–100 → 20% bonus
- 80–89 → 10% bonus
- 70–79 → 5% bonus
- Below 70 → 0% bonus
### Functions
- determine_bonus_percentage(score)
- calculate_bonus_amount(salary, bonus_percent)
- main()
### Assumptions
- Salary must be numeric.
- Performance score must be between 0 and 100.
- Negative salaries are not expected.
- Bonus amount is formatted with commas and two decimal places.

## Problem 3: Loan Risk Classification
### Description
This program classifies a loan applicant’s risk level based on credit score and annual income using conditional logic.
### Business Rules Implemented
- Low Risk:
  - Credit score ≥ 720 AND income ≥ 60,000
- Medium Risk:
  - Credit score ≥ 650 AND income ≥ 40,000
- High Risk:
  - All other cases
### Functions
- classify_risk(credit_score, income)
- main()
### Assumptions
- Credit score and income must be numeric.
- Negative values are not expected.
- Output matches the required wording exactly.

