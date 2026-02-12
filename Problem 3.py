# Exercise 3: Loan Risk Classification

# Classifies loan applicants into risk categories based on their credit score and annual income.
def classify_risk(credit_score, income):
    if credit_score >= 720 and income >= 60000:
        return "Low Risk"
    elif credit_score >= 650 and income >= 40000:
        return "Medium Risk"
    else:
        return "High Risk"

# Main function to get user input and classify risk
def main():
    try:
        credit_score = float(input("Enter credit score: ").strip())
        income = float(input("Enter annual income: ").strip())
    except ValueError:
        print("Invalid input.")
        return

    category = classify_risk(credit_score, income)

    print(f"Loan Risk Category: {category}")


if __name__ == "__main__":
    main()
