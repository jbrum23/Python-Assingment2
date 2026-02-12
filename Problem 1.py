
def determine_discount(purchase_amount, membership_status):
    """
    Determines discount percentage based on purchase amount
    and membership status.
    """
    if membership_status == "yes":
        if purchase_amount >= 100:
            return 15
        else:
            return 5
    else:  # membership_status == "no"
        if purchase_amount >= 150:
            return 10
        else:
            return 0


def calculate_final_price(purchase_amount, discount_percent):
    """
    Calculates final price after applying discount.
    """
    discount_amount = purchase_amount * (discount_percent / 100)
    return purchase_amount - discount_amount


def main():
    # Get purchase amount safely
    try:
        purchase_amount = float(input("Enter purchase amount: ").strip())
    except ValueError:
        print("Invalid input. Please enter a numeric purchase amount.")
        return

    # Get membership status safely
    membership_status = input("Are you a member? (yes/no): ").strip().lower()

    if membership_status not in ["yes", "no"]:
        print("Invalid membership status. Please enter 'yes' or 'no'.")
        return

    # Determine discount and final price
    discount_percent = determine_discount(purchase_amount, membership_status)
    final_price = calculate_final_price(purchase_amount, discount_percent)

    # Output
    print(f"Discount applied: {discount_percent}%")
    print(f"Final price: ${final_price:.2f}")


# Run program
if __name__ == "__main__":
    main()
