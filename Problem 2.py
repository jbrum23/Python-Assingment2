# Exercise 2: Employee Performance Bonus


def determine_bonus_percentage(score):
    if score >= 90:
        return 20
    elif score >= 80:
        return 10
    elif score >= 70:
        return 5
    else:
        return 0


def calculate_bonus_amount(salary, percent):
    return salary * percent / 100


def main():
    try:
        salary = float(input("Enter annual salary: ").strip())
        score = float(input("Enter performance score (0-100): ").strip())
    except ValueError:
        print("Invalid input.")
        return

    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        return

    percent = determine_bonus_percentage(score)
    bonus = calculate_bonus_amount(salary, percent)

    print(f"Performance Bonus: {percent}%")
    print(f"Bonus Amount: ${bonus:,.2f}")


if __name__ == "__main__":
    main()
